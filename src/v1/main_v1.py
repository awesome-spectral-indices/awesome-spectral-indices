"""Build the Awesome Spectral Indices v1 catalogue outputs."""

import json
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import pandas as pd

from src.v1.SpectralIndex import parse_formula_variables
from src.v1.bands import bands
from src.v1.crossref import CrossrefClient, extract_doi, normalize_crossref_work
from src.v1.indices import spindex
from src.v1.references import add_reference_metadata
from src.v1.utils import (
    Bands,
    Constants,
    External,
    Polarizations,
    is_hyperspectral_band,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "output/v1"
SPECTRAL_INDICES_JSON = OUTPUT_DIR / "spectral-indices-dict.json"
SPECTRAL_INDICES_TABLE = OUTPUT_DIR / "spectral-indices-table.csv"
SPECTRAL_INDICES_CITATIONS = OUTPUT_DIR / "spectral-indices-citations.json"
SPECTRAL_INDICES_REFERENCES = OUTPUT_DIR / "spectral-indices-references.bib"

TABLE_COLUMNS = [
    "acronym",
    "name",
    "classification",
    "formula",
    "bands",
    "polarizations",
    "constants",
    "external_variables",
    "reductions",
    "source",
    "contributor",
    "date_of_addition",
]

SOURCE_CHECK_TIMEOUT = 12
SOURCE_CHECK_WORKERS = 16
SOURCE_CHECK_ATTEMPTS = 2
SOURCE_CHECK_USER_AGENT = (
    "Awesome-Spectral-Indices/1.0 "
    "(+https://github.com/awesome-spectral-indices/awesome-spectral-indices)"
)
CROSSREF_REFRESH_DAYS = 7


def load_json(path):
    """Load a JSON document from disk."""
    with path.open() as fp:
        return json.load(fp)


def check_source_link(source_link, timeout=SOURCE_CHECK_TIMEOUT):
    """Return whether an HTTP source link is operational or down."""
    request = Request(
        source_link,
        headers={
            "User-Agent": SOURCE_CHECK_USER_AGENT,
            "Range": "bytes=0-0",
        },
    )

    for _ in range(SOURCE_CHECK_ATTEMPTS):
        try:
            with urlopen(request, timeout=timeout) as response:
                status = response.getcode()
                if status is None or status < 400:
                    return "operational"
        except HTTPError as exc:
            if exc.code not in {404, 410} and exc.code < 500:
                return "operational"
        except (TimeoutError, URLError, OSError):
            pass

    return "down"


def add_formula_metadata(index_catalog):
    """Populate generated inputs, modalities, and normalized formula metadata."""
    band_names = set(Bands._value2member_map_)
    polarization_names = set(Polarizations._value2member_map_)
    thermal_names = {"T", "T1", "T2"}
    multispectral_names = band_names - thermal_names

    for key, spectral_index in index_catalog.SpectralIndices.items():
        variables = parse_formula_variables(spectral_index.formula)
        spectral_index.bands = [
            variable
            for variable in variables
            if variable in band_names or is_hyperspectral_band(variable)
        ]
        spectral_index.polarizations = [
            variable for variable in variables if variable in polarization_names
        ]
        modalities = []
        if any(band in multispectral_names for band in spectral_index.bands):
            modalities.append("multispectral")
        if any(is_hyperspectral_band(band) for band in spectral_index.bands):
            modalities.append("hyperspectral")
        if any(band in thermal_names for band in spectral_index.bands):
            modalities.append("thermal")
        if spectral_index.polarizations:
            modalities.append("radar")
        spectral_index.classification.sensing_modalities = modalities
        spectral_index.constants = spectral_index.constants or {}
        spectral_index.external_variables = spectral_index.external_variables or {}
        spectral_index.reductions = spectral_index.reductions or {}
        index_catalog.SpectralIndices[key] = spectral_index

    return index_catalog


def build_constants_metadata(index_catalog):
    """Group contributor-provided constant definitions by constant and index."""
    metadata = {constant.value: {} for constant in Constants}

    for key, spectral_index in index_catalog.SpectralIndices.items():
        for name, definition in (spectral_index.constants or {}).items():
            metadata[name][key] = definition.model_dump(mode="json")

    return metadata


def build_external_variables_metadata(index_catalog):
    """Group contributor-provided external descriptions by variable and index."""
    metadata = {external.value: {} for external in External}

    for key, spectral_index in index_catalog.SpectralIndices.items():
        for name, definition in (spectral_index.external_variables or {}).items():
            metadata[name][key] = definition.model_dump(mode="json")

    return metadata


def add_source_companions(index_catalog):
    """Populate each source with other catalogue keys sharing its exact URL."""
    keys_by_source_link = {}
    for key, spectral_index in index_catalog.SpectralIndices.items():
        keys_by_source_link.setdefault(spectral_index.source.source_link, []).append(
            key
        )

    for key, spectral_index in index_catalog.SpectralIndices.items():
        companions = [
            companion
            for companion in keys_by_source_link[spectral_index.source.source_link]
            if companion != key
        ]
        spectral_index.source.set_source_companions(companions)

    return index_catalog


def add_source_metadata(index_catalog, checker=check_source_link):
    """Check each unique source link and populate its generated status."""
    source_links = sorted(
        {
            spectral_index.source.source_link
            for spectral_index in index_catalog.SpectralIndices.values()
        }
    )
    worker_count = max(1, min(SOURCE_CHECK_WORKERS, len(source_links)))

    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        statuses = dict(zip(source_links, executor.map(checker, source_links)))

    for spectral_index in index_catalog.SpectralIndices.values():
        status = statuses[spectral_index.source.source_link]
        spectral_index.source.set_source_link_status(status)

    operational = sum(status == "operational" for status in statuses.values())
    print(
        f"Checked {len(statuses)} unique source links: "
        f"{operational} operational, {len(statuses) - operational} down."
    )
    return index_catalog


def load_crossref_cache(path=SPECTRAL_INDICES_JSON):
    """Load generated Crossref metadata from the previous catalogue output."""
    if not path.exists():
        return {}
    try:
        previous_indices = load_json(path)["SpectralIndices"]
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return {}

    cache = {}
    for key, index in previous_indices.items():
        source = index.get("source", {})
        doi = extract_doi(source.get("source_link", ""))
        metadata = source.get("source_metadata")
        if doi and isinstance(metadata, dict) and metadata.get("source") == "crossref":
            metadata = dict(metadata)
            source_type = metadata.pop("type", source.get("source_type"))
            record = cache.setdefault(
                doi,
                {
                    "metadata": metadata,
                    "source_types": {},
                },
            )
            record["source_types"][key] = source_type
    return cache


def crossref_metadata_is_fresh(metadata, today, refresh_days=CROSSREF_REFRESH_DAYS):
    """Return whether cached citation metadata is younger than the refresh window."""
    try:
        retrieved_on = date.fromisoformat(metadata["citations"]["date"])
    except (KeyError, TypeError, ValueError):
        return False
    return today - retrieved_on < timedelta(days=refresh_days)


def add_crossref_metadata(
    index_catalog,
    fetcher=None,
    today=None,
    cache_path=SPECTRAL_INDICES_JSON,
    refresh_days=CROSSREF_REFRESH_DAYS,
):
    """Populate generated publication metadata for every DOI-backed source."""
    today = today or date.today()
    cache = load_crossref_cache(cache_path)
    doi_sources = {}
    for key, spectral_index in index_catalog.SpectralIndices.items():
        doi = extract_doi(spectral_index.source.source_link)
        if doi:
            doi_sources.setdefault(doi, []).append((key, spectral_index.source))

    if fetcher is None:
        client = CrossrefClient(email=os.environ.get("CROSSREF_EMAIL"))
        fetcher = client.fetch_work

    records = {}
    cache_hits = 0
    refreshed = 0
    failed = 0
    for doi in sorted(doi_sources):
        cached = cache.get(doi)
        if cached and crossref_metadata_is_fresh(
            cached["metadata"], today, refresh_days
        ):
            records[doi] = cached
            cache_hits += 1
            continue

        message = fetcher(doi)
        if message is not None:
            metadata, source_type = normalize_crossref_work(message, today)
            records[doi] = {
                "metadata": metadata,
                "source_type": source_type,
                "source_types": {},
            }
            refreshed += 1
        elif cached:
            records[doi] = cached
            failed += 1
        else:
            records[doi] = {
                "metadata": {},
                "source_type": None,
                "source_types": {},
            }
            failed += 1

    for doi, sources in doi_sources.items():
        record = records[doi]
        for key, source in sources:
            inferred_source_type = record.get("source_type")
            if inferred_source_type is None:
                inferred_source_type = record.get("source_types", {}).get(key)
            source.set_source_metadata(
                record["metadata"],
                inferred_source_type=inferred_source_type,
            )

    print(
        f"Crossref metadata for {len(doi_sources)} unique DOIs: "
        f"{refreshed} refreshed, {cache_hits} cached, {failed} unavailable."
    )
    return index_catalog


def load_citation_history(path=SPECTRAL_INDICES_CITATIONS):
    """Load citation snapshots, accepting the initial single-object shape."""
    if not path.exists():
        return {}
    try:
        history = load_json(path)
    except (TypeError, ValueError, json.JSONDecodeError):
        return {}
    if not isinstance(history, dict):
        return {}

    normalized = {}
    for key, value in history.items():
        if isinstance(value, list):
            normalized[key] = value
        elif isinstance(value, dict):
            normalized[key] = [value]
    return normalized


def write_citation_history(index_catalog, path=SPECTRAL_INDICES_CITATIONS):
    """Append or update the latest dated citation snapshot for every index."""
    previous = load_citation_history(path)
    history = {}
    for key, spectral_index in index_catalog.SpectralIndices.items():
        snapshots = list(previous.get(key, []))
        citations = spectral_index.source.source_metadata.citations
        if citations is not None:
            citations = citations.model_dump(mode="json")
            snapshots = [
                snapshot
                for snapshot in snapshots
                if snapshot.get("date") != citations["date"]
            ]
            snapshots.append(citations)
            snapshots.sort(key=lambda snapshot: snapshot["date"])
        history[key] = snapshots

    with path.open("w") as fp:
        json.dump(history, fp, indent=4, sort_keys=True)
        fp.write("\n")

    return history


def write_json_outputs(index_catalog, bibtex_entries):
    """Write the v1 catalogue and its variable metadata as JSON."""
    with SPECTRAL_INDICES_JSON.open("w") as fp:
        json.dump(
            index_catalog.model_dump(mode="json"),
            fp,
            indent=4,
            sort_keys=True,
        )

    with (OUTPUT_DIR / "bands.json").open("w") as fp:
        json.dump(bands, fp, indent=4, sort_keys=True)

    with (OUTPUT_DIR / "constants.json").open("w") as fp:
        json.dump(
            build_constants_metadata(index_catalog),
            fp,
            indent=4,
            sort_keys=True,
        )

    with (OUTPUT_DIR / "external_variables.json").open("w") as fp:
        json.dump(
            build_external_variables_metadata(index_catalog),
            fp,
            indent=4,
            sort_keys=True,
        )

    write_citation_history(index_catalog)

    with SPECTRAL_INDICES_REFERENCES.open("w") as fp:
        fp.write("\n\n".join(bibtex_entries.values()))
        if bibtex_entries:
            fp.write("\n")


def build_indices_dataframe(path=SPECTRAL_INDICES_JSON):
    """Build the public v1 CSV dataframe from the generated catalogue JSON."""
    with path.open() as fp:
        indices = json.load(fp)

    df = pd.DataFrame(list(indices["SpectralIndices"].values()))
    return df[TABLE_COLUMNS]


def write_spectral_indices_table(df):
    """Write the flat v1 CSV table used as a machine-readable output."""
    df.to_csv(SPECTRAL_INDICES_TABLE, index=False)


def main():
    """Generate all v1 catalogue JSON and CSV outputs."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    index_catalog = add_formula_metadata(spindex)
    index_catalog = add_source_metadata(index_catalog)
    index_catalog = add_crossref_metadata(index_catalog)
    index_catalog = add_source_companions(index_catalog)
    bibtex_entries = add_reference_metadata(
        index_catalog, cache_path=SPECTRAL_INDICES_JSON
    )
    write_json_outputs(index_catalog, bibtex_entries)

    df = build_indices_dataframe()
    write_spectral_indices_table(df)


if __name__ == "__main__":
    main()

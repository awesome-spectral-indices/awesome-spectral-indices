"""Build the Awesome Spectral Indices v1 catalogue outputs."""

import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import pandas as pd

from src.v1.SpectralIndex import parse_formula_variables
from src.v1.bands import bands
from src.v1.constants import constants
from src.v1.indices import spindex
from src.v1.utils import Bands, Constants


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "output/v1"
SPECTRAL_INDICES_JSON = OUTPUT_DIR / "spectral-indices-dict.json"
SPECTRAL_INDICES_TABLE = OUTPUT_DIR / "spectral-indices-table.csv"

TABLE_COLUMNS = [
    "acronym",
    "name",
    "application_domain",
    "formula",
    "bands",
    "constants",
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
    """Populate each index with its bands and constant defaults."""
    band_names = set(Bands._value2member_map_)
    constant_names = set(Constants._value2member_map_)

    for key, spectral_index in index_catalog.SpectralIndices.items():
        variables = parse_formula_variables(spectral_index.formula)
        spectral_index.bands = [
            variable for variable in variables if variable in band_names
        ]
        spectral_index.constants = {
            variable: constants[variable]["default"]
            for variable in variables
            if variable in constant_names
        }
        index_catalog.SpectralIndices[key] = spectral_index

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


def write_json_outputs(index_catalog):
    """Write the v1 catalogue, band metadata, and constants metadata as JSON."""
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
        json.dump(constants, fp, indent=4, sort_keys=True)


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
    write_json_outputs(index_catalog)

    df = build_indices_dataframe()
    write_spectral_indices_table(df)


if __name__ == "__main__":
    main()

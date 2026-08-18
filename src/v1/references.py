"""Generate shared BibTeX and APA references from source metadata."""

import json
import re

from src.v1.crossref import extract_doi


BIBTEX_ENTRY_TYPES = {
    "article": "article",
    "book": "book",
    "book_chapter": "incollection",
    "conference_paper": "inproceedings",
    "poster": "inproceedings",
    "report": "techreport",
    "preprint": "misc",
}


def _sentence(value):
    """Return text with terminal punctuation."""
    if not value:
        return None
    value = str(value).strip()
    return value if value.endswith((".", "!", "?")) else f"{value}."


def _bibtex_escape(value):
    """Escape characters with structural meaning in BibTeX field values."""
    value = str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(replacements.get(character, character) for character in value)


def reference_key(index_key, used_keys, preferred_key=None):
    """Return a deterministic unique BibTeX key based on a catalogue key."""
    if preferred_key and re.fullmatch(r"[A-Za-z0-9_:.+-]+", preferred_key):
        base = preferred_key
    else:
        base = "ASI_" + re.sub(r"[^A-Za-z0-9_:.+-]", "_", index_key)
    candidate = base
    suffix = 2
    while candidate.casefold() in used_keys:
        candidate = f"{base}_{suffix}"
        suffix += 1
    used_keys.add(candidate.casefold())
    return candidate


def source_identity(source_link):
    """Return the stable identity used to deduplicate one scientific source."""
    doi = extract_doi(source_link)
    return f"doi:{doi}" if doi else f"url:{source_link.strip()}"


def load_reference_key_cache(path):
    """Load previously generated bibliography keys by source identity."""
    if path is None or not path.exists():
        return {}
    try:
        with path.open() as fp:
            indices = json.load(fp)["SpectralIndices"]
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return {}

    keys = {}
    for index in indices.values():
        source = index.get("source", {})
        how_to_cite = source.get("source_metadata", {}).get("how_to_cite", {})
        key = how_to_cite.get("bibtex")
        source_link = source.get("source_link")
        if key and source_link:
            keys.setdefault(source_identity(source_link), key)
    return keys


def format_apa_citation(metadata, source_link):
    """Build a readable APA-style citation from normalized metadata."""
    authors = metadata.get("authors") or []
    if len(authors) == 1:
        author_text = authors[0]
    elif len(authors) == 2:
        author_text = f"{authors[0]}, & {authors[1]}"
    elif authors:
        author_text = ", ".join(authors[:-1]) + f", & {authors[-1]}"
    else:
        author_text = None

    year_text = f"({metadata['year']})." if metadata.get("year") else "(n.d.)."
    parts = []
    if author_text:
        parts.append(f"{author_text} {year_text}")
    else:
        parts.append(year_text)

    title = _sentence(metadata.get("title"))
    if title:
        parts.append(title)

    publication = metadata.get("journal")
    volume = metadata.get("volume")
    issue = metadata.get("issue")
    if publication:
        publication_text = publication
        if volume:
            publication_text += f", {volume}"
        if issue:
            publication_text += f"({issue})"
        parts.append(_sentence(publication_text))

    doi = extract_doi(source_link)
    parts.append(f"https://doi.org/{doi}" if doi else source_link)
    return " ".join(part for part in parts if part)


def format_bibtex_entry(key, metadata, source_link):
    """Build one BibTeX entry from normalized publication metadata."""
    source_type = metadata.get("type")
    entry_type = BIBTEX_ENTRY_TYPES.get(source_type, "misc")
    fields = []

    authors = metadata.get("authors") or []
    if authors:
        fields.append(("author", " and ".join(authors)))
    if metadata.get("title"):
        fields.append(("title", metadata["title"]))
    if metadata.get("journal"):
        venue_fields = {
            "article": "journal",
            "book": "series",
            "book_chapter": "booktitle",
            "conference_paper": "booktitle",
            "poster": "booktitle",
            "report": "institution",
            "preprint": "howpublished",
        }
        venue_field = venue_fields.get(source_type, "howpublished")
        fields.append((venue_field, metadata["journal"]))
    if metadata.get("volume"):
        fields.append(("volume", metadata["volume"]))
    if metadata.get("issue"):
        fields.append(("number", metadata["issue"]))
    if metadata.get("year"):
        fields.append(("year", metadata["year"]))

    doi = extract_doi(source_link)
    if doi:
        fields.append(("doi", doi))
        fields.append(("url", f"https://doi.org/{doi}"))
    elif source_link:
        fields.append(("url", source_link))

    rendered_fields = ",\n".join(
        f"  {name} = {{{_bibtex_escape(value)}}}" for name, value in fields
    )
    return f"@{entry_type}{{{key},\n{rendered_fields}\n}}"


def add_reference_metadata(index_catalog, cache_path=None):
    """Attach shared citation data and return unique rendered BibTeX entries."""
    indices_by_source = {}
    preferred_keys = load_reference_key_cache(cache_path)
    for key, spectral_index in index_catalog.SpectralIndices.items():
        metadata = spectral_index.source.source_metadata.model_dump(
            mode="json", exclude_none=True
        )
        has_citation_data = any(
            metadata.get(field) for field in ("authors", "journal", "title", "year")
        )
        if metadata.get("source") and has_citation_data:
            identity = source_identity(spectral_index.source.source_link)
            indices_by_source.setdefault(identity, []).append((key, spectral_index))

    entries = {}
    used_keys = set()
    for identity in sorted(indices_by_source):
        indices = sorted(indices_by_source[identity], key=lambda item: item[0])
        representative = indices[0][1]
        existing_citation = representative.source.source_metadata.how_to_cite
        preferred_key = (
            existing_citation.bibtex
            if existing_citation
            else preferred_keys.get(identity)
        )
        key = reference_key(indices[0][0], used_keys, preferred_key)
        metadata = representative.source.source_metadata.model_dump(
            mode="json", exclude_none=True
        )
        apa = format_apa_citation(metadata, representative.source.source_link)
        entries[key] = format_bibtex_entry(
            key, metadata, representative.source.source_link
        )
        for _, spectral_index in indices:
            spectral_index.source.set_how_to_cite(key, apa)

    return entries

"""Retrieve and normalize publication metadata from the Crossref REST API."""

import json
import time
from datetime import date
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlencode, urlsplit
from urllib.request import Request, urlopen


CROSSREF_API_URL = "https://api.crossref.org/works"
CROSSREF_TIMEOUT = 20
CROSSREF_ATTEMPTS = 4
CROSSREF_POLITE_INTERVAL = 0.15
CROSSREF_PUBLIC_INTERVAL = 0.25
CROSSREF_USER_AGENT = (
    "Awesome-Spectral-Indices/1.0 "
    "(+https://github.com/awesome-spectral-indices/awesome-spectral-indices)"
)

CROSSREF_SOURCE_TYPES = {
    "journal-article": "article",
    "book": "book",
    "edited-book": "book",
    "monograph": "book",
    "reference-book": "book",
    "book-chapter": "book_chapter",
    "book-part": "book_chapter",
    "book-section": "book_chapter",
    "reference-entry": "book_chapter",
    "proceedings": "conference_paper",
    "proceedings-article": "conference_paper",
    "posted-content": "preprint",
    "report": "report",
    "report-series": "report",
}


def extract_doi(source_link):
    """Extract a DOI from a supported DOI resolver URL."""
    parsed = urlsplit(source_link)
    if (parsed.hostname or "").lower() not in {
        "doi.org",
        "dx.doi.org",
        "www.doi.org",
    }:
        return None
    doi = unquote(parsed.path).lstrip("/").strip()
    return doi.casefold() or None


def _first_text(message, field):
    """Return the first non-empty string from a Crossref list field."""
    value = message.get(field)
    if isinstance(value, list):
        value = next(
            (item.strip() for item in value if isinstance(item, str) and item.strip()),
            None,
        )
    elif isinstance(value, str):
        value = value.strip() or None
    else:
        value = None
    return value


def _author_name(author):
    """Return one display name from a Crossref author record."""
    if not isinstance(author, dict):
        return None
    literal_name = author.get("name")
    if isinstance(literal_name, str) and literal_name.strip():
        return literal_name.strip()
    parts = [author.get("given"), author.get("family")]
    name = " ".join(part.strip() for part in parts if isinstance(part, str) and part.strip())
    return name or None


def _publication_year(message):
    """Return the best available publication year from Crossref date fields."""
    for field in ("published-print", "published-online", "published", "issued"):
        value = message.get(field)
        try:
            year = value["date-parts"][0][0]
        except (KeyError, IndexError, TypeError):
            continue
        if isinstance(year, int) and not isinstance(year, bool):
            return year
    return None


def normalize_crossref_work(message, retrieved_on=None):
    """Convert one Crossref work record into catalogue source metadata."""
    if not isinstance(message, dict):
        raise ValueError("Crossref work metadata must be an object.")

    authors = [
        name
        for name in (_author_name(author) for author in message.get("author", []))
        if name
    ]
    citation_count = message.get("is-referenced-by-count")
    citations_metrics = None
    if isinstance(citation_count, int) and not isinstance(citation_count, bool):
        citations_metrics = {
            "citation_count": max(0, citation_count),
            "date": (retrieved_on or date.today()).isoformat(),
        }

    metadata = {
        "title": _first_text(message, "title"),
        "journal": _first_text(message, "container-title"),
        "volume": str(message["volume"]).strip() if message.get("volume") else None,
        "issue": str(message["issue"]).strip() if message.get("issue") else None,
        "authors": authors or None,
        "year": _publication_year(message),
        "citations_metrics": citations_metrics,
        "source": "crossref",
    }
    metadata = {key: value for key, value in metadata.items() if value is not None}
    source_type = CROSSREF_SOURCE_TYPES.get(message.get("type"))
    return metadata, source_type


def _retry_delay(error, attempt):
    """Return a bounded retry delay, honoring Retry-After when available."""
    retry_after = error.headers.get("Retry-After") if error.headers else None
    if retry_after:
        try:
            return min(30.0, max(0.0, float(retry_after)))
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(retry_after)
                return min(
                    30.0,
                    max(0.0, retry_at.timestamp() - time.time()),
                )
            except (TypeError, ValueError, OverflowError):
                pass
    return min(30.0, 2.0**attempt)


class CrossrefClient:
    """Small sequential Crossref client with throttling and retry backoff."""

    def __init__(self, email=None, opener=urlopen, sleeper=time.sleep):
        self.email = email.strip() if email else None
        self.opener = opener
        self.sleeper = sleeper
        self.interval = (
            CROSSREF_POLITE_INTERVAL if self.email else CROSSREF_PUBLIC_INTERVAL
        )
        self._last_request_at = None

    def _throttle(self):
        """Keep sequential requests below the applicable published limit."""
        if self._last_request_at is not None:
            elapsed = time.monotonic() - self._last_request_at
            if elapsed < self.interval:
                self.sleeper(self.interval - elapsed)

    def fetch_work(self, doi):
        """Return a Crossref work message, or None after bounded failures."""
        query = urlencode({"mailto": self.email}) if self.email else ""
        url = f"{CROSSREF_API_URL}/{quote(doi, safe='')}"
        if query:
            url = f"{url}?{query}"
        request = Request(
            url,
            headers={
                "Accept": "application/json",
                "User-Agent": CROSSREF_USER_AGENT,
            },
        )

        for attempt in range(CROSSREF_ATTEMPTS):
            self._throttle()
            try:
                with self.opener(request, timeout=CROSSREF_TIMEOUT) as response:
                    self._last_request_at = time.monotonic()
                    payload = json.load(response)
                message = payload.get("message")
                return message if isinstance(message, dict) else None
            except HTTPError as error:
                self._last_request_at = time.monotonic()
                if error.code == 404:
                    return None
                if error.code != 429 and error.code < 500:
                    return None
                if attempt + 1 < CROSSREF_ATTEMPTS:
                    self.sleeper(_retry_delay(error, attempt))
            except (TimeoutError, URLError, OSError, json.JSONDecodeError):
                self._last_request_at = time.monotonic()
                if attempt + 1 < CROSSREF_ATTEMPTS:
                    self.sleeper(min(30.0, 2.0**attempt))

        return None

"""Retrieve and normalize metadata from the Semantic Scholar Graph API."""

import json
import time
from datetime import date
from email.utils import parsedate_to_datetime
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


SEMANTIC_SCHOLAR_BATCH_URL = (
    "https://api.semanticscholar.org/graph/v1/paper/batch"
)
SEMANTIC_SCHOLAR_FIELDS = (
    "paperId",
    "corpusId",
    "title",
    "venue",
    "year",
    "authors",
    "citationCount",
    "publicationTypes",
    "journal",
)
SEMANTIC_SCHOLAR_BATCH_SIZE = 500
SEMANTIC_SCHOLAR_TIMEOUT = 30
SEMANTIC_SCHOLAR_ATTEMPTS = 4
# The introductory authenticated limit is one request per second across all
# endpoints. A small margin keeps this client below that threshold.
SEMANTIC_SCHOLAR_INTERVAL = 1.1
SEMANTIC_SCHOLAR_USER_AGENT = (
    "Awesome-Spectral-Indices/1.0 "
    "(+https://github.com/awesome-spectral-indices/awesome-spectral-indices)"
)

SEMANTIC_SCHOLAR_SOURCE_TYPES = {
    "JournalArticle": "article",
    "Review": "article",
    "CaseReport": "article",
    "ClinicalTrial": "article",
    "Editorial": "article",
    "LettersAndComments": "article",
    "MetaAnalysis": "article",
    "News": "article",
    "Study": "article",
    "Conference": "conference_paper",
    "Book": "book",
    "BookSection": "book_chapter",
}
SEMANTIC_SCHOLAR_SOURCE_TYPE_PRIORITY = (
    "BookSection",
    "Book",
    "Conference",
    "JournalArticle",
    "Review",
    "CaseReport",
    "ClinicalTrial",
    "Editorial",
    "LettersAndComments",
    "MetaAnalysis",
    "News",
    "Study",
)


def _text(value):
    """Return stripped text or None for unavailable values."""
    return value.strip() if isinstance(value, str) and value.strip() else None


def _source_type(publication_types):
    """Map the most specific supported publication type to the v1 schema."""
    if not isinstance(publication_types, list):
        return None
    available = {
        value for value in publication_types if isinstance(value, str)
    }
    for value in SEMANTIC_SCHOLAR_SOURCE_TYPE_PRIORITY:
        if value in available:
            return SEMANTIC_SCHOLAR_SOURCE_TYPES[value]
    return None


def normalize_semantic_scholar_paper(paper, retrieved_on=None):
    """Convert one Semantic Scholar paper record into source metadata."""
    if not isinstance(paper, dict):
        raise ValueError("Semantic Scholar paper metadata must be an object.")

    journal = paper.get("journal")
    journal = journal if isinstance(journal, dict) else {}
    venue = _text(journal.get("name")) or _text(paper.get("venue"))
    volume = _text(journal.get("volume"))
    authors = [
        name
        for name in (
            _text(author.get("name"))
            for author in paper.get("authors", [])
            if isinstance(author, dict)
        )
        if name
    ]

    year = paper.get("year")
    if isinstance(year, bool) or not isinstance(year, int):
        year = None

    citation_count = paper.get("citationCount")
    citations = None
    if isinstance(citation_count, int) and not isinstance(citation_count, bool):
        citations = {
            "citation_count": max(0, citation_count),
            "date": (retrieved_on or date.today()).isoformat(),
        }

    metadata = {
        "title": _text(paper.get("title")),
        "journal": venue,
        "volume": volume,
        "authors": authors or None,
        "year": year,
        "citations": citations,
        "source": "semantic_scholar",
    }
    metadata = {key: value for key, value in metadata.items() if value is not None}
    return metadata, _source_type(paper.get("publicationTypes"))


def _retry_delay(error, attempt):
    """Return bounded backoff while honoring a Retry-After response header."""
    retry_after = error.headers.get("Retry-After") if error.headers else None
    if retry_after:
        try:
            return min(30.0, max(0.0, float(retry_after)))
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(retry_after)
                return min(30.0, max(0.0, retry_at.timestamp() - time.time()))
            except (TypeError, ValueError, OverflowError):
                pass
    return min(30.0, 2.0**attempt)


class SemanticScholarClient:
    """Sequential batch client that stays below one request per second."""

    def __init__(self, api_key=None, opener=urlopen, sleeper=time.sleep):
        self.api_key = api_key.strip() if api_key else None
        self.opener = opener
        self.sleeper = sleeper
        self._last_request_at = None

    def _throttle(self):
        """Keep all requests made by this client below the API-key limit."""
        if self._last_request_at is not None:
            elapsed = time.monotonic() - self._last_request_at
            if elapsed < SEMANTIC_SCHOLAR_INTERVAL:
                self.sleeper(SEMANTIC_SCHOLAR_INTERVAL - elapsed)

    def _fetch_batch(self, paper_ids):
        """Return one response item per submitted ID, using None on failure."""
        query = urlencode({"fields": ",".join(SEMANTIC_SCHOLAR_FIELDS)})
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": SEMANTIC_SCHOLAR_USER_AGENT,
        }
        if self.api_key:
            headers["x-api-key"] = self.api_key
        request = Request(
            f"{SEMANTIC_SCHOLAR_BATCH_URL}?{query}",
            data=json.dumps({"ids": paper_ids}).encode("utf-8"),
            headers=headers,
            method="POST",
        )

        for attempt in range(SEMANTIC_SCHOLAR_ATTEMPTS):
            self._throttle()
            try:
                with self.opener(
                    request, timeout=SEMANTIC_SCHOLAR_TIMEOUT
                ) as response:
                    self._last_request_at = time.monotonic()
                    payload = json.load(response)
                if isinstance(payload, list) and len(payload) == len(paper_ids):
                    return [
                        item if isinstance(item, dict) else None
                        for item in payload
                    ]
                return [None] * len(paper_ids)
            except HTTPError as error:
                self._last_request_at = time.monotonic()
                if error.code != 429 and error.code < 500:
                    return [None] * len(paper_ids)
                if attempt + 1 < SEMANTIC_SCHOLAR_ATTEMPTS:
                    self.sleeper(_retry_delay(error, attempt))
            except (TimeoutError, URLError, OSError, json.JSONDecodeError):
                self._last_request_at = time.monotonic()
                if attempt + 1 < SEMANTIC_SCHOLAR_ATTEMPTS:
                    self.sleeper(min(30.0, 2.0**attempt))

        return [None] * len(paper_ids)

    def fetch_papers(self, paper_ids):
        """Fetch up to 500 papers per rate-limited batch request."""
        paper_ids = list(paper_ids)
        papers = []
        for start in range(0, len(paper_ids), SEMANTIC_SCHOLAR_BATCH_SIZE):
            batch = paper_ids[start : start + SEMANTIC_SCHOLAR_BATCH_SIZE]
            papers.extend(self._fetch_batch(batch))
        return papers

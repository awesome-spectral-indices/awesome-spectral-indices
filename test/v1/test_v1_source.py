import json
from datetime import date
from io import BytesIO

import pytest
from pydantic import ValidationError

from src.v1.SpectralIndex import Source, SourceMetadata, SpectralIndex
from src.v1.crossref import extract_doi, normalize_crossref_work
from src.v1.indices import SpectralIndices, spindex
from src.v1.main_v1 import (
    add_citation_metrics,
    add_crossref_metadata,
    add_semantic_scholar_metadata,
    add_source_companions,
    add_source_metadata,
    migrate_cached_citation_metadata,
    write_citation_history,
)
from src.v1.semantic_scholar import (
    SEMANTIC_SCHOLAR_BATCH_SIZE,
    SEMANTIC_SCHOLAR_INTERVAL,
    SemanticScholarClient,
    normalize_semantic_scholar_paper,
)
from src.v1.references import (
    add_reference_metadata,
    format_apa_citation,
    format_bibtex_entry,
)


def test_source_link_type_is_generated_from_the_url():
    assert (
        Source(source_link="https://doi.org/10.1234/example").source_link_type == "doi"
    )
    assert (
        Source(source_link="http://dx.doi.org/10.1234/example").source_link_type
        == "doi"
    )
    assert Source(source_link="https://example.com/paper").source_link_type == "other"


def test_semantic_scholar_source_identifiers_are_optional_and_validated():
    source = Source(
        source_link="https://example.com/source",
        source_link_semantic_scholar={
            "paper_id": "AbC123",
            "corpus_id": 123456,
        },
    )

    assert source.source_link_semantic_scholar.paper_id == "AbC123"
    assert source.source_link_semantic_scholar.corpus_id == 123456
    assert (
        Source(source_link="https://example.com/source").source_link_semantic_scholar
        is None
    )


@pytest.mark.parametrize("paper_id", ["", "abc-123", "abc 123", 123])
def test_semantic_scholar_paper_id_rejects_non_alphanumeric_values(paper_id):
    with pytest.raises(ValidationError):
        Source(
            source_link="https://example.com/source",
            source_link_semantic_scholar={"paper_id": paper_id},
        )


@pytest.mark.parametrize("corpus_id", [-1, 1.5, "123", True])
def test_semantic_scholar_corpus_id_requires_a_non_negative_integer(corpus_id):
    with pytest.raises(ValidationError):
        Source(
            source_link="https://example.com/source",
            source_link_semantic_scholar={"corpus_id": corpus_id},
        )


def test_source_companions_are_empty_before_generation():
    source = Source(source_link="https://example.com/source")

    assert source.source_companions == []


def test_source_metadata_is_empty_before_generation():
    source = Source(source_link="https://doi.org/10.1234/example")

    assert source.source_metadata.model_dump(mode="json") == {}


@pytest.mark.parametrize(
    "source_type",
    [
        "article",
        "book",
        "book_chapter",
        "conference_paper",
        "poster",
        "report",
        "preprint",
    ],
)
def test_source_type_accepts_supported_values(source_type):
    source = Source(
        source_link="https://example.com/source",
        source_metadata={"type": source_type, "source": "contributor"},
    )
    assert source.source_metadata.type == source_type


def test_source_type_rejects_unsupported_values():
    with pytest.raises(ValidationError):
        Source(
            source_link="https://example.com/source",
            source_metadata={"type": "website", "source": "contributor"},
        )


def test_contributed_source_metadata_requires_provenance():
    with pytest.raises(ValidationError, match="source to 'contributor'"):
        Source(
            source_link="https://example.com/source",
            source_metadata={"title": "A contributed title"},
        )

    source = Source(
        source_link="https://example.com/source",
        source_metadata={
            "type": "report",
            "title": "A contributed title",
            "journal": "Example series",
            "volume": "2",
            "issue": "1",
            "authors": ["Example Author"],
            "year": 2024,
            "source": "contributor",
        },
    )
    assert source.source_metadata.source == "contributor"


@pytest.mark.parametrize("generated_field", ["citations_metrics", "how_to_cite"])
def test_contributors_cannot_submit_generated_citation_metadata(generated_field):
    values = {
        "citations_metrics": {
            "citation_count": 1,
            "date": "2026-08-18",
        },
        "how_to_cite": {"bibtex": "ASI_TEST", "apa": "A citation."},
    }
    with pytest.raises(ValidationError, match="cannot provide generated"):
        Source(
            source_link="https://example.com/source",
            source_metadata={
                "source": "contributor",
                generated_field: values[generated_field],
            },
        )


def test_source_metadata_validates_generated_values():
    metadata = SourceMetadata(
        title="A publication",
        authors=["Ada Lovelace", "Grace Hopper"],
        year=2026,
        citations_metrics={"citation_count": 12, "date": "2026-08-18"},
        source="crossref",
    )

    assert metadata.citations_metrics.citation_count == 12
    with pytest.raises(ValidationError):
        SourceMetadata(
            citations_metrics={"citation_count": -1, "date": "2026-08-18"}
        )

    semantic_scholar = SourceMetadata(source="semantic_scholar")
    assert semantic_scholar.source == "semantic_scholar"


def test_citation_metrics_rank_overall_age_and_application_domain_cohorts():
    def make_index(key, count, year, domain):
        index = SpectralIndex(
            acronym=key,
            name=f"{key} name",
            formula="N",
            source={"source_link": f"https://example.com/{key}"},
            classification={"application_domain": domain},
            date_of_addition="2026-08-20",
            contributor="https://github.com/example",
        )
        metadata = {
            "citations_metrics": {
                "citation_count": count,
                "date": "2026-08-20",
            },
            "source": "crossref",
        }
        if year is not None:
            metadata["year"] = year
        index.source.set_source_metadata(metadata)
        return index

    catalogue = SpectralIndices(
        SpectralIndices={
            "A": make_index("A", 100, 2020, "vegetation"),
            "B": make_index("B", 100, 2020, "vegetation"),
            "C": make_index("C", 50, 2022, "vegetation"),
            "D": make_index("D", 10, 2024, "vegetation"),
            "E": make_index("E", 60, 2020, "water"),
            "F": make_index("F", 5, None, "water"),
        }
    )

    add_citation_metrics(catalogue)

    first = catalogue.SpectralIndices["A"].source.source_metadata.citations_metrics
    tied = catalogue.SpectralIndices["B"].source.source_metadata.citations_metrics
    water = catalogue.SpectralIndices["E"].source.source_metadata.citations_metrics
    undated = catalogue.SpectralIndices["F"].source.source_metadata.citations_metrics

    assert first.overall.model_dump() == {
        "rank": 1,
        "rank_similar_age": 1,
        "percentile": 100.0,
        "percentile_similar_age": 100.0,
        "similar_age_count": 4,
    }
    assert tied.overall.rank == 2
    assert tied.overall.percentile == 100.0
    assert first.within_application_domain.rank == 1
    assert first.within_application_domain.rank_similar_age == 1
    assert first.within_application_domain.similar_age_count == 3
    assert water.overall.rank == 3
    assert water.overall.percentile == 66.67
    assert water.within_application_domain.rank == 1
    assert undated.overall.rank == 6
    assert undated.overall.rank_similar_age is None
    assert undated.within_application_domain.rank_similar_age is None
    assert undated.overall.similar_age_count == 0
    assert undated.within_application_domain.similar_age_count == 0


def test_cached_citation_metrics_keep_only_the_provider_snapshot():
    metadata = migrate_cached_citation_metadata(
        {
            "title": "Cached publication",
            "citations_metrics": {
                "citation_count": 42,
                "date": "2026-08-20",
                "overall": {"rank": 1},
                "similar_age_count": 9,
            },
        }
    )

    assert metadata == {
        "title": "Cached publication",
        "citations_metrics": {
            "citation_count": 42,
            "date": "2026-08-20",
        },
    }


def test_crossref_work_normalization_and_source_type_mapping():
    message = {
        "title": ["A spectral-index publication"],
        "container-title": ["Remote Sensing Proceedings"],
        "volume": "12",
        "issue": "3",
        "author": [
            {"given": "Ada", "family": "Lovelace"},
            {"name": "Example Research Group"},
        ],
        "published-print": {"date-parts": [[2025, 6, 1]]},
        "is-referenced-by-count": 42,
        "type": "proceedings-article",
    }

    metadata, source_type = normalize_crossref_work(
        message, retrieved_on=date(2026, 8, 18)
    )

    assert metadata == {
        "title": "A spectral-index publication",
        "journal": "Remote Sensing Proceedings",
        "volume": "12",
        "issue": "3",
        "authors": ["Ada Lovelace", "Example Research Group"],
        "year": 2025,
        "citations_metrics": {
            "citation_count": 42,
            "date": "2026-08-18",
        },
        "source": "crossref",
    }
    assert source_type == "conference_paper"


def test_semantic_scholar_paper_normalization_and_source_type_mapping():
    metadata, source_type = normalize_semantic_scholar_paper(
        {
            "title": "A spectral-index publication",
            "venue": "Fallback venue",
            "journal": {
                "name": "Remote Sensing Journal",
                "volume": "12",
            },
            "authors": [
                {"authorId": "1", "name": "Ada Lovelace"},
                {"authorId": "2", "name": "Grace Hopper"},
            ],
            "year": 2025,
            "citationCount": 42,
            "publicationTypes": ["Review", "JournalArticle"],
        },
        retrieved_on=date(2026, 8, 19),
    )

    assert metadata == {
        "title": "A spectral-index publication",
        "journal": "Remote Sensing Journal",
        "volume": "12",
        "authors": ["Ada Lovelace", "Grace Hopper"],
        "year": 2025,
        "citations_metrics": {
            "citation_count": 42,
            "date": "2026-08-19",
        },
        "source": "semantic_scholar",
    }
    assert source_type == "article"


def test_semantic_scholar_batch_client_uses_api_key_and_rate_limit():
    requests = []
    delays = []

    def opener(request, timeout):
        requests.append((request, timeout))
        ids = json.loads(request.data)["ids"]
        return BytesIO(
            json.dumps([{"paperId": paper_id} for paper_id in ids]).encode()
        )

    client = SemanticScholarClient(
        api_key="secret-key",
        opener=opener,
        sleeper=delays.append,
    )
    ids = [f"paper{number}" for number in range(SEMANTIC_SCHOLAR_BATCH_SIZE + 1)]

    papers = client.fetch_papers(ids)

    assert [paper["paperId"] for paper in papers] == ids
    assert len(requests) == 2
    assert all(request.method == "POST" for request, _ in requests)
    assert all(
        dict(request.header_items()).get("X-api-key") == "secret-key"
        for request, _ in requests
    )
    assert delays and delays[-1] > 1.0
    assert SEMANTIC_SCHOLAR_INTERVAL > 1.0


def test_semantic_scholar_falls_back_from_paper_id_to_corpus_id(tmp_path):
    def make_index(acronym, source):
        return SpectralIndex(
            acronym=acronym,
            name=f"{acronym} name",
            formula="N",
            source=source,
            classification={"application_domain": "vegetation"},
            date_of_addition="2026-08-19",
            contributor="https://github.com/example",
        )

    shared_link = "https://example.com/shared-source"
    catalogue = SpectralIndices(
        SpectralIndices={
            "ONE": make_index(
                "ONE",
                {
                    "source_link": shared_link,
                    "source_link_semantic_scholar": {
                        "paper_id": "missingpaper",
                        "corpus_id": 123,
                    },
                },
            ),
            "TWO": make_index("TWO", {"source_link": shared_link}),
            "DOI_FALLBACK": make_index(
                "DOI_FALLBACK",
                {
                    "source_link": "https://doi.org/10.1234/unavailable",
                    "source_link_semantic_scholar": {"paper_id": "foundpaper"},
                },
            ),
            "CROSSREF": make_index(
                "CROSSREF",
                {
                    "source_link": "https://doi.org/10.1234/available",
                    "source_link_semantic_scholar": {"paper_id": "unusedpaper"},
                },
            ),
        }
    )
    catalogue.SpectralIndices["CROSSREF"].source.set_source_metadata(
        {"title": "Crossref record", "source": "crossref"},
        inferred_source_type="article",
    )
    calls = []

    def fetcher(ids):
        calls.append(ids)
        records = {
            "missingpaper": None,
            "foundpaper": {
                "title": "DOI fallback paper",
                "citationCount": 9,
                "publicationTypes": ["Conference"],
            },
            "CorpusId:123": {
                "title": "Shared source paper",
                "citationCount": 7,
                "publicationTypes": ["JournalArticle"],
            },
        }
        return [records.get(identifier) for identifier in ids]

    add_semantic_scholar_metadata(
        catalogue,
        fetcher=fetcher,
        today=date(2026, 8, 19),
        cache_path=tmp_path / "missing.json",
    )

    assert calls == [["foundpaper", "missingpaper"], ["CorpusId:123"]]
    assert (
        catalogue.SpectralIndices["ONE"].source.source_metadata.title
        == "Shared source paper"
    )
    assert (
        catalogue.SpectralIndices["TWO"].source.source_metadata.source
        == "semantic_scholar"
    )
    assert catalogue.SpectralIndices["ONE"].source.source_metadata.type == "article"
    assert (
        catalogue.SpectralIndices["DOI_FALLBACK"].source.source_metadata.type
        == "conference_paper"
    )
    assert (
        catalogue.SpectralIndices["CROSSREF"].source.source_metadata.title
        == "Crossref record"
    )


def test_semantic_scholar_reuses_fresh_generated_metadata(tmp_path):
    source_link = "https://example.com/cached-source"
    cache_path = tmp_path / "catalogue.json"
    cache_path.write_text(
        json.dumps(
            {
                "SpectralIndices": {
                    "CACHED": {
                        "source": {
                            "source_link": source_link,
                            "source_link_semantic_scholar": {
                                "paper_id": "cachedpaper"
                            },
                            "source_metadata": {
                                "type": "article",
                                "title": "Cached paper",
                                "citations": {
                                    "citation_count": 5,
                                    "date": "2026-08-18",
                                },
                                "source": "semantic_scholar",
                            },
                        }
                    }
                }
            }
        )
    )
    index = SpectralIndex(
        acronym="CACHED",
        name="Cached index",
        formula="N",
        source={
            "source_link": source_link,
            "source_link_semantic_scholar": {"paper_id": "cachedpaper"},
        },
        classification={"application_domain": "vegetation"},
        date_of_addition="2026-08-19",
        contributor="https://github.com/example",
    )
    catalogue = SpectralIndices(SpectralIndices={"CACHED": index})

    def unexpected_fetch(ids):
        raise AssertionError(f"Unexpected Semantic Scholar request: {ids}")

    add_semantic_scholar_metadata(
        catalogue,
        fetcher=unexpected_fetch,
        today=date(2026, 8, 19),
        cache_path=cache_path,
    )

    assert index.source.source_metadata.title == "Cached paper"
    assert index.source.source_metadata.type == "article"
    assert index.source.source_metadata.source == "semantic_scholar"


def test_crossref_generation_reuses_each_doi_and_overwrites_contributed_metadata(
    tmp_path,
):
    shared_doi = "https://doi.org/10.1234/Shared-DOI"

    def make_index(acronym, source):
        return SpectralIndex(
            acronym=acronym,
            name=f"{acronym} name",
            formula="N",
            source=source,
            classification={"application_domain": "vegetation"},
            date_of_addition="2026-08-18",
            contributor="https://github.com/example",
        )

    catalogue = SpectralIndices(
        SpectralIndices={
            "ONE": make_index("ONE", {"source_link": shared_doi}),
            "TWO": make_index(
                "TWO",
                {
                    "source_link": shared_doi,
                    "source_metadata": {
                        "type": "report",
                        "title": "Contributor title",
                        "source": "contributor",
                    },
                },
            ),
            "THREE": make_index(
                "THREE", {"source_link": "https://example.com/source"}
            ),
        }
    )
    fetched_dois = []

    def fetcher(doi):
        fetched_dois.append(doi)
        return {
            "title": ["Shared publication"],
            "is-referenced-by-count": 7,
            "published": {"date-parts": [[2020]]},
            "type": "journal-article",
        }

    add_crossref_metadata(
        catalogue,
        fetcher=fetcher,
        today=date(2026, 8, 18),
        cache_path=tmp_path / "missing.json",
    )

    assert fetched_dois == ["10.1234/shared-doi"]
    assert catalogue.SpectralIndices["ONE"].source.source_metadata.type == "article"
    assert catalogue.SpectralIndices["TWO"].source.source_metadata.type == "article"
    assert (
        catalogue.SpectralIndices["TWO"].source.source_metadata.title
        == "Shared publication"
    )
    assert (
        catalogue.SpectralIndices["THREE"].source.source_metadata.model_dump(
            mode="json"
        )
        == {}
    )
    assert catalogue.SpectralIndices[
        "ONE"
    ].source.source_metadata.citations_metrics.model_dump(
        mode="json", exclude_none=True
    ) == {
        "citation_count": 7,
        "date": "2026-08-18",
    }

    references = add_reference_metadata(catalogue)
    one_citation = catalogue.SpectralIndices["ONE"].source.source_metadata.how_to_cite
    two_citation = catalogue.SpectralIndices["TWO"].source.source_metadata.how_to_cite
    assert one_citation.bibtex == two_citation.bibtex
    assert one_citation.bibtex in references
    assert one_citation.apa == two_citation.apa
    assert references[one_citation.bibtex].startswith("@article{")

    history_path = tmp_path / "citations.json"
    write_citation_history(catalogue, history_path)
    write_citation_history(catalogue, history_path)
    history = json.loads(history_path.read_text())
    assert history["ONE"] == [{"citation_count": 7, "date": "2026-08-18"}]
    assert history["TWO"] == [{"citation_count": 7, "date": "2026-08-18"}]
    assert history["THREE"] == []


def test_unavailable_crossref_record_preserves_contributed_metadata(tmp_path):
    index = SpectralIndex(
        acronym="TEST",
        name="Test index",
        formula="N",
        source={
            "source_link": "https://doi.org/10.1234/unavailable",
            "source_metadata": {
                "title": "Contributor title",
                "source": "contributor",
            },
        },
        classification={"application_domain": "vegetation"},
        date_of_addition="2026-08-18",
        contributor="https://github.com/example",
    )
    catalogue = SpectralIndices(SpectralIndices={"TEST": index})

    add_crossref_metadata(
        catalogue,
        fetcher=lambda doi: None,
        today=date(2026, 8, 18),
        cache_path=tmp_path / "missing.json",
    )

    assert index.source.source_metadata.title == "Contributor title"
    assert index.source.source_metadata.source == "contributor"


def test_contributed_metadata_can_generate_a_shared_reference():
    source = {
        "source_link": "https://example.com/shared-report",
        "source_metadata": {
            "type": "report",
            "title": "A contributed report",
            "journal": "Example Institute",
            "authors": ["Ada Lovelace"],
            "year": 2024,
            "source": "contributor",
        },
    }

    def make_index(acronym):
        return SpectralIndex(
            acronym=acronym,
            name=f"{acronym} name",
            formula="N",
            source=source,
            classification={"application_domain": "vegetation"},
            date_of_addition="2026-08-18",
            contributor="https://github.com/example",
        )

    catalogue = SpectralIndices(
        SpectralIndices={
            "ONE": make_index("ONE"),
            "TWO": make_index("TWO"),
        }
    )

    references = add_reference_metadata(catalogue)
    one_metadata = catalogue.SpectralIndices["ONE"].source.source_metadata
    two_metadata = catalogue.SpectralIndices["TWO"].source.source_metadata

    assert one_metadata.source == "contributor"
    assert one_metadata.how_to_cite.bibtex == two_metadata.how_to_cite.bibtex
    assert one_metadata.how_to_cite.bibtex in references
    assert references[one_metadata.how_to_cite.bibtex].startswith("@techreport{")


def test_extract_doi_normalizes_resolver_urls():
    assert (
        extract_doi("https://doi.org/10.1234/Example%2FPart")
        == "10.1234/example/part"
    )
    assert extract_doi("https://example.com/10.1234/example") is None


def test_reference_formatters_use_normalized_metadata():
    metadata = {
        "type": "article",
        "title": "A useful index",
        "journal": "Remote Sensing & Applications",
        "volume": "4",
        "issue": "2",
        "authors": ["Ada Lovelace", "Grace Hopper"],
        "year": 2024,
    }
    source_link = "https://doi.org/10.1234/example"

    apa = format_apa_citation(metadata, source_link)
    bibtex = format_bibtex_entry("ASI_TEST", metadata, source_link)

    assert apa == (
        "Ada Lovelace, & Grace Hopper (2024). A useful index. "
        "Remote Sensing & Applications, 4(2). https://doi.org/10.1234/example"
    )
    assert "@article{ASI_TEST," in bibtex
    assert "Ada Lovelace and Grace Hopper" in bibtex
    assert r"Remote Sensing \& Applications" in bibtex


def test_source_status_generation_checks_each_unique_link_once():
    catalogue = spindex.model_copy(deep=True)
    checked_links = []

    def checker(source_link):
        checked_links.append(source_link)
        return "operational"

    add_source_metadata(catalogue, checker=checker)

    unique_links = {
        index.source.source_link for index in catalogue.SpectralIndices.values()
    }
    assert set(checked_links) == unique_links
    assert len(checked_links) == len(unique_links)
    assert all(
        index.source.source_link_status == "operational"
        for index in catalogue.SpectralIndices.values()
    )


def test_source_companions_include_every_other_key_with_the_same_link():
    catalogue = spindex.model_copy(deep=True)

    add_source_companions(catalogue)

    for key, index in catalogue.SpectralIndices.items():
        expected = [
            other_key
            for other_key, other_index in catalogue.SpectralIndices.items()
            if other_key != key
            and other_index.source.source_link == index.source.source_link
        ]
        assert index.source.source_companions == expected

    assert catalogue.SpectralIndices["GARI"].source.source_companions == [
        "GNDVI",
        "GRARI",
    ]

import pytest
from pydantic import ValidationError

from src.v1.SpectralIndex import Source
from src.v1.indices import spindex
from src.v1.main_v1 import add_source_metadata


def test_source_link_type_is_generated_from_the_url():
    assert (
        Source(source_link="https://doi.org/10.1234/example").source_link_type == "doi"
    )
    assert (
        Source(source_link="http://dx.doi.org/10.1234/example").source_link_type
        == "doi"
    )
    assert Source(source_link="https://example.com/paper").source_link_type == "other"


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
    source = Source(source_link="https://example.com/source", source_type=source_type)
    assert source.source_type == source_type


def test_source_type_rejects_unsupported_values():
    with pytest.raises(ValidationError):
        Source(source_link="https://example.com/source", source_type="website")


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

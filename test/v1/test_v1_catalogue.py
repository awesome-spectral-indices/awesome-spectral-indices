from datetime import date
from urllib.parse import urlparse

from src.v1.SpectralIndex import parse_formula_variables
from src.v1.constants import constants
from src.v1.indices import spindex
from src.v1.utils import Bands, Constants, IndexType


REQUIRED_TEXT_FIELDS = (
    "acronym",
    "name",
    "formula",
    "application_domain",
    "contributor",
)

SOURCE_TYPES = {
    "article",
    "book",
    "book_chapter",
    "conference_paper",
    "poster",
    "report",
    "preprint",
}


def test_required_catalogue_metadata_is_present_and_well_formed():
    for index in spindex.SpectralIndices.values():
        for field in REQUIRED_TEXT_FIELDS:
            value = getattr(index, field)
            assert isinstance(value, str)
            assert value.strip(), f"{index.acronym}.{field} is empty"

        source_link = urlparse(index.source.source_link)
        assert source_link.scheme in {"http", "https"}
        assert source_link.netloc
        assert index.source.source_link_type in {"doi", "other"}
        assert (
            index.source.source_type is None or index.source.source_type in SOURCE_TYPES
        )
        assert isinstance(index.date_of_addition, date)


def test_acronym_and_name_are_required_v1_fields():
    fields = type(next(iter(spindex.SpectralIndices.values()))).model_fields

    assert fields["acronym"].is_required()
    assert fields["name"].is_required()
    assert fields["source"].is_required()
    assert not fields["bands"].is_required()
    assert not fields["constants"].is_required()
    assert "short_name" not in fields
    assert "long_name" not in fields
    assert "reference" not in fields

    source_fields = next(iter(spindex.SpectralIndices.values())).source.model_fields
    assert source_fields["source_link"].is_required()
    assert not source_fields["source_type"].is_required()


def test_ndvi_and_tvi_are_conference_papers():
    assert spindex.SpectralIndices["NDVI"].source.source_type == "conference_paper"
    assert spindex.SpectralIndices["TVI"].source.source_type == "conference_paper"


def test_evi_is_an_article():
    assert spindex.SpectralIndices["EVI"].source.source_type == "article"


def test_catalogue_domains_and_formula_variables_are_supported():
    supported_domains = set(IndexType._value2member_map_)
    supported_variables = {
        *Bands._value2member_map_,
        *Constants._value2member_map_,
    }

    for index in spindex.SpectralIndices.values():
        assert index.application_domain in supported_domains
        assert set(parse_formula_variables(index.formula)) <= supported_variables


def test_bands_and_constants_are_separate_registries():
    band_names = set(Bands._value2member_map_)
    constant_names = set(Constants._value2member_map_)

    assert band_names.isdisjoint(constant_names)
    assert constant_names == set(constants)

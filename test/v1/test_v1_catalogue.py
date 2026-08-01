from datetime import date
from urllib.parse import urlparse

from src.v1.SpectralIndex import parse_formula_variables
from src.v1.indices import spindex
from src.v1.utils import Bands, IndexType


REQUIRED_TEXT_FIELDS = (
    "acronym",
    "name",
    "formula",
    "reference",
    "application_domain",
    "contributor",
)


def test_required_catalogue_metadata_is_present_and_well_formed():
    for index in spindex.SpectralIndices.values():
        for field in REQUIRED_TEXT_FIELDS:
            value = getattr(index, field)
            assert isinstance(value, str)
            assert value.strip(), f"{index.acronym}.{field} is empty"

        reference = urlparse(index.reference)
        assert reference.scheme in {"http", "https"}
        assert reference.netloc
        assert isinstance(index.date_of_addition, date)


def test_acronym_and_name_are_required_v1_fields():
    fields = type(next(iter(spindex.SpectralIndices.values()))).model_fields

    assert fields["acronym"].is_required()
    assert fields["name"].is_required()
    assert "short_name" not in fields
    assert "long_name" not in fields


def test_catalogue_domains_and_formula_variables_are_supported():
    supported_domains = set(IndexType._value2member_map_)
    supported_variables = set(Bands._value2member_map_)

    for index in spindex.SpectralIndices.values():
        assert index.application_domain in supported_domains
        assert set(parse_formula_variables(index.formula)) <= supported_variables

from datetime import date
from urllib.parse import urlparse

import pytest
from pydantic import ValidationError

from src.v1.SpectralIndex import (
    Classification,
    ConstantDefinition,
    ExternalVariableDefinition,
    ReductionDefinition,
    SpectralIndex,
    parse_formula_reduction_dimensions,
    parse_formula_variables,
)
from src.v1.indices import spindex
from src.v1.utils import (
    ApplicationDomain,
    Bands,
    Constants,
    External,
    IndexFamily,
    Polarizations,
    SensingModality,
)


REQUIRED_TEXT_FIELDS = (
    "acronym",
    "name",
    "formula",
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

        assert index.classification.application_domain
        assert index.classification.sensing_modalities is None

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
    assert fields["classification"].is_required()
    assert not fields["bands"].is_required()
    assert not fields["polarizations"].is_required()
    assert not fields["constants"].is_required()
    assert not fields["external_variables"].is_required()
    assert not fields["reductions"].is_required()
    assert "short_name" not in fields
    assert "long_name" not in fields
    assert "reference" not in fields
    assert "application_domain" not in fields

    source_fields = next(iter(spindex.SpectralIndices.values())).source.model_fields
    assert source_fields["source_link"].is_required()
    assert not source_fields["source_type"].is_required()


def test_ndvi_and_tvi_are_conference_papers():
    assert spindex.SpectralIndices["NDVI"].source.source_type == "conference_paper"
    assert spindex.SpectralIndices["TVI"].source.source_type == "conference_paper"


def test_evi_and_savi_are_articles():
    assert spindex.SpectralIndices["EVI"].source.source_type == "article"
    assert spindex.SpectralIndices["SAVI"].source.source_type == "article"


def test_catalogue_domains_and_formula_variables_are_supported():
    supported_domains = set(ApplicationDomain._value2member_map_)
    supported_variables = {
        *Bands._value2member_map_,
        *Polarizations._value2member_map_,
        *Constants._value2member_map_,
        *External._value2member_map_,
    }

    for index in spindex.SpectralIndices.values():
        assert index.classification.application_domain in supported_domains
        assert set(parse_formula_variables(index.formula)) <= supported_variables


def test_formula_variable_registries_are_disjoint():
    band_names = set(Bands._value2member_map_)
    constant_names = set(Constants._value2member_map_)
    external_names = set(External._value2member_map_)
    polarization_names = set(Polarizations._value2member_map_)

    assert band_names.isdisjoint(constant_names)
    assert band_names.isdisjoint(external_names)
    assert band_names.isdisjoint(polarization_names)
    assert constant_names.isdisjoint(external_names)
    assert constant_names.isdisjoint(polarization_names)
    assert external_names.isdisjoint(polarization_names)


def test_classification_vocabularies_and_authored_assignments():
    assert set(ApplicationDomain._value2member_map_) == {
        "vegetation",
        "water",
        "burn",
        "snow",
        "soil",
        "urban",
        "geology",
        "clouds",
    }
    assert set(SensingModality._value2member_map_) == {
        "multispectral",
        "thermal",
        "radar",
    }
    assert set(IndexFamily._value2member_map_) == {
        "kernel",
        "tasseled_cap",
        "radar",
    }

    kernel_keys = {"kEVI", "kNDVI", "kRVI", "kVARI", "kIPVI"}
    radar_keys = {
        key
        for key, index in spindex.SpectralIndices.items()
        if set(parse_formula_variables(index.formula))
        & set(Polarizations._value2member_map_)
    }

    for key, index in spindex.SpectralIndices.items():
        expected_family = (
            ["kernel"] if key in kernel_keys else ["radar"] if key in radar_keys else None
        )
        assert index.classification.family == expected_family

    assert spindex.SpectralIndices["NDPolI"].classification.application_domain == (
        "geology"
    )
    assert all(
        spindex.SpectralIndices[key].classification.application_domain == "vegetation"
        for key in radar_keys - {"NDPolI"}
    )
    assert all(
        spindex.SpectralIndices[key].classification.application_domain == "vegetation"
        for key in kernel_keys
    )


def test_classification_rejects_invalid_or_duplicate_values():
    assert Classification(application_domain="geology").family is None

    with pytest.raises(ValidationError):
        Classification(application_domain="radar")
    with pytest.raises(ValidationError):
        Classification(application_domain="vegetation", family=[])
    with pytest.raises(ValidationError):
        Classification(
            application_domain="vegetation", family=["kernel", "kernel"]
        )
    with pytest.raises(ValidationError):
        Classification(application_domain="vegetation", family=["ratio"])


def test_kernel_results_are_functions_not_registered_band_operands():
    legacy_kernel_operands = {
        "kNN",
        "kNR",
        "kNB",
        "kNL",
        "kGG",
        "kGR",
        "kGB",
        "kBB",
        "kBR",
        "kBL",
        "kRR",
        "kRB",
        "kRL",
        "kLL",
    }

    assert legacy_kernel_operands.isdisjoint(Bands._value2member_map_)
    for key in ("kEVI", "kNDVI", "kRVI", "kVARI", "kIPVI"):
        index = spindex.SpectralIndices[key]
        assert "kernel(" in index.formula
        assert legacy_kernel_operands.isdisjoint(
            parse_formula_variables(index.formula)
        )


def test_catalogue_defines_exactly_the_constants_and_externals_in_each_formula():
    constant_names = set(Constants._value2member_map_)
    external_names = set(External._value2member_map_)

    for index in spindex.SpectralIndices.values():
        expected_constants = {
            variable
            for variable in parse_formula_variables(index.formula)
            if variable in constant_names
        }
        expected_externals = {
            variable
            for variable in parse_formula_variables(index.formula)
            if variable in external_names
        }
        assert set(index.constants or {}) == expected_constants
        assert set(index.external_variables or {}) == expected_externals


def _index_with(
    formula, constants=None, external_variables=None, reductions=None
):
    values = {
        "acronym": "TEST",
        "name": "Test Index",
        "formula": formula,
        "source": {"source_link": "https://example.com/source"},
        "classification": {"application_domain": "vegetation"},
        "date_of_addition": "2026-08-03",
        "contributor": "https://github.com/example",
    }
    if constants is not None:
        values["constants"] = constants
    if external_variables is not None:
        values["external_variables"] = external_variables
    if reductions is not None:
        values["reductions"] = reductions
    return SpectralIndex(**values)


def test_constants_are_optional_when_formula_has_none():
    index = _index_with("(N - R) / (N + R)")

    assert index.constants is None
    assert index.external_variables is None


def test_formula_constants_require_matching_contributor_definitions():
    with pytest.raises(ValidationError, match="missing: L"):
        _index_with("(1 + L) * N")

    with pytest.raises(ValidationError, match="not used by formula: C1"):
        _index_with(
            "(1 + L) * N",
            {
                "L": {"description": "Adjustment", "default_value": 1},
                "C1": {"description": "Unused coefficient"},
            },
        )


def test_constant_definition_requires_description_and_strict_numeric_default():
    assert ConstantDefinition(description="Anything").default_value is None
    assert (
        ConstantDefinition(description="Anything", default_value=1).default_value == 1
    )
    assert (
        ConstantDefinition(description="Anything", default_value=1.5).default_value
        == 1.5
    )

    with pytest.raises(ValidationError):
        ConstantDefinition(default_value=1)
    with pytest.raises(ValidationError):
        ConstantDefinition(description=123)
    with pytest.raises(ValidationError):
        ConstantDefinition(description="Anything", default_value="1.0")
    with pytest.raises(ValidationError):
        ConstantDefinition(description="Anything", default_value=True)


def test_constant_definition_accepts_suggested_values_and_ranges():
    definition = ConstantDefinition(
        description="Adjustment",
        suggested_values={
            "Low density": 1,
            "Intermediate density": 0.5,
            "Published interval": [0.25, 1.0],
        },
        suggested_range=[0.25, 1],
    )

    assert definition.suggested_values == {
        "Low density": 1,
        "Intermediate density": 0.5,
        "Published interval": [0.25, 1.0],
    }
    assert definition.suggested_range == [0.25, 1]


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("suggested_range", [0.25]),
        ("suggested_range", [0.25, 0.5, 1]),
        ("suggested_range", ["0.25", 1]),
        ("suggested_range", [False, 1]),
        ("suggested_values", {"Condition": [0.25]}),
        ("suggested_values", {"Condition": [0.25, 0.5, 1]}),
        ("suggested_values", {"Condition": "0.5"}),
        ("suggested_values", {"Condition": True}),
        ("suggested_values", {1: 0.5}),
    ],
)
def test_constant_definition_rejects_invalid_suggestions(field, value):
    with pytest.raises(ValidationError):
        ConstantDefinition(description="Adjustment", **{field: value})


def test_formula_externals_require_matching_contributor_definitions():
    with pytest.raises(ValidationError, match="missing: PAR"):
        _index_with("N * PAR")

    with pytest.raises(ValidationError, match="not used by formula: PAR"):
        _index_with(
            "N / R",
            external_variables={"PAR": {"description": "Incoming radiation"}},
        )


def test_external_variable_definition_only_accepts_a_strict_description():
    definition = ExternalVariableDefinition(description="Incoming radiation")
    assert definition.model_dump() == {"description": "Incoming radiation"}

    with pytest.raises(ValidationError):
        ExternalVariableDefinition()
    with pytest.raises(ValidationError):
        ExternalVariableDefinition(description=123)

    for unsupported_property in (
        "default_value",
        "suggested_values",
        "suggested_range",
    ):
        with pytest.raises(ValidationError):
            ExternalVariableDefinition(
                description="Incoming radiation",
                **{unsupported_property: 1},
            )


def test_spatial_reductions_require_matching_context_definitions():
    index = _index_with(
        "spatial_max(S2) / spatial_mean(B)",
        reductions={"space": {"scope": "aoi"}},
    )

    assert parse_formula_reduction_dimensions(index.formula) == ["space"]
    assert index.reductions["space"].scope == "aoi"

    with pytest.raises(ValidationError, match="missing: space"):
        _index_with("spatial_min(N)")

    with pytest.raises(ValidationError, match="not used by formula: space"):
        _index_with("N / R", reductions={"space": {"scope": "scene"}})


@pytest.mark.parametrize("scope", ["aoi", "scene"])
def test_spatial_reductions_accept_supported_scopes(scope):
    definition = ReductionDefinition(scope=scope)
    assert definition.scope == scope


def test_spatial_reductions_reject_unsupported_scopes_and_properties():
    with pytest.raises(ValidationError):
        ReductionDefinition(scope="tile")
    with pytest.raises(ValidationError):
        ReductionDefinition(scope="aoi", radius=3)
    with pytest.raises(ValidationError):
        _index_with(
            "spatial_max(N)",
            reductions={"time": {"scope": "scene"}},
        )


def test_nirvp_defines_par_as_an_external_variable():
    nirvp = spindex.SpectralIndices["NIRvP"]

    assert nirvp.constants is None
    assert nirvp.external_variables["PAR"].model_dump() == {
        "description": "Photosynthetically Active Radiation"
    }


def test_wci3_uses_nested_max_and_tanh_functions():
    wci3 = spindex.SpectralIndices["WCI3"]

    assert wci3.formula == (
        "((B - R)/(B + R + epsilon)) * tanh(R - max(B, G, RE1, N))"
    )
    assert parse_formula_variables(wci3.formula) == [
        "B",
        "R",
        "epsilon",
        "G",
        "RE1",
        "N",
    ]
    assert wci3.constants["epsilon"].model_dump() == {
        "description": "Adjustment constant for numerical stability",
        "default_value": 1e-10,
    }


def test_cwi_uses_aoi_scoped_spatial_maximum_reductions():
    cwi = spindex.SpectralIndices["CWI"]

    assert cwi.formula == (
        "(spatial_max(S2) * B) / (spatial_max(B) * S2)"
    )
    assert parse_formula_variables(cwi.formula) == ["S2", "B"]
    assert parse_formula_reduction_dimensions(cwi.formula) == ["space"]
    assert cwi.reductions["space"].model_dump() == {"scope": "aoi"}


def test_kndvi_uses_explicit_two_input_kernel_calls():
    kndvi = spindex.SpectralIndices["kNDVI"]

    assert kndvi.formula == (
        "(kernel(N, N) - kernel(N, R)) / "
        "(kernel(N, N) + kernel(N, R))"
    )
    assert parse_formula_variables(kndvi.formula) == ["N", "R"]


def test_kevi_exposes_its_kernel_inputs_and_background_constant():
    kevi = spindex.SpectralIndices["kEVI"]

    assert parse_formula_variables(kevi.formula) == [
        "g",
        "N",
        "R",
        "C1",
        "C2",
        "B",
        "L",
    ]
    assert kevi.constants["L"].model_dump() == {
        "description": "Canopy background adjustment",
        "default_value": 1.0,
    }

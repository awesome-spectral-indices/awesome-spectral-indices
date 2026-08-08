import csv
import json
from collections import Counter
from pathlib import Path

from src.v1.SpectralIndex import parse_formula_variables
from src.v1.indices import spindex
from src.v1.utils import Bands, Constants, External, Hyperspectral, Polarizations


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "output/v1"


def _source_acronyms():
    return Counter(index.acronym for index in spindex.SpectralIndices.values())


def test_v1_source_catalogue_and_outputs_contain_the_same_indices():
    expected = _source_acronyms()

    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]
    json_acronyms = Counter(item["acronym"] for item in json_catalogue.values())

    with (OUTPUT_DIR / "spectral-indices-table.csv").open(newline="") as fp:
        csv_reader = csv.DictReader(fp)
        assert "external_variables" in csv_reader.fieldnames
        assert "classification" in csv_reader.fieldnames
        assert "polarizations" in csv_reader.fieldnames
        assert "reductions" in csv_reader.fieldnames
        assert "application_domain" not in csv_reader.fieldnames
        csv_acronyms = Counter(row["acronym"] for row in csv_reader)

    assert json_acronyms == expected
    assert csv_acronyms == expected


def test_v1_indices_do_not_define_or_serialize_platforms():
    for index in spindex.SpectralIndices.values():
        assert "platforms" not in type(index).model_fields

    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    for index in json_catalogue.values():
        assert "platforms" not in index


def test_v1_outputs_contain_generated_source_metadata():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    for index in json_catalogue.values():
        assert "reference" not in index
        assert set(index["source"]) == {
            "source_companions",
            "source_link",
            "source_link_status",
            "source_link_type",
            "source_type",
        }
        assert index["source"]["source_link_status"] in {"operational", "down"}
        assert index["source"]["source_link_type"] in {"doi", "other"}

    for key, index in json_catalogue.items():
        companions = index["source"]["source_companions"]
        assert key not in companions
        assert len(companions) == len(set(companions))
        assert companions == [
            other_key
            for other_key, other_index in spindex.SpectralIndices.items()
            if other_key != key
            and other_index.source.source_link == index["source"]["source_link"]
        ]

    assert json_catalogue["GARI"]["source"]["source_companions"] == [
        "GNDVI",
        "GRARI",
    ]

    assert json_catalogue["EVI"]["source"]["source_type"] == "article"
    assert json_catalogue["SAVI"]["source"]["source_type"] == "article"
    assert json_catalogue["NDVI"]["source"]["source_type"] == "conference_paper"
    assert json_catalogue["TVI"]["source"]["source_type"] == "conference_paper"


def test_v1_outputs_separate_formula_input_types():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    band_names = set(Bands._value2member_map_)
    polarization_names = set(Polarizations._value2member_map_)
    external_names = set(External._value2member_map_)

    for key, source_index in spindex.SpectralIndices.items():
        variables = parse_formula_variables(source_index.formula)
        expected_bands = [
            variable
            for variable in variables
            if variable in band_names or Hyperspectral.is_band(variable)
        ]
        expected_polarizations = [
            variable for variable in variables if variable in polarization_names
        ]
        expected_constants = {
            name: definition.model_dump(mode="json")
            for name, definition in (source_index.constants or {}).items()
        }
        expected_externals = {
            name: definition.model_dump(mode="json")
            for name, definition in (source_index.external_variables or {}).items()
        }
        expected_reductions = {
            name: definition.model_dump(mode="json")
            for name, definition in (source_index.reductions or {}).items()
        }
        expected_external_names = {
            variable for variable in variables if variable in external_names
        }

        assert json_catalogue[key]["bands"] == expected_bands
        assert json_catalogue[key]["polarizations"] == expected_polarizations
        assert json_catalogue[key]["constants"] == expected_constants
        assert json_catalogue[key]["external_variables"] == expected_externals
        assert json_catalogue[key]["reductions"] == expected_reductions
        assert set(expected_externals) == expected_external_names

        serialized_variables = (
            set(json_catalogue[key]["bands"])
            | set(json_catalogue[key]["polarizations"])
            | set(json_catalogue[key]["constants"])
            | set(json_catalogue[key]["external_variables"])
        )
        assert serialized_variables == set(variables)


def test_v1_outputs_generate_classification_and_sensing_modalities():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    for index in json_catalogue.values():
        assert "application_domain" not in index
        assert set(index["classification"]) == {
            "application_domain",
            "sensing_modalities",
            "family",
        }
        assert index["classification"]["sensing_modalities"]

    assert json_catalogue["NDVI"]["classification"] == {
        "application_domain": "vegetation",
        "sensing_modalities": ["multispectral"],
        "family": None,
    }
    assert json_catalogue["NBRT1"]["classification"]["sensing_modalities"] == [
        "multispectral",
        "thermal",
    ]
    assert json_catalogue["kNDVI"]["classification"] == {
        "application_domain": "vegetation",
        "sensing_modalities": ["multispectral"],
        "family": ["kernel"],
    }
    assert json_catalogue["TMTCbrightness"]["classification"] == {
        "application_domain": "vegetation",
        "sensing_modalities": ["multispectral"],
        "family": ["tasseled_cap"],
    }
    assert json_catalogue["NDPolI"]["classification"] == {
        "application_domain": "geology",
        "sensing_modalities": ["radar"],
        "family": ["radar"],
    }
    assert json_catalogue["NDPolI"]["bands"] == []
    assert json_catalogue["NDPolI"]["polarizations"] == ["VV", "VH"]
    assert json_catalogue["CARI"]["classification"] == {
        "application_domain": "vegetation",
        "sensing_modalities": ["hyperspectral"],
        "family": None,
    }
    assert json_catalogue["CARI"]["bands"] == ["R720", "R521"]
    assert json_catalogue["CARI"]["polarizations"] == []

    hyperspectral_keys = {
        key
        for key, source_index in spindex.SpectralIndices.items()
        if any(
            Hyperspectral.is_band(variable)
            for variable in parse_formula_variables(source_index.formula)
        )
    }
    for key in hyperspectral_keys:
        assert "hyperspectral" in json_catalogue[key]["classification"][
            "sensing_modalities"
        ]
        assert any(
            Hyperspectral.is_band(band) for band in json_catalogue[key]["bands"]
        )


def test_v1_outputs_include_cwi_spatial_reduction_context():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    assert json_catalogue["CWI"]["bands"] == ["S2", "B"]
    assert json_catalogue["CWI"]["reductions"] == {
        "space": {"scope": "aoi"}
    }
    assert all(
        index["reductions"] == {}
        for key, index in json_catalogue.items()
        if key != "CWI"
    )


def test_v1_outputs_generate_physical_bands_for_kernel_indices():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    assert json_catalogue["kNDVI"]["bands"] == ["N", "R"]
    assert json_catalogue["kEVI"]["bands"] == ["N", "R", "B"]
    assert json_catalogue["kVARI"]["bands"] == ["G", "R", "B"]
    assert json_catalogue["kEVI"]["constants"]["L"] == {
        "description": "Canopy background adjustment",
        "default_value": 1.0,
    }


def test_v1_constants_metadata_is_grouped_by_constant_and_index():
    with (OUTPUT_DIR / "constants.json").open() as fp:
        generated_constants = json.load(fp)

    assert set(generated_constants) == set(Constants._value2member_map_)

    for constant_name, index_definitions in generated_constants.items():
        for key, definition in index_definitions.items():
            expected = spindex.SpectralIndices[key].constants[constant_name]
            assert definition == expected.model_dump(mode="json")
            assert "description" in definition
            assert set(definition) <= {
                "description",
                "default_value",
                "suggested_values",
                "suggested_range",
            }

    assert generated_constants["L"]["EVI"] == {
        "description": "Canopy background adjustment",
        "default_value": 1.0,
    }
    assert "short_name" not in generated_constants["L"]
    assert generated_constants["L"]["SAVI"] == {
        "description": "Canopy background adjustment",
        "default_value": 0.5,
        "suggested_values": {
            "Low vegetation densities": 1.0,
            "Intermediate vegetation densities": 0.5,
            "High vegetation densities": 0.25,
        },
        "suggested_range": [0.25, 1],
    }


def test_v1_external_metadata_is_grouped_by_variable_and_index():
    with (OUTPUT_DIR / "external_variables.json").open() as fp:
        generated_externals = json.load(fp)

    assert set(generated_externals) == set(External._value2member_map_)

    for external_name, index_definitions in generated_externals.items():
        for key, definition in index_definitions.items():
            expected = spindex.SpectralIndices[key].external_variables[external_name]
            assert definition == expected.model_dump(mode="json")
            assert set(definition) == {"description"}

    assert generated_externals["PAR"]["NIRvP"] == {
        "description": "Photosynthetically Active Radiation"
    }

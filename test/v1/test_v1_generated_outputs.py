import csv
import json
import re
from collections import Counter
from pathlib import Path

from src.v1.SpectralIndex import parse_formula_variables
from src.v1.indices import spindex
from src.v1.utils import (
    Bands,
    External,
    Polarizations,
    is_hyperspectral_band,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "output/v1"


def test_v1_json_and_csv_outputs_contain_the_same_indices():
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

    assert csv_acronyms == json_acronyms


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

    citation_snapshots_by_source = {}
    for key, index in json_catalogue.items():
        assert "reference" not in index
        assert set(index["source"]) == {
            "source_companions",
            "source_link",
            "source_link_semantic_scholar",
            "source_link_status",
            "source_link_type",
            "source_metadata",
        }
        assert index["source"]["source_link_status"] in {"operational", "down"}
        assert index["source"]["source_link_type"] in {"doi", "other"}
        assert isinstance(index["source"]["source_metadata"], dict)
        assert "source_type" not in index["source"]
        metadata = index["source"]["source_metadata"]
        if metadata:
            assert metadata["source"] in {
                "contributor",
                "crossref",
                "semantic_scholar",
                "other",
            }

        metrics = metadata.get("citations_metrics")
        if metrics:
            snapshot = (metrics["citation_count"], metrics["date"])
            source_link = index["source"]["source_link"]
            previous = citation_snapshots_by_source.setdefault(
                source_link, snapshot
            )
            assert snapshot == previous

    for key, index in json_catalogue.items():
        companions = index["source"]["source_companions"]
        assert key not in companions
        assert len(companions) == len(set(companions))
        assert set(companions) == {
            other_key
            for other_key, other_index in json_catalogue.items()
            if other_key != key
            and other_index["source"]["source_link"]
            == index["source"]["source_link"]
        }


def test_v1_bibtex_references_are_shared_by_source():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]
    bibtex = (OUTPUT_DIR / "spectral-indices-references.bib").read_text()
    bibtex_keys = set(re.findall(r"^@\w+\{([^,]+),", bibtex, flags=re.MULTILINE))

    used_keys = set()
    citation_keys_by_source = {}
    for index in json_catalogue.values():
        citation = index["source"]["source_metadata"].get("how_to_cite")
        if citation:
            assert set(citation) == {"apa", "bibtex"}
            assert citation["apa"].strip()
            assert citation["bibtex"] in bibtex_keys
            used_keys.add(citation["bibtex"])
            source_link = index["source"]["source_link"]
            previous = citation_keys_by_source.setdefault(
                source_link, citation["bibtex"]
            )
            assert citation["bibtex"] == previous

    assert used_keys == bibtex_keys


def test_v1_citation_history_matches_latest_catalogue_snapshots():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]
    with (OUTPUT_DIR / "spectral-indices-citations.json").open() as fp:
        citation_history = json.load(fp)

    assert set(citation_history) == set(json_catalogue)
    for key, snapshots in citation_history.items():
        assert isinstance(snapshots, list)
        assert snapshots == sorted(snapshots, key=lambda item: item["date"])
        assert len({snapshot["date"] for snapshot in snapshots}) == len(snapshots)
        for snapshot in snapshots:
            assert set(snapshot) == {"citation_count", "date"}
            assert isinstance(snapshot["citation_count"], int)
            assert snapshot["citation_count"] >= 0

        current = json_catalogue[key]["source"]["source_metadata"].get(
            "citations_metrics"
        )
        if current:
            assert snapshots[-1] == {
                "citation_count": current["citation_count"],
                "date": current["date"],
            }


def test_v1_citation_metrics_have_generated_comparison_statistics():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    cited_indices = {
        key: index
        for key, index in json_catalogue.items()
        if "citations_metrics" in index["source"]["source_metadata"]
    }
    assert cited_indices

    for index in cited_indices.values():
        metrics = index["source"]["source_metadata"]["citations_metrics"]
        assert set(metrics) == {
            "citation_count",
            "date",
            "overall",
            "within_application_domain",
        }
        for comparison in ("overall", "within_application_domain"):
            values = metrics[comparison]
            assert set(values) == {
                "percentile",
                "percentile_similar_age",
                "rank",
                "rank_similar_age",
                "similar_age_count",
            }
            assert values["rank"] >= 1
            assert 0 <= values["percentile"] <= 100
            assert values["similar_age_count"] >= 0


def test_v1_outputs_separate_formula_input_types():
    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]

    band_names = set(Bands._value2member_map_)
    polarization_names = set(Polarizations._value2member_map_)
    external_names = set(External._value2member_map_)

    for index in json_catalogue.values():
        variables = parse_formula_variables(index["formula"])
        expected_bands = [
            variable
            for variable in variables
            if variable in band_names or is_hyperspectral_band(variable)
        ]
        expected_polarizations = [
            variable for variable in variables if variable in polarization_names
        ]
        expected_external_names = {
            variable for variable in variables if variable in external_names
        }

        assert index["bands"] == expected_bands
        assert index["polarizations"] == expected_polarizations
        assert set(index["external_variables"]) == expected_external_names

        serialized_variables = (
            set(index["bands"])
            | set(index["polarizations"])
            | set(index["constants"])
            | set(index["external_variables"])
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
    assert json_catalogue["NDISI"]["classification"] == {
        "application_domain": "snow",
        "sensing_modalities": ["hyperspectral"],
        "family": None,
    }
    assert json_catalogue["NDISI"]["bands"] == [
        "R1080_1120",
        "R1760_1800",
    ]

    hyperspectral_indices = [
        index
        for index in json_catalogue.values()
        if any(
            is_hyperspectral_band(variable)
            for variable in parse_formula_variables(index["formula"])
        )
    ]
    for index in hyperspectral_indices:
        assert "hyperspectral" in index["classification"]["sensing_modalities"]
        assert any(is_hyperspectral_band(band) for band in index["bands"])


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

    for index_definitions in generated_constants.values():
        for definition in index_definitions.values():
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

    for index_definitions in generated_externals.values():
        for definition in index_definitions.values():
            assert set(definition) == {"description"}

    assert generated_externals["PAR"]["NIRvP"] == {
        "description": "Photosynthetically Active Radiation"
    }

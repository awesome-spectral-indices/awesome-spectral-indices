import csv
import json
from collections import Counter
from pathlib import Path

from src.v1.indices import spindex


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
        csv_acronyms = Counter(row["acronym"] for row in csv.DictReader(fp))

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
            "source_link",
            "source_link_status",
            "source_link_type",
            "source_type",
        }
        assert index["source"]["source_link_status"] in {"operational", "down"}
        assert index["source"]["source_link_type"] in {"doi", "other"}

    assert json_catalogue["EVI"]["source"]["source_type"] == "article"
    assert json_catalogue["NDVI"]["source"]["source_type"] == "conference_paper"
    assert json_catalogue["TVI"]["source"]["source_type"] == "conference_paper"

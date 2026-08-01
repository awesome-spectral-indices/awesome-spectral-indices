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

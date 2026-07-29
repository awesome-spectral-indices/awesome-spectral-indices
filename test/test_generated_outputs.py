import csv
import json
from collections import Counter
from pathlib import Path

from src.indices import spindex


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "output"


def _source_short_names():
    return Counter(
        index.short_name for index in spindex.SpectralIndices.values()
    )


def test_source_catalogue_and_public_outputs_contain_the_same_indices():
    expected = _source_short_names()

    with (OUTPUT_DIR / "spectral-indices-dict.json").open() as fp:
        json_catalogue = json.load(fp)["SpectralIndices"]
    json_names = Counter(item["short_name"] for item in json_catalogue.values())

    with (OUTPUT_DIR / "spectral-indices-table.csv").open(newline="") as fp:
        csv_names = Counter(row["short_name"] for row in csv.DictReader(fp))

    assert json_names == expected
    assert csv_names == expected

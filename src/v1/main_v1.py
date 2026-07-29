"""Build the Awesome Spectral Indices v1 catalogue outputs."""

import json
from pathlib import Path

import pandas as pd

from src.v1.SpectralIndex import parse_formula_variables
from src.v1.bands import bands
from src.v1.constants import constants
from src.v1.indices import spindex


REPO_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = REPO_ROOT / "output/v1"
SPECTRAL_INDICES_JSON = OUTPUT_DIR / "spectral-indices-dict.json"
SPECTRAL_INDICES_TABLE = OUTPUT_DIR / "spectral-indices-table.csv"

TABLE_COLUMNS = [
    "short_name",
    "long_name",
    "application_domain",
    "formula",
    "bands",
    "reference",
    "contributor",
    "date_of_addition",
]

def add_formula_metadata(index_catalog):
    """Populate each spectral index with its parsed formula variables."""
    for key, spectral_index in index_catalog.SpectralIndices.items():
        spectral_index.bands = parse_formula_variables(spectral_index.formula)
        index_catalog.SpectralIndices[key] = spectral_index

    return index_catalog


def write_json_outputs(index_catalog):
    """Write the v1 catalogue, band metadata, and constants metadata as JSON."""
    with SPECTRAL_INDICES_JSON.open("w") as fp:
        json.dump(
            index_catalog.model_dump(mode="json"),
            fp,
            indent=4,
            sort_keys=True,
        )

    with (OUTPUT_DIR / "bands.json").open("w") as fp:
        json.dump(bands, fp, indent=4, sort_keys=True)

    with (OUTPUT_DIR / "constants.json").open("w") as fp:
        json.dump(constants, fp, indent=4, sort_keys=True)


def build_indices_dataframe(path=SPECTRAL_INDICES_JSON):
    """Build the public v1 CSV dataframe from the generated catalogue JSON."""
    with path.open() as fp:
        indices = json.load(fp)

    df = pd.DataFrame(list(indices["SpectralIndices"].values()))
    return df[TABLE_COLUMNS]


def write_spectral_indices_table(df):
    """Write the flat v1 CSV table used as a machine-readable output."""
    df.to_csv(SPECTRAL_INDICES_TABLE, index=False)


def main():
    """Generate all v1 catalogue JSON and CSV outputs."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    index_catalog = add_formula_metadata(spindex)
    write_json_outputs(index_catalog)

    df = build_indices_dataframe()
    write_spectral_indices_table(df)


if __name__ == "__main__":
    main()

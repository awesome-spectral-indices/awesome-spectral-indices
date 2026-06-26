"""Build the Awesome Spectral Indices catalogue outputs."""

import json
from pathlib import Path

import pandas as pd

from src.SpectralIndex import parse_formula_variables
from src.bands import bands
from src.constants import constants
from src.indices import spindex
from src.utils import Bands


OUTPUT_DIR = Path("output")
DOCS_STATIC_DIR = Path("docs/_static")
SPECTRAL_INDICES_JSON = OUTPUT_DIR / "spectral-indices-dict.json"
SPECTRAL_INDICES_TABLE = OUTPUT_DIR / "spectral-indices-table.csv"

BAND_VARIABLES = [
    "A",
    "B",
    "G1",
    "G",
    "Y",
    "R",
    "N",
    "N2",
    "WV",
    "RE1",
    "RE2",
    "RE3",
    "S1",
    "S2",
    "T",
    "T1",
    "T2",
    "HV",
    "HH",
    "VV",
    "VH",
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
]

PLATFORM_BANDS = {
    "Sentinel-1 (Dual Polarisation VV-VH)": ["VV", "VH"],
    "Sentinel-1 (Dual Polarisation HH-HV)": ["HV", "HH"],
    "Sentinel-2": [
        "A",
        "B",
        "G",
        "R",
        "N",
        "N2",
        "RE1",
        "RE2",
        "RE3",
        "WV",
        "S1",
        "S2",
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
    ],
    "Landsat-OLI": [
        "A",
        "B",
        "G",
        "R",
        "N",
        "S1",
        "S2",
        "T1",
        "T2",
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
    ],
    "Landsat-TM": [
        "B",
        "G",
        "R",
        "N",
        "S1",
        "S2",
        "T",
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
    ],
    "Landsat-ETM+": [
        "B",
        "G",
        "R",
        "N",
        "S1",
        "S2",
        "T",
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
    ],
    "MODIS": [
        "B",
        "G1",
        "G",
        "R",
        "N",
        "S1",
        "S2",
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
    ],
    "Planet-Fusion": [
        "B",
        "G",
        "R",
        "N",
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
    ],
}

DOC_TABLE_DOMAINS = [
    "vegetation",
    "burn",
    "water",
    "snow",
    "urban",
    "soil",
    "clouds",
    "kernel",
    "radar",
]

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

NON_PLATFORM_VARIABLES = [
    variable
    for variable in Bands._value2member_map_.keys()
    if variable not in BAND_VARIABLES
]


def get_available_platforms(index_bands):
    """Return platforms whose bands can support an index formula."""
    available_platforms = []

    for platform, platform_bands in PLATFORM_BANDS.items():
        supported_variables = NON_PLATFORM_VARIABLES + platform_bands
        if all(band in supported_variables for band in index_bands):
            available_platforms.append(platform)

    return available_platforms


def add_formula_metadata(index_catalog):
    """Populate each spectral index with parsed bands and supported platforms."""
    for key, spectral_index in index_catalog.SpectralIndices.items():
        spectral_index.bands = parse_formula_variables(spectral_index.formula)
        spectral_index.platforms = get_available_platforms(spectral_index.bands)
        index_catalog.SpectralIndices[key] = spectral_index

    return index_catalog


def write_json_outputs(index_catalog):
    """Write the catalogue, band metadata, and constants metadata as JSON."""
    with SPECTRAL_INDICES_JSON.open("w") as fp:
        json.dump(
            json.loads(index_catalog.model_dump_json(indent=4)),
            fp,
            indent=4,
            sort_keys=True,
        )

    with (OUTPUT_DIR / "bands.json").open("w") as fp:
        json.dump(bands, fp, indent=4, sort_keys=True)

    with (OUTPUT_DIR / "constants.json").open("w") as fp:
        json.dump(constants, fp, indent=4, sort_keys=True)


def build_indices_dataframe(path=SPECTRAL_INDICES_JSON):
    """Build the public CSV dataframe from the generated catalogue JSON."""
    with path.open() as fp:
        indices = json.load(fp)

    df = pd.DataFrame(list(indices["SpectralIndices"].values()))
    return df[TABLE_COLUMNS]


def formula_to_rst_math(formula):
    """Convert a Python-like formula string to the docs' RST math format."""
    formula = formula.replace(" ", "")
    formula = formula.replace("**", "^")
    formula = formula.replace("^2.0", "^{2.0}")
    formula = formula.replace("^0.5", "^{0.5}")
    formula = formula.replace("^nexp", "^{n}")
    formula = formula.replace("^cexp", "^{c}")
    formula = formula.replace("gamma", "\\gamma ")
    formula = formula.replace("alpha", "\\alpha ")
    formula = formula.replace("beta", "\\beta ")
    formula = formula.replace("omega", "\\omega ")
    formula = formula.replace("lambdaN", "\\lambda_{N} ")
    formula = formula.replace("lambdaR", "\\lambda_{R} ")
    formula = formula.replace("lambdaG", "\\lambda_{G} ")
    formula = formula.replace("*", "\\times ")
    return f":math:`{formula}`"


def write_spectral_indices_table(df):
    """Write the flat CSV table used as a machine-readable output."""
    df.to_csv(SPECTRAL_INDICES_TABLE, index=False)


def write_docs_tables(df):
    """Write one docs CSV table for each application domain."""
    docs_df = df.copy()
    docs_df["Equation"] = docs_df["formula"].apply(formula_to_rst_math)
    docs_df["Long Name"] = (
        docs_df["long_name"] + " [`ref <" + docs_df["reference"] + ">`_]"
    )
    docs_df["Index"] = docs_df["short_name"]

    for domain in DOC_TABLE_DOMAINS:
        path = DOCS_STATIC_DIR / f"indices_{domain}.csv"
        docs_df[docs_df["application_domain"] == domain][
            ["Index", "Long Name", "Equation"]
        ].to_csv(path, index=False)


def main():
    """Generate all catalogue JSON, CSV, and docs-table outputs."""
    index_catalog = add_formula_metadata(spindex)
    write_json_outputs(index_catalog)

    df = build_indices_dataframe()
    write_spectral_indices_table(df)
    write_docs_tables(df)


if __name__ == "__main__":
    main()

"""Build README.md from static fragments and the generated v1 catalogue."""

import json
from pathlib import Path
from urllib.parse import quote

from src.v1.SpectralIndex import FormulaVisitor
from src.v1.utils import Hyperspectral, HyperspectralRange


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = REPO_ROOT / "output/v1"
CATALOGUE_PATH = OUTPUT_DIR / "spectral-indices-dict.json"
BANDS_PATH = OUTPUT_DIR / "bands.json"
CONSTANTS_PATH = OUTPUT_DIR / "constants.json"
EXTERNAL_VARIABLES_PATH = OUTPUT_DIR / "external_variables.json"
README_PATH = REPO_ROOT / "README.md"
README_PARTS_DIR = REPO_ROOT / "readme"
INTRO_PATH = README_PARTS_DIR / "intro.md"
OUTRO_PATH = README_PARTS_DIR / "outro.md"

WEBSITE_ROOT = "https://awesome-spectral-indices.github.io/awesome-spectral-indices"

DOMAIN_ORDER = [
    "vegetation",
    "water",
    "burn",
    "snow",
    "urban",
    "soil",
    "geology",
    "clouds",
]
DOMAIN_LABELS = {
    "vegetation": "Vegetation",
    "water": "Water",
    "burn": "Burn",
    "snow": "Snow",
    "urban": "Urban",
    "soil": "Soil",
    "geology": "Geology",
    "clouds": "Clouds",
}
MODALITY_ORDER = ["multispectral", "hyperspectral", "thermal", "radar"]
MODALITY_LABELS = {
    "multispectral": "Multispectral",
    "hyperspectral": "Hyperspectral",
    "thermal": "Thermal",
    "radar": "Radar",
}
INSTRUMENT_COLUMNS = ("Sentinel-2", "Landsat-89", "Landsat-457", "MODIS")
INSTRUMENT_BAND_MAPPINGS = {
    "A": ("B1", "B1", None, None),
    "B": ("B2", "B2", "B1", "B3"),
    "G": ("B3", "B3", "B2", "B4"),
    "G1": (None, None, None, "B11"),
    "N": ("B8", "B5", "B4", "B2"),
    "N2": ("B8A", None, None, None),
    "R": ("B4", "B4", "B3", "B1"),
    "RE1": ("B5", None, None, None),
    "RE2": ("B6", None, None, None),
    "RE3": ("B7", None, None, None),
    "S1": ("B11", "B6", "B5", "B6"),
    "S2": ("B12", "B7", "B7", "B7"),
    "T": (None, None, "B6", None),
    "T1": (None, "B10", None, None),
    "T2": (None, "B11", None, None),
    "WV": ("B9", None, None, None),
    "Y": (None, None, None, None),
}
ROUTE_OVERRIDES = {
    "BAI": "BAI-burn",
    "BaI": "BaI-soil",
    "MSR705": "MSR705-ratio",
    "mSR705": "mSR705-modified",
}

GENERATED_MARKERS = {
    "toc": "<!-- README-GENERATED:TOC -->",
    "properties": "<!-- README-GENERATED:PROPERTIES -->",
    "bands": "<!-- README-GENERATED:BANDS -->",
    "polarizations": "<!-- README-GENERATED:POLARIZATIONS -->",
    "hyperspectral": "<!-- README-GENERATED:HYPERSPECTRAL -->",
    "functions": "<!-- README-GENERATED:FUNCTIONS -->",
    "constants": "<!-- README-GENERATED:CONSTANTS -->",
    "external_variables": "<!-- README-GENERATED:EXTERNAL_VARIABLES -->",
}

PRIMARY_PROPERTIES = [
    ("acronym", "Required display acronym; it does not have to be unique."),
    ("name", "Required full index name; it does not have to be unique."),
    ("formula", "Validated v1 mathematical expression."),
    (
        "classification",
        "Application domain, generated sensing modalities, and optional families.",
    ),
    ("bands", "Generated spectral, thermal, and hyperspectral inputs."),
    ("polarizations", "Generated radar-polarization inputs."),
    ("constants", "Per-index definitions for constants used by the formula."),
    (
        "external_variables",
        "Per-index definitions for formula inputs supplied outside spectral data.",
    ),
    ("reductions", "Execution context for contextual reduction functions."),
    ("source", "Source link plus generated status, metadata, and citation data."),
    ("contributor", "Contributor GitHub profile URL or email address."),
    ("date_of_addition", "Catalogue contribution date in YYYY-MM-DD format."),
]

POLARIZATION_DESCRIPTIONS = {
    "HH": "Horizontal transmit, horizontal receive",
    "HV": "Horizontal transmit, vertical receive",
    "VH": "Vertical transmit, horizontal receive",
    "VV": "Vertical transmit, vertical receive",
}

FUNCTION_DESCRIPTIONS = {
    "max": ("`max(X, ...)`", "Per-pixel maximum of positional expressions."),
    "min": ("`min(X, ...)`", "Per-pixel minimum of positional expressions."),
    "tanh": ("`tanh(X)`", "Hyperbolic tangent of one expression."),
    "log": ("`log(X)`", "Natural logarithm of one expression."),
    "kernel": (
        "`kernel(X, Y)`",
        "Kernel evaluation over exactly two input expressions.",
    ),
    "spatial_max": (
        "`spatial_max(X)`",
        "Maximum of an input over the configured spatial scope.",
    ),
    "spatial_min": (
        "`spatial_min(X)`",
        "Minimum of an input over the configured spatial scope.",
    ),
    "spatial_mean": (
        "`spatial_mean(X)`",
        "Arithmetic mean of an input over the configured spatial scope.",
    ),
}


def read_markdown_fragment(path):
    """Read a static Markdown fragment used to compose the README."""
    return path.read_text()


def load_json(path):
    """Load one generated JSON document."""
    with path.open() as fp:
        return json.load(fp)


def table_text(value):
    """Escape text for a single-line Markdown table cell."""
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ")


def markdown_table(headers, rows):
    """Render a Markdown table from headers and rows."""
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend(
        "| " + " | ".join(table_text(value) for value in row) + " |" for row in rows
    )
    return "\n".join(lines)


def index_page_url(key):
    """Return the deployed VitePress URL for a catalogue key."""
    route = ROUTE_OVERRIDES.get(key, key)
    return f"{WEBSITE_ROOT}/indices/{quote(route, safe='')}.html"


def render_properties_table():
    """Render the primary top-level v1 properties."""
    return markdown_table(
        ["Property", "Meaning"],
        [(f"`{name}`", description) for name, description in PRIMARY_PROPERTIES],
    )


def render_bands_table(bands):
    """Render broad standards and their legacy instrument-band mappings."""
    missing_mappings = set(bands) - set(INSTRUMENT_BAND_MAPPINGS)
    stale_mappings = set(INSTRUMENT_BAND_MAPPINGS) - set(bands)
    if missing_mappings or stale_mappings:
        raise ValueError(
            "README instrument mappings do not match the broad-band standards: "
            f"missing={sorted(missing_mappings)}, stale={sorted(stale_mappings)}"
        )

    rows = []
    for standard, definition in bands.items():
        minimum = definition.get("min_wavelength")
        maximum = definition.get("max_wavelength")
        spectral_range = (
            f"{minimum}–{maximum}"
            if minimum is not None and maximum is not None
            else "—"
        )
        instrument_bands = [
            f"`{band}`" if band else "—" for band in INSTRUMENT_BAND_MAPPINGS[standard]
        ]
        rows.append(
            (
                f"`{standard}`",
                definition["long_name"],
                spectral_range,
                *instrument_bands,
            )
        )
    return markdown_table(
        [
            "Standard",
            "Description",
            "Spectral range (nm)",
            *INSTRUMENT_COLUMNS,
        ],
        rows,
    )


def render_polarizations_table():
    """Render the supported radar-polarization standards."""
    return markdown_table(
        ["Standard", "Description"],
        [
            (f"`{standard}`", description)
            for standard, description in POLARIZATION_DESCRIPTIONS.items()
        ],
    )


def render_hyperspectral_table():
    """Render the two dynamic hyperspectral input forms."""
    minimum = Hyperspectral.MIN_WAVELENGTH
    maximum = Hyperspectral.MAX_WAVELENGTH
    if (
        HyperspectralRange.MIN_WAVELENGTH != minimum
        or HyperspectralRange.MAX_WAVELENGTH != maximum
    ):
        raise ValueError("Hyperspectral wavelength limits are inconsistent.")
    return markdown_table(
        ["Standard", "Meaning", "Validation"],
        [
            (
                "`R<a>`",
                "Reflectance at the exact integer wavelength `a`.",
                f"`{minimum} <= a <= {maximum}`",
            ),
            (
                "`R<a>_<b>`",
                "Reflectance at any one wavelength in the inclusive range `a` to `b`.",
                f"`{minimum} <= a < b <= {maximum}`",
            ),
        ],
    )


def render_functions_table():
    """Render every function accepted by the current v1 formula parser."""
    allowed = FormulaVisitor.allowed_functions
    missing = set(allowed) - set(FUNCTION_DESCRIPTIONS)
    extra = set(FUNCTION_DESCRIPTIONS) - set(allowed)
    if missing or extra:
        raise ValueError(
            "README function descriptions do not match the formula parser: "
            f"missing={sorted(missing)}, extra={sorted(extra)}"
        )
    return markdown_table(
        ["Function", "Meaning"],
        [FUNCTION_DESCRIPTIONS[name] for name in allowed],
    )


def render_constants_table(constants):
    """Group index links that share a constant ID and description."""
    rows = []
    for standard in sorted(constants, key=lambda value: (value.casefold(), value)):
        description_groups = {}
        for key, definition in constants[standard].items():
            description_groups.setdefault(definition["description"], []).append(key)
        for description, keys in sorted(
            description_groups.items(),
            key=lambda item: (item[0].casefold(), item[0]),
        ):
            index_links = ", ".join(
                f"[{key}]({index_page_url(key)})"
                for key in sorted(keys, key=lambda value: (value.casefold(), value))
            )
            rows.append(
                (
                    f"`{standard}`",
                    index_links,
                    description,
                )
            )
    return markdown_table(["Constant", "Indices", "Description"], rows)


def render_external_variables_table(external_variables):
    """Render each index-specific external-variable description."""
    rows = []
    for standard in sorted(
        external_variables, key=lambda value: (value.casefold(), value)
    ):
        for key, definition in sorted(
            external_variables[standard].items(),
            key=lambda item: (item[0].casefold(), item[0]),
        ):
            rows.append(
                (
                    f"`{standard}`",
                    f"[{key}]({index_page_url(key)})",
                    definition["description"],
                )
            )
    return markdown_table(["Variable", "Index", "Description"], rows)


def modality_profile_rank(modalities):
    """Match the sensing-modality profile order used by the VitePress search."""
    return MODALITY_ORDER.index(modalities[0]) * 10 + len(modalities)


def catalogue_profiles(catalogue):
    """Return the catalogue grouped and sorted by sensing-modality profile."""
    profiles = {}
    for key, index in catalogue["SpectralIndices"].items():
        modalities = tuple(index["classification"]["sensing_modalities"])
        profiles.setdefault(modalities, []).append((key, index))
    return sorted(
        profiles.items(),
        key=lambda item: (
            modality_profile_rank(item[0]),
            "+".join(item[0]),
        ),
    )


def modality_profile_label(modalities):
    """Return the display label for a sensing-modality profile."""
    return " + ".join(MODALITY_LABELS[value] for value in modalities)


def modality_profile_slug(modalities):
    """Return a stable anchor component for a sensing-modality profile."""
    return "-".join(modalities)


def profile_domains(indices):
    """Return populated application domains in catalogue display order."""
    populated = {index["classification"]["application_domain"] for _, index in indices}
    return [domain for domain in DOMAIN_ORDER if domain in populated]


def render_toc(catalogue):
    """Render the README contents, including generated catalogue groups."""
    lines = [
        "## Table of Contents",
        "",
        "- [Spectral Indices](#spectral-indices)",
        "  - [Citation](#citation)",
        "  - [Properties](#properties)",
        "  - [Formula expressions](#formula-expressions)",
        "    - [Broad spectral and thermal bands](#broad-spectral-and-thermal-bands)",
        "    - [Radar polarizations](#radar-polarizations)",
        "    - [Hyperspectral standards](#hyperspectral-standards)",
        "    - [Supported functions](#supported-functions)",
        "    - [Constants](#constants)",
        "    - [External variables](#external-variables)",
        "- [Spectral Indices by Sensing Modality and Application Domain]"
        "(#spectral-indices-by-sensing-modality-and-application-domain)",
    ]
    for modalities, indices in catalogue_profiles(catalogue):
        profile_slug = modality_profile_slug(modalities)
        profile_label = modality_profile_label(modalities)
        lines.append(f"  - [{profile_label}](#modality-{profile_slug})")
        for domain in profile_domains(indices):
            lines.append(f"    - [{DOMAIN_LABELS[domain]}](#{profile_slug}-{domain})")
    lines.extend(
        (
            "- [Download Raw Files](#download-raw-files)",
            "- [Credits](#credits)",
        )
    )
    return "\n".join(lines)


def render_intro(catalogue, bands, constants, external_variables):
    """Insert generated v1 reference tables into the static introduction."""
    intro = read_markdown_fragment(INTRO_PATH)
    replacements = {
        "toc": render_toc(catalogue),
        "properties": render_properties_table(),
        "bands": render_bands_table(bands),
        "polarizations": render_polarizations_table(),
        "hyperspectral": render_hyperspectral_table(),
        "functions": render_functions_table(),
        "constants": render_constants_table(constants),
        "external_variables": render_external_variables_table(external_variables),
    }
    for name, marker in GENERATED_MARKERS.items():
        if intro.count(marker) != 1:
            raise ValueError(
                f"README intro must contain exactly one {marker!r} marker."
            )
        intro = intro.replace(marker, replacements[name])
    return intro


def render_index_list(catalogue):
    """Group v1 indices by sensing-modality profile and application domain."""
    lines = []
    for modalities, indices in catalogue_profiles(catalogue):
        profile_slug = modality_profile_slug(modalities)
        lines.extend(
            (
                f'<a id="modality-{profile_slug}"></a>',
                "",
                f"## {modality_profile_label(modalities)}",
                "",
            )
        )
        for domain in profile_domains(indices):
            domain_indices = [
                (key, index)
                for key, index in indices
                if index["classification"]["application_domain"] == domain
            ]
            lines.extend(
                (
                    f'<a id="{profile_slug}-{domain}"></a>',
                    "",
                    f"### {DOMAIN_LABELS[domain]}",
                    "",
                )
            )
            for key, index in sorted(
                domain_indices,
                key=lambda item: (item[0].casefold(), item[0]),
            ):
                lines.append(f"- [{key}]({index_page_url(key)}): {index['name']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_readme(catalogue, bands, constants, external_variables):
    """Merge static fragments with generated v1 reference data and index lists."""
    intro = render_intro(catalogue, bands, constants, external_variables)
    index_list = render_index_list(catalogue)
    outro = read_markdown_fragment(OUTRO_PATH)
    return intro.rstrip() + "\n\n" + index_list + "\n" + outro.lstrip()


def main():
    """Generate README.md from the current v1 output files."""
    catalogue = load_json(CATALOGUE_PATH)
    bands = load_json(BANDS_PATH)
    constants = load_json(CONSTANTS_PATH)
    external_variables = load_json(EXTERNAL_VARIABLES_PATH)
    README_PATH.write_text(
        build_readme(catalogue, bands, constants, external_variables)
    )


if __name__ == "__main__":
    main()

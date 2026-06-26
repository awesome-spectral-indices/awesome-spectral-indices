"""Build README.md from static Markdown fragments and generated index tables."""

import json
import string
from pathlib import Path


CATALOGUE_PATH = Path("output/spectral-indices-dict.json")
README_PATH = Path("README.md")
README_PARTS_DIR = Path("readme")
INTRO_PATH = README_PARTS_DIR / "intro.md"
OUTRO_PATH = README_PARTS_DIR / "outro.md"

APPLICATION_DOMAINS = [
    "vegetation",
    "water",
    "burn",
    "snow",
    "urban",
    "soil",
    "clouds",
    "kernel",
    "radar",
]

PLATFORM_BADGES_HTML = {
    "MODIS": '<img src="https://img.shields.io/badge/-MODIS-green?style=flat-square" alt="MODIS">',
    "Landsat-TM": '<img src="https://img.shields.io/badge/-Landsat%20TM-blueviolet?style=flat-square" alt="Landsat-TM">',
    "Landsat-ETM+": '<img src="https://img.shields.io/badge/-Landsat%20ETM+-purple?style=flat-square" alt="Landsat-ETM+">',
    "Landsat-OLI": '<img src="https://img.shields.io/badge/-Landsat%20OLI-blue?style=flat-square" alt="Landsat-OLI">',
    "Sentinel-1 (Dual Polarisation VV-VH)": '<img src="https://img.shields.io/badge/-Sentinel%201%20(Dual%20VV%20VH)-lightgray?style=flat-square" alt="(Dual Polarisation VV-VH)">',
    "Sentinel-1 (Dual Polarisation HH-HV)": '<img src="https://img.shields.io/badge/-Sentinel%201%20(Dual%20HH%20HV)-gray?style=flat-square" alt="(Dual Polarisation HH-HV)">',
    "Sentinel-2": '<img src="https://img.shields.io/badge/-Sentinel%202-red?style=flat-square" alt="Sentinel-2">',
    "Planet-Fusion": '<img src="https://img.shields.io/badge/-Planet%20Fusion-yellow?style=flat-square" alt="Planet-Fusion">',
}


def read_markdown_fragment(path):
    """Read a static Markdown fragment used to compose the README."""
    return path.read_text()


def load_catalogue(path=CATALOGUE_PATH):
    """Load the generated spectral-indices catalogue JSON."""
    with path.open("r") as fp:
        return json.load(fp)


def get_indices_by_domain(catalogue, application_domain):
    """Return index names that belong to an application domain."""
    return [
        index
        for index, attributes in catalogue["SpectralIndices"].items()
        if attributes["application_domain"] == application_domain
    ]


def render_platform_badges(platforms):
    """Render HTML badges for platforms supported by a spectral index."""
    badges = []

    for platform, badge in PLATFORM_BADGES_HTML.items():
        if platform in platforms:
            badges.append(f" {badge} ")

    return "".join(badges)


def render_index_row(index, attributes):
    """Render one HTML table row for a spectral index."""
    link = attributes["reference"]
    name = attributes["long_name"]
    badges = render_platform_badges(attributes["platforms"])
    return (
        f'<tr><td width="50%"><a href="{link}" target="_blank">{index}</a>: '
        f'{name}.</td><td width="50%">{badges}</td></tr>\n'
    )


def render_application_domain_table(catalogue, application_domain):
    """Render the README table for one application domain."""
    text = [f"\n## {application_domain.capitalize()}\n\n<table>"]
    domain_indices = get_indices_by_domain(catalogue, application_domain)

    for letter in string.ascii_uppercase:
        if any(index.upper().startswith(letter) for index in domain_indices):
            for index, attributes in catalogue["SpectralIndices"].items():
                if attributes["application_domain"] != application_domain:
                    continue
                if index.startswith(letter) or index.startswith(letter.lower()):
                    text.append(render_index_row(index, attributes))

    text.append("</table>\n")
    return "".join(text)


def render_application_domain_tables(catalogue):
    """Render all generated spectral-index tables for the README."""
    return "".join(
        render_application_domain_table(catalogue, application_domain)
        for application_domain in APPLICATION_DOMAINS
    )


def build_readme(catalogue):
    """Merge static README fragments with the generated index tables."""
    intro = read_markdown_fragment(INTRO_PATH)
    tables = render_application_domain_tables(catalogue)
    outro = read_markdown_fragment(OUTRO_PATH)
    return intro + "\n" + tables + "\n" + outro


def main():
    """Generate README.md from the catalogue and Markdown fragments."""
    catalogue = load_catalogue()
    README_PATH.write_text(build_readme(catalogue))


if __name__ == "__main__":
    main()

"""Generate VitePress content from the Awesome Spectral Indices v1 catalogue."""

import json
import re
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
INDICES_DIR = DOCS_DIR / "indices"
CATALOGUE_PATH = REPO_ROOT / "output/v1/spectral-indices-dict.json"
BANDS_PATH = REPO_ROOT / "output/v1/bands.json"
CONSTANTS_PATH = REPO_ROOT / "output/v1/constants.json"
CONTRIBUTING_PATH = REPO_ROOT / "CONTRIBUTING.md"

SAFE_FILENAME = re.compile(r"^[A-Za-z0-9._+-]+$")

VARIABLE_DESCRIPTIONS = {
    "HH": "Horizontal transmit, horizontal receive radar polarization",
    "HV": "Horizontal transmit, vertical receive radar polarization",
    "VH": "Vertical transmit, horizontal receive radar polarization",
    "VV": "Vertical transmit, vertical receive radar polarization",
}

CASE_COLLISION_ROUTES = {
    "BAI": "BAI-burn",
    "BaI": "BaI-soil",
    "MSR705": "MSR705-ratio",
    "mSR705": "mSR705-modified",
}


def load_json(path):
    """Load a JSON document."""
    with path.open() as fp:
        return json.load(fp)


def yaml_string(value):
    """Return a JSON-quoted string, which is also valid YAML."""
    return json.dumps(str(value), ensure_ascii=False)


def sentence(value):
    """Ensure a short description ends with sentence punctuation."""
    value = str(value).strip()
    if value.endswith((".", "!", "?")):
        return value
    return f"{value}."


def describe_band(name, band_metadata):
    """Return a human-readable description for a band or derived variable."""
    if name in band_metadata:
        return band_metadata[name]["long_name"]
    if name in VARIABLE_DESCRIPTIONS:
        return VARIABLE_DESCRIPTIONS[name]
    if name.startswith("k"):
        return f"Kernel variable {name}"
    return name


def render_bands(variable_names, band_metadata, constant_metadata):
    """Render the non-constant formula variables as a Markdown list."""
    band_names = [
        name for name in variable_names if name not in constant_metadata
    ]
    if not band_names:
        return "No bands are used in this index."

    return "\n".join(
        f"- `{name}`: {sentence(describe_band(name, band_metadata))}"
        for name in band_names
    )


def render_constants(variable_names, constant_metadata):
    """Render formula constants and their catalogue defaults."""
    constant_names = [
        name for name in variable_names if name in constant_metadata
    ]
    if not constant_names:
        return "No constants are used in this index."

    items = []
    for name in constant_names:
        metadata = constant_metadata[name]
        description = sentence(metadata["description"])
        default = metadata["default"]
        if default is not None:
            description = f"{description} Default: `{default}`."
        items.append(f"- `{name}`: {description}")
    return "\n".join(items)


def render_index_page(
    key,
    index,
    band_metadata,
    constant_metadata,
):
    """Render one spectral-index page using the NDVI page structure."""
    domain = index["application_domain"].replace("_", " ").title()
    bands = render_bands(
        index["bands"],
        band_metadata,
        constant_metadata,
    )
    constants = render_constants(index["bands"], constant_metadata)

    return f"""---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: {yaml_string(f'index-page domain-{index["application_domain"]}')}

hero:
  name: {yaml_string(index["short_name"])}
  text: {yaml_string(index["long_name"])}
  tagline: {yaml_string(domain)}
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: {yaml_string(index["reference"])}
---

## Formula

```
{index["formula"]}
```

### Bands

{bands}

### Constants

{constants}

## Contributor

Index contributed by {index["contributor"]} on {index["date_of_addition"]}.
"""


def copy_contributing_guide():
    """Copy the root contribution guide into the VitePress source directory."""
    shutil.copy2(CONTRIBUTING_PATH, DOCS_DIR / "CONTRIBUTING.md")


def generate_index_pages():
    """Generate one Markdown page for every v1 spectral index."""
    catalogue = load_json(CATALOGUE_PATH)["SpectralIndices"]
    band_metadata = load_json(BANDS_PATH)
    constant_metadata = load_json(CONSTANTS_PATH)

    INDICES_DIR.mkdir(parents=True, exist_ok=True)

    for key, index in catalogue.items():
        if not SAFE_FILENAME.fullmatch(key):
            raise ValueError(f"Unsafe spectral-index key for filename: {key!r}")
        page = render_index_page(
            key,
            index,
            band_metadata,
            constant_metadata,
        )
        (INDICES_DIR / f"{key}.md").write_text(page)
        if key in CASE_COLLISION_ROUTES:
            route = CASE_COLLISION_ROUTES[key]
            (INDICES_DIR / f"{route}.md").write_text(page)

    return len(catalogue)


def main():
    """Generate all catalogue-driven VitePress content."""
    copy_contributing_guide()
    count = generate_index_pages()
    print(f"Generated {count} spectral-index pages.")


if __name__ == "__main__":
    main()

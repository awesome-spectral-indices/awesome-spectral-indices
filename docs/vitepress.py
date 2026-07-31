"""Generate VitePress content from the Awesome Spectral Indices v1 catalogue."""

import hashlib
import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
INDICES_DIR = DOCS_DIR / "indices"
CATALOGUE_PATH = REPO_ROOT / "output/v1/spectral-indices-dict.json"
BANDS_PATH = REPO_ROOT / "output/v1/bands.json"
CONSTANTS_PATH = REPO_ROOT / "output/v1/constants.json"
CONTRIBUTING_PATH = REPO_ROOT / "CONTRIBUTING.md"
PEOPLE_CONTRIBUTORS_PATH = (
    DOCS_DIR / ".vitepress/data/index-contributors.json"
)

SAFE_FILENAME = re.compile(r"^[A-Za-z0-9._+-]+$")
EMAIL_ADDRESS = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

EMAIL_ICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
    '<path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 '
    '0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5-8-5V6l8 '
    '5 8-5v2Z"/></svg>'
)

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


def contributor_member(value):
    """Convert a catalogue contributor URL or email into a team member."""
    value = str(value).strip()
    parsed = urlsplit(value)
    path_parts = [part for part in parsed.path.split("/") if part]

    if (
        parsed.scheme in {"http", "https"}
        and parsed.netloc.lower() in {"github.com", "www.github.com"}
        and len(path_parts) == 1
    ):
        username = path_parts[0]
        profile = f"https://github.com/{username}"
        return {
            "avatar": f"{profile}.png",
            "name": username,
            "title": "Index Contributor",
            "links": [{"icon": "github", "link": profile}],
        }

    if EMAIL_ADDRESS.fullmatch(value):
        normalized_email = value.casefold()
        avatar_hash = hashlib.md5(
            normalized_email.encode(), usedforsecurity=False
        ).hexdigest()
        return {
            "avatar": (
                f"https://www.gravatar.com/avatar/{avatar_hash}?d=identicon"
            ),
            "name": value,
            "title": "Index Contributor",
            "links": [
                {
                    "icon": {"svg": EMAIL_ICON},
                    "link": f"mailto:{value}",
                }
            ],
        }

    raise ValueError(
        "Contributor must be a GitHub profile URL or email address: "
        f"{value!r}"
    )


def generate_people_contributors():
    """Generate deduplicated People-page members from the v1 catalogue."""
    catalogue = load_json(CATALOGUE_PATH)["SpectralIndices"]
    members_by_profile = {}

    for index in catalogue.values():
        member = contributor_member(index["contributor"])
        profile_link = member["links"][0]["link"].casefold()
        members_by_profile.setdefault(profile_link, member)

    members = sorted(
        members_by_profile.values(), key=lambda member: member["name"].casefold()
    )
    PEOPLE_CONTRIBUTORS_PATH.parent.mkdir(parents=True, exist_ok=True)
    PEOPLE_CONTRIBUTORS_PATH.write_text(
        json.dumps(members, indent=2, ensure_ascii=False) + "\n"
    )
    return len(members)


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
    contributor_count = generate_people_contributors()
    print(f"Generated {count} spectral-index pages.")
    print(f"Generated {contributor_count} People-page contributors.")


if __name__ == "__main__":
    main()

"""Generate VitePress content from the Awesome Spectral Indices v1 catalogue."""

import hashlib
import json
import re
import shutil
from html import escape
from pathlib import Path
from urllib.parse import quote, urlsplit


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
INDICES_DIR = DOCS_DIR / "indices"
CATALOGUE_PATH = REPO_ROOT / "output/v1/spectral-indices-dict.json"
BANDS_PATH = REPO_ROOT / "output/v1/bands.json"
CONTRIBUTING_PATH = REPO_ROOT / "CONTRIBUTING.md"
PEOPLE_CONTRIBUTORS_PATH = DOCS_DIR / ".vitepress/data/index-contributors.json"

SAFE_FILENAME = re.compile(r"^[A-Za-z0-9._+-]+$")
EMAIL_ADDRESS = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

EMAIL_ICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
    '<path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 '
    "0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5-8-5V6l8 "
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


def render_bands(band_names, band_metadata):
    """Render the formula's band and derived-input variables."""
    if not band_names:
        return "No bands are used in this index."

    return "\n".join(
        f"- `{name}`: {sentence(describe_band(name, band_metadata))}"
        for name in band_names
    )


def render_constants(constant_definitions):
    """Render formula constants and their contributor-provided metadata."""
    if not constant_definitions:
        return "No constants are used in this index."

    items = []
    for name, definition in constant_definitions.items():
        description = escape(sentence(definition["description"]))
        cards = []

        default = definition.get("default_value")
        default_value = "Not specified" if default is None else escape(str(default))
        default_state = " is-empty" if default is None else ""
        cards.append(
            f"""<div class="constant-detail-card constant-default{default_state}">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">{default_value}</strong>
</div>"""
        )

        suggested_range = definition.get("suggested_range")
        if suggested_range is not None:
            range_start = escape(str(suggested_range[0]))
            range_end = escape(str(suggested_range[1]))
            cards.append(
                f"""<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">{range_start}<span aria-hidden="true">–</span>{range_end}</strong>
</div>"""
            )

        suggested_values = definition.get("suggested_values")
        if suggested_values is not None:
            rendered_values = []
            for condition, value in suggested_values.items():
                if isinstance(value, list):
                    value_start = escape(str(value[0]))
                    value_end = escape(str(value[1]))
                    rendered_value = (
                        f'{value_start}<span aria-hidden="true">–</span>{value_end}'
                    )
                else:
                    rendered_value = escape(str(value))
                rendered_values.append(
                    f"""<div class="constant-suggestion-row">
<dt>{escape(str(condition))}</dt>
<dd>{rendered_value}</dd>
</div>"""
                )
            cards.append(
                """<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
"""
                + "\n".join(rendered_values)
                + """
</dl>
</div>"""
            )

        rendered_cards = "\n".join(cards)
        items.append(
            f"""<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">{escape(str(name))}</code>
<p>{description}</p>
</header>
<div class="constant-details">
{rendered_cards}
</div>
</article>"""
        )

    return '<div class="constant-list">\n' + "\n".join(items) + "\n</div>"


def render_external_variables(external_definitions):
    """Render descriptions for formula inputs supplied outside spectral data."""
    return "\n".join(
        f"- `{name}`: {sentence(definition['description'])}"
        for name, definition in external_definitions.items()
    )


def render_source_companions(companion_keys):
    """Render links to indices generated from the same scientific source."""
    return "\n".join(
        f"- [`{key}`](/indices/{quote(CASE_COLLISION_ROUTES.get(key, key), safe='')})"
        for key in companion_keys
    )


def render_index_page(
    key,
    index,
    band_metadata,
):
    """Render one spectral-index page using the NDVI page structure."""
    domain = index["application_domain"].replace("_", " ").title()
    bands = render_bands(index["bands"], band_metadata)
    constants = render_constants(index["constants"])
    external_variables_section = ""
    if index["external_variables"]:
        external_variables = render_external_variables(index["external_variables"])
        external_variables_section = f"""### External Variables

{external_variables}

"""
    source_companions_section = ""
    if index["source"]["source_companions"]:
        source_companions = render_source_companions(
            index["source"]["source_companions"]
        )
        source_companions_section = f"""### Source Companions

These indices are part of the same scientific source:

{source_companions}

"""

    return f"""---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: {yaml_string(f'index-page domain-{index["application_domain"]}')}

hero:
  name: {yaml_string(index["acronym"])}
  text: {yaml_string(index["name"])}
  tagline: {yaml_string(domain)}
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: {yaml_string(index["source"]["source_link"])}
---

## Formula

```
{index["formula"]}
```

### Bands

{bands}

### Constants

{constants}

{external_variables_section}{source_companions_section}## Contributor

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
            "avatar": (f"https://www.gravatar.com/avatar/{avatar_hash}?d=identicon"),
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
        "Contributor must be a GitHub profile URL or email address: " f"{value!r}"
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

    INDICES_DIR.mkdir(parents=True, exist_ok=True)

    for key, index in catalogue.items():
        if not SAFE_FILENAME.fullmatch(key):
            raise ValueError(f"Unsafe spectral-index key for filename: {key!r}")
        page = render_index_page(
            key,
            index,
            band_metadata,
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

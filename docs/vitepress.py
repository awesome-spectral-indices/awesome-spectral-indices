"""Generate VitePress content from the Awesome Spectral Indices v1 catalogue."""

import hashlib
import json
import os
import re
import shutil
from html import escape
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
INDICES_DIR = DOCS_DIR / "indices"
CATALOGUE_PATH = REPO_ROOT / "output/v1/spectral-indices-dict.json"
BIBLIOGRAPHY_PATH = REPO_ROOT / "output/v1/spectral-indices-references.bib"
CONTRIBUTING_PATH = REPO_ROOT / "CONTRIBUTING.md"
PEOPLE_CONTRIBUTORS_PATH = DOCS_DIR / ".vitepress/data/index-contributors.json"
REPOSITORY_CONTRIBUTORS_PATH = (
    DOCS_DIR / ".vitepress/data/repository-contributors.json"
)

GITHUB_REPOSITORY = os.environ.get(
    "GITHUB_REPOSITORY",
    "awesome-spectral-indices/awesome-spectral-indices",
)
GITHUB_CONTRIBUTORS_URL = (
    f"https://api.github.com/repos/{GITHUB_REPOSITORY}/contributors"
)
GITHUB_API_VERSION = "2022-11-28"
GITHUB_API_TIMEOUT = 20
AUTOMATED_GITHUB_ACCOUNTS = {"actions-user", "github-actions[bot]"}

SAFE_FILENAME = re.compile(r"^[A-Za-z0-9._+-]+$")
EMAIL_ADDRESS = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

EMAIL_ICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
    '<path fill="currentColor" d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 '
    "0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Zm0 4-8 5-8-5V6l8 "
    '5 8-5v2Z"/></svg>'
)

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


def load_bibtex_entries(path):
    """Load generated BibTeX entries keyed by their citation key."""
    entries = {}
    for block in re.split(r"\n\s*\n(?=@)", path.read_text().strip()):
        match = re.match(r"^@\w+\{([^,\s]+),", block)
        if match:
            entries[match.group(1)] = block.strip()
    return entries


def render_citation_slot(key, index, bibtex_entries):
    """Render citation Markdown so VitePress can syntax-highlight it."""
    metadata = index["source"].get("source_metadata") or {}
    citation = metadata.get("how_to_cite")
    if not citation:
        return ""

    citation_key = citation["bibtex"]
    try:
        bibtex = bibtex_entries[citation_key]
    except KeyError as error:
        raise ValueError(
            f"Missing BibTeX entry {citation_key!r} for spectral index {key!r}"
        ) from error

    apa = citation["apa"]
    if "```" in bibtex or "```" in apa:
        raise ValueError(f"Citation for spectral index {key!r} contains a code fence")

    return f"""::: code-group

```bibtex [BibTeX]
{bibtex}
```

```text [APA]
{apa}
```

:::
"""


def render_index_page(
    key,
    index,
    bibtex_entries,
):
    """Render one spectral-index page with a themed hero and detail tabs."""
    classification = index["classification"]
    domain = classification["application_domain"].replace("_", " ").title()
    domain_badge = (
        '<span class="hero-domain-badge">' + escape(domain) + "</span>"
    )
    modality_badges = "".join(
        (
            '<span class="hero-modality-badge modality-'
            + escape(modality)
            + '">'
            + escape(modality.replace("_", " ").title())
            + "</span>"
        )
        for modality in classification["sensing_modalities"]
    )
    hero_tagline = (
        '<span class="hero-classification-badges">'
        + domain_badge
        + modality_badges
        + "</span>"
    )
    citation_slot = render_citation_slot(key, index, bibtex_entries)

    return f"""---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: {yaml_string(f'index-page domain-{classification["application_domain"]}')}

hero:
  name: {yaml_string(index["acronym"])}
  text: {yaml_string(index["name"])}
  tagline: {yaml_string(hero_tagline)}
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: {yaml_string(index["source"]["source_link"])}
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key={yaml_string(key)}>

{citation_slot}</IndexDetails>
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


def fetch_repository_contributors():
    """Fetch all human contributors reported by the GitHub repository."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Awesome-Spectral-Indices-VitePress",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }
    github_token = os.environ.get("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    contributors = []
    page = 1
    while True:
        request = Request(
            f"{GITHUB_CONTRIBUTORS_URL}?per_page=100&page={page}",
            headers=headers,
        )
        with urlopen(request, timeout=GITHUB_API_TIMEOUT) as response:
            payload = json.load(response)

        if not isinstance(payload, list):
            raise ValueError("GitHub contributors response must be a list")

        contributors.extend(payload)
        if len(payload) < 100:
            break
        page += 1

    return contributors


def generate_repository_contributors():
    """Generate People-page members from the GitHub contributors API."""
    members = []
    for contributor in fetch_repository_contributors():
        username = contributor.get("login")
        account_type = contributor.get("type")
        if (
            not username
            or account_type == "Bot"
            or username.casefold() in AUTOMATED_GITHUB_ACCOUNTS
            or username.casefold().endswith("[bot]")
        ):
            continue

        profile = contributor.get("html_url") or f"https://github.com/{username}"
        avatar = contributor.get("avatar_url") or f"{profile}.png"
        members.append(
            {
                "avatar": avatar,
                "name": username,
                "title": "Repository Contributor",
                "links": [{"icon": "github", "link": profile}],
            }
        )

    members.sort(key=lambda member: member["name"].casefold())
    REPOSITORY_CONTRIBUTORS_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPOSITORY_CONTRIBUTORS_PATH.write_text(
        json.dumps(members, indent=2, ensure_ascii=False) + "\n"
    )
    return len(members)


def generate_index_pages():
    """Generate every v1 index page and remove obsolete generated pages."""
    catalogue = load_json(CATALOGUE_PATH)["SpectralIndices"]
    bibtex_entries = load_bibtex_entries(BIBLIOGRAPHY_PATH)

    INDICES_DIR.mkdir(parents=True, exist_ok=True)
    expected_page_names = {"index.md"}

    for key, index in catalogue.items():
        if not SAFE_FILENAME.fullmatch(key):
            raise ValueError(f"Unsafe spectral-index key for filename: {key!r}")
        page = render_index_page(
            key,
            index,
            bibtex_entries,
        )
        filename = f"{key}.md"
        expected_page_names.add(filename)
        (INDICES_DIR / filename).write_text(page)
        if key in CASE_COLLISION_ROUTES:
            route = CASE_COLLISION_ROUTES[key]
            route_filename = f"{route}.md"
            expected_page_names.add(route_filename)
            (INDICES_DIR / route_filename).write_text(page)

    for path in INDICES_DIR.glob("*.md"):
        if path.name not in expected_page_names:
            path.unlink()

    return len(catalogue)


def main():
    """Generate all catalogue-driven VitePress content."""
    copy_contributing_guide()
    count = generate_index_pages()
    contributor_count = generate_people_contributors()
    repository_contributor_count = generate_repository_contributors()
    print(f"Generated {count} spectral-index pages.")
    print(f"Generated {contributor_count} People-page contributors.")
    print(
        "Generated "
        f"{repository_contributor_count} People-page repository contributors."
    )


if __name__ == "__main__":
    main()

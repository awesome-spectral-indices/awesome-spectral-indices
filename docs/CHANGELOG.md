# Changelog

All notable changes to Awesome Spectral Indices are summarized here.

## 1.0.0 (Upcoming)

Awesome Spectral Indices has started its migration to v1. The migration is
being developed alongside v0: the existing API and v0 output files remain
available and can continue to be used, and spectral indices can still be
submitted through the usual contribution process.

### Added

- Added an independent v1 source tree under `src/v1/` as the foundation for
  evolving the catalogue without changing the v0 implementation.
- Added v1 catalogue outputs under `output/v1/`, including:
  - `spectral-indices-dict.json`
  - `spectral-indices-table.csv`
  - `bands.json`
  - `constants.json`
- Added a v1 generator that parses formula variables and writes the new outputs
  independently of v0.
- Added a dedicated v1 test suite under `test/v1/`.
- Added characterization tests for the existing catalogue, including:
  - catalogue structure and required properties;
  - supported application domains;
  - formula parsing and rejection of unsupported syntax;
  - validation of index definitions; and
  - consistency of generated JSON and CSV outputs.
- Added root-level Markdown contribution guidelines with instructions for
  creating a Conda or `venv` development environment, running the tests, and
  submitting an index.
- Added links to the contribution guidelines and the AI and Scientific
  Validation Policy from the new-index issue template.
- Added a new VitePress website as the foundation for the v1 documentation.
- Added VitePress support for mathematical notation through MathJax.
- Added a catalogue search page with:
  - immediate filtering by catalogue key, short name, long name, and
    application domain;
  - an advanced search panel for individual metadata fields;
  - filtering by required bands, parameters, radar polarizations, and kernel
    variables;
  - results grouped by application domain; and
  - a live filtered-versus-total result count.
- Added one generated documentation page for every spectral index. Each page
  includes its formula, required variables, constants, reference, contributor,
  and date of addition.
- Added application-domain styling and artwork for vegetation, water, burn,
  snow, urban, soil, clouds, kernel, and radar index pages.
- Added a responsive green visual theme with translucent navigation, liquid
  highlights, and light and dark mode support.
- Added the **v1 Explained** page documenting the current v0/v1 schema
  difference, property meanings, validation rules, generated files, and
  migration status.
- Added a VitePress content generator that:
  - copies `CONTRIBUTING.md` into the website;
  - reads the generated v1 catalogue and metadata;
  - creates the spectral-index pages; and
  - handles routes whose names differ only by letter case.

### Changed

- Migrated catalogue validation from Pydantic 1 to Pydantic 2.
- Replaced legacy Pydantic validators and configuration with
  `field_validator`, `ConfigDict`, and Pydantic 2 serialization.
- Removed the custom `orjson` serialization configuration in favor of the
  standard Pydantic 2 and JSON serialization paths.
- Added explicit string element types to the generated `bands` and `platforms`
  lists in the v0 model.
- Consolidated catalogue-generation dependencies in `requirements.txt` and
  test dependencies in `requirements-test.txt`.
- Moved the preserved v0 catalogue generator from `main.py` to
  `src/main_v0.py`.
- Moved the README generator from `readme.py` to `readme/readme.py`.
- Updated the scheduled generation workflow to run the v0 generator, v1
  generator, VitePress content generator, and README generator.
- Modernized the test workflow to run on Python 3.10, 3.11, and 3.12 with pip
  dependency caching and read-only repository permissions.
- Updated the generation workflow to use Python 3.10, dependency caching, and
  explicit write permissions.
- Updated README links and badges to use the
  `awesome-spectral-indices/awesome-spectral-indices` organization repository.
- Updated the README logo to use `docs/public/asi.png`.
- Added a README migration notice explaining that the old website is no longer
  available, the existing API remains usable, and index submissions remain
  open.
- Updated contribution and download links to point to their current repository
  locations.
- Expanded the new-index issue template to list all currently supported
  application domains.

### Removed

- Removed the generated `platforms` property from v1 spectral-index records.
  The v0 catalogue continues to generate it.
- Removed the retired Read the Docs configuration and links.
- Removed the former Sphinx documentation project, including its configuration,
  build files, dependency file, reStructuredText pages, and generated
  application-domain tables.
- Removed direct dependency installation commands from GitHub Actions in favor
  of the repository requirements files.

### Fixed

- Corrected the Aerosols band name in the band metadata.
- Corrected the Landsat 9 coastal aerosol platform label, which previously
  identified the platform as Landsat 8.

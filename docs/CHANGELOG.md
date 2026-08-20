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
  - `external_variables.json`
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
- Added `min()`, `max()`, and the unary `tanh()` and natural-logarithm `log()`
  calls to the v1 formula expression language. Function-call syntax is new in
  the v1 schema.
- Added WCI3 (Wheat Canopy Index, Growth Stage 3) as the first catalogue index
  using nested allowed functions. Its v1 formula combines multi-argument
  `max()` with unary `tanh()` and an index-specific `epsilon` constant.
- Added the contextual reduction functions `spatial_max()`, `spatial_min()`,
  and `spatial_mean()` to the v1 formula language. Their shared spatial scope
  is configured through the conditionally required `reductions` property,
  which currently accepts `aoi` and `scene`.
- Added CWI (Coastal Water Index) to v1 as the first index using contextual
  spatial reductions. Its two `spatial_max()` operations are evaluated over
  the area of interest without introducing generated reduction operands.
- Added the strict two-input `kernel()` function to the v1 formula language so
  kernel evaluations can be expressed as operations over their underlying
  inputs rather than as additional operands.
- Added the structured v1 `classification` property. Contributors provide the
  required `application_domain` and optional `family`, while generation adds
  one or more sensing modalities from the formula standards.
- Added `geology` as an application domain and `kernel`, `tasseled_cap`, and
  `radar` as the initial supported index families.
- Added the six Thematic Mapper Tasseled Cap features—brightness, wetness,
  greenness, fourth, fifth, and sixth—to v1 as vegetation indices in the
  `tasseled_cap` family.
- Added the v1 `Polarizations` registry and generated `polarizations` property
  for the `HH`, `HV`, `VH`, and `VV` radar inputs.
- Added the range-based v1 `Hyperspectral` standard. Formula operands from
  `R300` through `R2500` represent reflectance at an integer wavelength in
  nanometres and generate the `hyperspectral` sensing modality.
- Added the dynamic `HyperspectralRange` standard. Operands such as
  `R750_800` represent one selectable reflectance wavelength within an
  inclusive interval without enumerating every possible wavelength range.
- Added CARI (Carotenoid Index) to v1 as the first hyperspectral index, using
  reflectance inputs at 720 nm and 521 nm.
- Added fifteen hyperspectral pigment indices to v1: RARSa, RARSb, RARSc,
  PSSRa, PSSRb, PSSRc, PSNDa, PSNDb, PSNDc, OPSSRa, OPSSRb, OPSSRc, OPSNDa,
  OPSNDb, and OPSNDc.
- Added ten hyperspectral Reflectance Band Ratio indices to v1: the
  untransformed URBR1 through URBR5 and the scatter-adjusted SARBR1 through
  SARBR5.
- Added four hyperspectral physiological and photochemical reflectance
  indices to v1: PRI550, PRI570, PRIm1, and PRIm4.
- Added RVSI (Red-edge Vegetation Stress Index) to v1 as a hyperspectral
  vegetation index.
- Added NDNI (Normalized Difference Nitrogen Index) and NDLI (Normalized
  Difference Lignin Index) to v1 as the first catalogue indices using the
  natural-logarithm `log()` formula function.
- Added NDISI (Normalized Difference Ice-Snow Index) to v1 as the first index
  using selectable hyperspectral wavelength ranges.
- Added LCI (Leaf Chlorophyll Index) as a hyperspectral vegetation index and
  GreenDVI (Green Difference Vegetation Index) as a multispectral vegetation
  index.
- Added SUI (Sealed Urban Index) to v1 as a multispectral urban index.
- Added NDVISR (Normalized Difference Vegetation Index with Simple Ratio) and
  SAVISR (Soil-Adjusted Vegetation Index with Simple Ratio) to v1 as
  multispectral vegetation indices.
- Added CCRI (Carotenoid-Chlorophyll Ratio Index) to v1 as a hyperspectral
  vegetation index.
- Added a catalogue search page with:
  - immediate filtering by catalogue key, acronym, name, and
    application domain;
  - an advanced search panel for individual metadata fields;
  - filtering by source link, link status, link type, and source type;
  - filtering independently by classification, required bands, radar
    polarizations, constants, and external variables;
  - results arranged by sensing-modality profile and then application domain;
  - results grouped by application domain; and
  - a live filtered-versus-total result count.
- Added one generated documentation page for every spectral index. Each page
  includes its formula, required bands, constants, external variables, source,
  contributor, and date of addition.
- Added the generated v1 `source.source_companions` property, which lists the
  other catalogue keys sharing an index's exact source link. Generated index
  pages link those keys to their companion pages.
- Added the optional contributor-provided
  `source.source_link_semantic_scholar` object for Semantic Scholar paper and
  corpus identifiers, recommended when an index source does not use a DOI
  link.
- Added Semantic Scholar Academic Graph enrichment as the fallback for
  non-DOI sources and DOI sources unavailable from Crossref. Paper IDs are
  resolved before corpus IDs through rate-limited batch requests, and returned
  publication metadata and citation counts identify `semantic_scholar` as
  their provider.
- Added the **v1 Explained** page documenting the current v0/v1 schema
  difference, property meanings, validation rules, generated files, and
  migration status.
- Added a catalogue status dashboard with interactive summaries of source-link
  availability, DOI coverage, and source-type completeness, plus expandable
  affected-index lists.
- Added an interactive, tabbed catalogue dashboard showing index counts by
  application domain and sensing modality; publication totals by year, venue,
  and source type; and citation-count rankings both catalogue-wide and within
  each application domain. Every chart provides drill-down links to the
  matching indices.
- Added an automatically generated Repository Contributors section to the
  People page using contribution data from the GitHub repository.
- Added generated `source.source_metadata` publication metadata for DOI-backed
  indices using Crossref, including titles, venues, volume and issue details,
  authors, publication years, and dated citation counts. Added
  `spectral-indices-citations.json` to retain the citation-count history for
  every index.
- Added `spectral-indices-references.bib`, containing one generated BibTeX
  entry per unique retrieved source. Added `source_metadata.how_to_cite` with
  the shared BibTeX key and an APA citation for each associated index.
- Added a VitePress content generator that:
  - copies `CONTRIBUTING.md` into the website;
  - reads the generated v1 catalogue and metadata;
  - creates the spectral-index pages; and
  - handles routes whose names differ only by letter case.

### Changed

- Renamed the generated v1 `source.source_metadata.citations` property to
  `citations_metrics`. In addition to the latest citation count and retrieval
  date, it now provides deterministic ranks and citation-count percentiles
  across the complete cited catalogue, within the same application domain,
  and within an inclusive five-year publication-age window.
- Renamed the previous v1 `MSAVI` definition to `MSAVI2`, matching the name of
  its closed-form recursive formula. Added the distinct soil-line-dependent
  MSAVI formula with its `gamma` constant. The v0 definition remains unchanged.
- Replaced the broad-band v1 CRI550 and CRI700 approximations with their
  original hyperspectral formulas, `(1 / R510) - (1 / R550)` and
  `(1 / R510) - (1 / R700)`. The v0 definitions remain unchanged.
- Replaced the broad-band v1 PSRI approximation `(R - B) / RE2` with the
  original hyperspectral formula `(R678 - R500) / R750`, and updated its name
  to Plant Senescence Reflectance Index. The v0 definition remains unchanged.
- Renamed the initial RBR1 through RBR5 catalogue keys and acronyms to URBR1
  through URBR5 to distinguish untransformed from scatter-adjusted ratios.
- Renamed the required v1 spectral-index properties `short_name` to `acronym`
  and `long_name` to `name`. Neither property is required to be unique.
- Replaced the v1 `reference` string with a structured `source` object. The
  contributor provides its required `source_link` and may optionally provide
  descriptive `source_metadata` marked with `source: contributor`.
  Citation counts and citation formats remain generated-only. For DOI links,
  a successful or cached Crossref record replaces contributed metadata as the
  authoritative record; contributed metadata is retained when Crossref has no
  record. Generation also adds `source_link_status`, `source_link_type`, and
  source-companion metadata.
- Changed the scheduled catalogue refresh from daily to weekly. Crossref
  responses are cached for seven days and shared by every index using the same
  DOI.
- Classified EVI as an article and NDVI and TVI as conference-paper sources in
  the v1 catalogue.
- Split formula constants from bands in v1. Constant-using indices now submit a
  description and optional numeric default for every formula constant, while
  `bands` contains spectral and radar inputs. The generated `constants.json`
  groups these definitions first by standard constant and then by index.
  Constant definitions can also include condition-specific `suggested_values`
  and a general two-number `suggested_range`.
- Replaced the synthetic kernel operands in the v1 kEVI, kNDVI, kRVI, kVARI,
  and kIPVI formulas with explicit `kernel(X, Y)` calls. Removed all fourteen
  `kXY` values from the v1 `Bands` registry; generated kernel-index band lists
  now contain only their underlying observed inputs. kEVI additionally defines
  the `L` constant exposed by `kernel(N, L)`.
- Moved the required v1 `application_domain` into `classification`. The five
  kernel indices now use vegetation with the kernel family. The thirteen radar
  indices use the radar family and vegetation application, except NDPolI,
  which uses the new geology application.
- Split radar polarizations from spectral and thermal bands in v1. Generated
  `bands` no longer contains `HH`, `HV`, `VH`, or `VV`; those inputs are now
  written to `polarizations`, while `classification.sensing_modalities`
  distinguishes multispectral, thermal, and radar requirements.
- Separated formula inputs supplied outside spectral data into a new v1
  `External` registry. `PAR` is now an external variable rather than a
  constant, and NIRvP supplies its required, description-only definition
  through `external_variables`. Generated catalogue and CSV records include
  this property, while `external_variables.json` groups definitions by
  external-variable standard and index.
- Changed the OCVI exponent constant from `cexp` to `c` in v1 to preserve the
  notation used by its original source, with OCVI-specific metadata stored
  independently from other indices that also use the `c` standard.
- Changed the GDVI exponent constant from `nexp` to `n` in v1 to preserve the
  notation used by its original source, with GDVI-specific metadata stored
  independently from RWI's use of the same `n` standard.
- Changed the ATSAVI formula in v1 to replace its hard-coded `0.08` adjustment
  with the source-defined `X` constant. Added the ATSAVI-specific `X`, `sla`,
  and `slb` descriptions and defaults, including `X = 0.08`.
- Changed the v1 constant standard used by NDWIns from `alpha` to `a` and the
  standard used by NDSInw from `beta` to `b`. Added their index-specific
  descriptions and retained the submitted defaults of `a = 2.0` and
  `b = 0.05`.
- Completed the first v1 metadata pass for all 45 indices that use registered
  constants. Their 75 per-index definitions now include the submitted
  descriptions, defaults where universal values are appropriate, and
  source-specific suggested values and ranges.
- Changed the GARI formula in v0 and v1 to apply an explicit
  atmospheric-correction parameter, `lmb`, to `(B - R)`. Added its
  index-specific v1 description and a default of `lmb = 1.0`.
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
- Updated the README and website to use theme-aware light and dark logo assets,
  and retained the previous artwork as `docs/public/legacy-logo.png`.
- Added a README migration notice explaining that the old website is no longer
  available, the existing API remains usable, and index submissions remain
  open.
- Updated contribution and download links to point to their current repository
  locations.
- Expanded the new-index issue template to list all currently supported
  application domains.

### Removed

- Removed SR3 from v1 because its broad-band representation corresponds to the
  newly represented hyperspectral SARBR5 index. SR3 remains available in v0.
- Removed the generated `platforms` property from v1 spectral-index records.
  The v0 catalogue continues to generate it.
- Removed the retired Read the Docs configuration and links.
- Removed the former Sphinx documentation project, including its configuration,
  build files, dependency file, reStructuredText pages, and generated
  application-domain tables.
- Removed direct dependency installation commands from GitHub Actions in favor
  of the repository requirements files.

### Fixed

- Replaced the unavailable CiteSeerX source link shared by AVI, BI, and SI with
  an operational publication page.
- Corrected the v1 ARVI and SARVI formulas so the atmospheric-resistance
  coefficient `gamma` is applied to the published `(B - R)` term. The v0
  definitions remain unchanged.
- Corrected the Aerosols band name in the band metadata.
- Corrected the Landsat 9 coastal aerosol platform label, which previously
  identified the platform as Landsat 8.

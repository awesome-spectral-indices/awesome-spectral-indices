<p align="center">
  <br>
  <a href="https://github.com/awesome-spectral-indices/awesome-spectral-indices">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/public/logo-dark.png">
      <source media="(prefers-color-scheme: light)" srcset="docs/public/logo.png">
      <img src="docs/public/logo.png" alt="Awesome Spectral Indices" width="70%">
    </picture>
  </a>
  <br>
  <br>
</p>
<p align="center">
    <em>A ready-to-use curated list of Spectral Indices for Remote Sensing applications.</em>
</p>
<p align="center">
<a href="https://github.com/sindresorhus/awesome" target="_blank">
    <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome">
</a>
<a href="https://share.streamlit.io/davemlz/espectro/main/espectro.py" target="_blank">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit">
</a>
<a href="https://github.com/awesome-spectral-indices/awesome-spectral-indices/actions/workflows/tests.yml" target="_blank">
    <img src="https://github.com/awesome-spectral-indices/awesome-spectral-indices/actions/workflows/tests.yml/badge.svg" alt="Tests">
</a>
<a href="https://zenodo.org/badge/latestdoi/355720108"><img src="https://zenodo.org/badge/355720108.svg" alt="DOI"></a>
<a href="https://github.com/sponsors/davemlz" target="_blank">
    <img src="https://img.shields.io/badge/GitHub%20Sponsors-Donate-ff69b4.svg" alt="GitHub Sponsors">
</a>
<a href="https://www.buymeacoffee.com/davemlz" target="_blank">
    <img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-Donate-ff69b4.svg" alt="Buy me a coffee">
</a>
<a href="https://ko-fi.com/davemlz" target="_blank">
    <img src="https://img.shields.io/badge/kofi-Donate-ff69b4.svg" alt="Ko-fi">
</a>
<a href="https://twitter.com/dmlmont" target="_blank">
    <img src="https://img.shields.io/twitter/follow/dmlmont?style=social" alt="Twitter">
</a>
<a href="https://github.com/psf/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black">
</a>
</p>

---

**GitHub**: <a href="https://github.com/awesome-spectral-indices/awesome-spectral-indices" target="_blank">github.com/awesome-spectral-indices/awesome-spectral-indices</a>

**Website**: <a href="https://awesome-spectral-indices.github.io/awesome-spectral-indices/" target="_blank">awesome-spectral-indices.github.io/awesome-spectral-indices/</a>

**Python Package**: <a href="https://github.com/awesome-spectral-indices/spyndex" target="_blank">github.com/awesome-spectral-indices/spyndex</a>

**Paper**: <a href="https://doi.org/10.1038/s41597-023-02096-0" target="_blank">doi.org/10.1038/s41597-023-02096-0</a>

**Streamlit App**: <a href="https://github.com/awesome-spectral-indices/espectro" target="_blank">github.com/awesome-spectral-indices/espectro</a>

**Google Earth Engine**: <a href="https://github.com/davemlz/eemont" target="_blank">github.com/davemlz/eemont</a> (Python), <a href="https://github.com/awesome-spectral-indices/spectral" target="_blank">github.com/awesome-spectral-indices/spectral</a> (JavaScript) and <a href="https://github.com/r-earthengine/rgeeExtra" target="_blank">github.com/r-earthengine/rgeeExtra</a> (R)

**Julia Package**: <a href="https://github.com/awesome-spectral-indices/SpectralIndices.jl" target="_blank">github.com/awesome-spectral-indices/SpectralIndices.jl</a>

---

> [!WARNING]
> Awesome Spectral Indices is being migrated to v1. The v1 catalogue and schema are **experimental and may change** while the migration is in progress. Existing APIs continue to use v0 until their individual migrations are ready.
>
> Read [v1 Explained](https://awesome-spectral-indices.github.io/awesome-spectral-indices/v1.html) for the current schema, implemented changes, and migration status.

> [!IMPORTANT]
> **Call for Indices!** Researchers who have published—or aim to publish—their
> novel spectral indices are encouraged to add them to this repository. To add
> an index, follow the [Contribution Guidelines](CONTRIBUTING.md).
>
> If you know a spectral index that is missing, or find an error in an existing
> entry, please open an
> [issue](https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new).
> There is no deadline; the repository is continuously updated.

<!-- README-GENERATED:TOC -->

# Spectral Indices

Spectral indices are widely used throughout the remote-sensing community. This
repository curates classical and novel indices for different Earth-observation
applications and makes their definitions available across programming
languages and processing environments.

The README now follows the experimental v1 catalogue. Browse the generated
[CSV table](https://github.com/awesome-spectral-indices/awesome-spectral-indices/blob/main/output/v1/spectral-indices-table.csv),
or download the raw
[CSV](https://raw.githubusercontent.com/awesome-spectral-indices/awesome-spectral-indices/main/output/v1/spectral-indices-table.csv)
and
[JSON](https://raw.githubusercontent.com/awesome-spectral-indices/awesome-spectral-indices/main/output/v1/spectral-indices-dict.json)
files.

## Citation

If you use this work, please consider citing the following paper:

```bibtex
@article{montero2023standardized,
  title={A standardized catalogue of spectral indices to advance the use of remote sensing in Earth system research},
  author={Montero, David and Aybar, C{'e}sar and Mahecha, Miguel D and Martinuzzi, Francesco and S{"o}chting, Maximilian and Wieneke, Sebastian},
  journal={Scientific Data},
  volume={10},
  number={1},
  pages={197},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```

## Properties

Each v1 catalogue entry has a case-sensitive lookup key and the following
primary properties. Nested objects contain additional generated and
contributor-provided information. For the complete schema and validation
rules, visit [v1 Explained](https://awesome-spectral-indices.github.io/awesome-spectral-indices/v1.html).

<!-- README-GENERATED:PROPERTIES -->

## Formula expressions

V1 formulas are validated mathematical expressions. Their variables are
classified into broad spectral or thermal bands, exact or selectable-range
hyperspectral inputs, radar polarizations, constants, and external variables.

### Broad spectral and thermal bands

<!-- README-GENERATED:BANDS -->

### Radar polarizations

<!-- README-GENERATED:POLARIZATIONS -->

### Hyperspectral standards

Hyperspectral reflectance operands use integer wavelengths in nanometres.

<!-- README-GENERATED:HYPERSPECTRAL -->

### Supported functions

Only the following function calls are currently accepted in v1 formulas.
Contextual `spatial_*` functions additionally require a matching `reductions`
definition.

<!-- README-GENERATED:FUNCTIONS -->

### Constants

Constant meanings are defined per index rather than globally. The following
table is generated from `output/v1/constants.json` and intentionally shows
only each standard, the indices sharing its description, and that contributed
description.

<!-- README-GENERATED:CONSTANTS -->

### External variables

External variables are formula inputs supplied outside spectral data. Their
descriptions are also specific to each index.

<!-- README-GENERATED:EXTERNAL_VARIABLES -->

# Spectral Indices by Sensing Modality and Application Domain

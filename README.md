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

## Table of Contents

- [Spectral Indices](#spectral-indices)
  - [Citation](#citation)
  - [Properties](#properties)
  - [Formula expressions](#formula-expressions)
    - [Broad spectral and thermal bands](#broad-spectral-and-thermal-bands)
    - [Radar polarizations](#radar-polarizations)
    - [Hyperspectral standards](#hyperspectral-standards)
    - [Supported functions](#supported-functions)
    - [Constants](#constants)
    - [External variables](#external-variables)
- [Spectral Indices by Sensing Modality and Application Domain](#spectral-indices-by-sensing-modality-and-application-domain)
  - [Multispectral](#modality-multispectral)
    - [Vegetation](#multispectral-vegetation)
    - [Water](#multispectral-water)
    - [Burn](#multispectral-burn)
    - [Snow](#multispectral-snow)
    - [Urban](#multispectral-urban)
    - [Soil](#multispectral-soil)
    - [Clouds](#multispectral-clouds)
  - [Multispectral + Thermal](#modality-multispectral-thermal)
    - [Burn](#multispectral-thermal-burn)
    - [Urban](#multispectral-thermal-urban)
    - [Soil](#multispectral-thermal-soil)
  - [Hyperspectral](#modality-hyperspectral)
    - [Vegetation](#hyperspectral-vegetation)
    - [Snow](#hyperspectral-snow)
  - [Radar](#modality-radar)
    - [Vegetation](#radar-vegetation)
    - [Geology](#radar-geology)
- [Download Raw Files](#download-raw-files)
- [Credits](#credits)

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

| Property | Meaning |
| --- | --- |
| `acronym` | Required display acronym; it does not have to be unique. |
| `name` | Required full index name; it does not have to be unique. |
| `formula` | Validated v1 mathematical expression. |
| `classification` | Application domain, generated sensing modalities, and optional families. |
| `bands` | Generated spectral, thermal, and hyperspectral inputs. |
| `polarizations` | Generated radar-polarization inputs. |
| `constants` | Per-index definitions for constants used by the formula. |
| `external_variables` | Per-index definitions for formula inputs supplied outside spectral data. |
| `reductions` | Execution context for contextual reduction functions. |
| `source` | Source link plus generated status, metadata, and citation data. |
| `contributor` | Contributor GitHub profile URL or email address. |
| `date_of_addition` | Catalogue contribution date in YYYY-MM-DD format. |

## Formula expressions

V1 formulas are validated mathematical expressions. Their variables are
classified into broad spectral or thermal bands, exact or selectable-range
hyperspectral inputs, radar polarizations, constants, and external variables.

### Broad spectral and thermal bands

| Standard | Description | Spectral range (nm) | Sentinel-2 | Landsat-89 | Landsat-457 | MODIS |
| --- | --- | --- | --- | --- | --- | --- |
| `A` | Aerosols | 400–455 | `B1` | `B1` | — | — |
| `B` | Blue | 450–530 | `B2` | `B2` | `B1` | `B3` |
| `G` | Green | 510–600 | `B3` | `B3` | `B2` | `B4` |
| `G1` | Green 1 | 510–550 | — | — | — | `B11` |
| `N` | Near-Infrared (NIR) | 760–900 | `B8` | `B5` | `B4` | `B2` |
| `N2` | Near-Infrared (NIR) 2 | 850–880 | `B8A` | — | — | — |
| `R` | Red | 620–690 | `B4` | `B4` | `B3` | `B1` |
| `RE1` | Red Edge 1 | 695–715 | `B5` | — | — | — |
| `RE2` | Red Edge 2 | 730–750 | `B6` | — | — | — |
| `RE3` | Red Edge 3 | 765–795 | `B7` | — | — | — |
| `S1` | Short-wave Infrared (SWIR) 1 | 1550–1750 | `B11` | `B6` | `B5` | `B6` |
| `S2` | Short-wave Infrared (SWIR) 2 | 2080–2350 | `B12` | `B7` | `B7` | `B7` |
| `T` | Thermal Infrared | 10400–12500 | — | — | `B6` | — |
| `T1` | Thermal Infrared 1 | 10600–11190 | — | `B10` | — | — |
| `T2` | Thermal Infrared 2 | 11500–12510 | — | `B11` | — | — |
| `WV` | Water Vapour | 930–960 | `B9` | — | — | — |
| `Y` | Yellow | 585–625 | — | — | — | — |

### Radar polarizations

| Standard | Description |
| --- | --- |
| `HH` | Horizontal transmit, horizontal receive |
| `HV` | Horizontal transmit, vertical receive |
| `VH` | Vertical transmit, horizontal receive |
| `VV` | Vertical transmit, vertical receive |

### Hyperspectral standards

Hyperspectral reflectance operands use integer wavelengths in nanometres.

| Standard | Meaning | Validation |
| --- | --- | --- |
| `R<a>` | Reflectance at the exact integer wavelength `a`. | `300 <= a <= 2500` |
| `R<a>_<b>` | Reflectance at any one wavelength in the inclusive range `a` to `b`. | `300 <= a < b <= 2500` |

### Supported functions

Only the following function calls are currently accepted in v1 formulas.
Contextual `spatial_*` functions additionally require a matching `reductions`
definition.

| Function | Meaning |
| --- | --- |
| `max(X, ...)` | Per-pixel maximum of positional expressions. |
| `min(X, ...)` | Per-pixel minimum of positional expressions. |
| `tanh(X)` | Hyperbolic tangent of one expression. |
| `log(X)` | Natural logarithm of one expression. |
| `kernel(X, Y)` | Kernel evaluation over exactly two input expressions. |
| `spatial_max(X)` | Maximum of an input over the configured spatial scope. |
| `spatial_min(X)` | Minimum of an input over the configured spatial scope. |
| `spatial_mean(X)` | Arithmetic mean of an input over the configured spatial scope. |

### Constants

Constant meanings are defined per index rather than globally. The following
table is generated from `output/v1/constants.json` and intentionally shows
only each standard, the indices sharing its description, and that contributed
description.

| Constant | Indices | Description |
| --- | --- | --- |
| `a` | [NDWIns](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDWIns.html) | Empirical parameter weighting NIR reflectance |
| `alpha` | [BWDRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BWDRVI.html) | NIR reflectance scalar |
| `alpha` | [NDVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVI4RE.html), [RVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RVI4RE.html), [SAVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI4RE.html) | Parameter representing the proportion of Red Edge 3 reflectance (Sentinel-2) |
| `alpha` | [sNIRvNDPI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/sNIRvNDPI.html) | Parameter to mitigate soil and snow effects. Taken from NDPI |
| `alpha` | [NDPI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDPI.html), [WDRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WDRVI.html) | Weighting coefficient |
| `b` | [NDSInw](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSInw.html) | Empirical parameter that offsets the index |
| `beta` | [NDVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVI4RE.html), [RVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RVI4RE.html), [SAVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI4RE.html) | Parameter representing the proportion of Red reflectance (Sentinel-2) |
| `c` | [OCVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OCVI.html) | Correction factor |
| `c` | [EVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI2.html) | Ratio of red to blue reflectances. Red = c * Blue |
| `C1` | [EVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI.html), [EVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI2.html), [kEVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kEVI.html) | Coefficient 1 for the aerosol resistance term |
| `C2` | [EVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI.html), [EVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI2.html), [kEVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kEVI.html) | Coefficient 2 for the aerosol resistance term |
| `epsilon` | [EBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EBI.html) | Adjustment constant |
| `epsilon` | [WCI1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WCI1.html), [WCI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WCI2.html), [WCI3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WCI3.html) | Adjustment constant for numerical stability |
| `eta` | [GRARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GRARI.html) | Mix of green and red reflectances to get properties that are between ARVI and GARI |
| `fdelta` | [SEVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SEVI.html) | Adjustment factor to avoid under-elimination or over-elimination |
| `g` | [EVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI.html), [EVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI2.html), [kEVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kEVI.html) | Gain factor |
| `gamma` | [IAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IAVI.html) | Correction coefficient for upward atmospheric path radiance reaching the satellite |
| `gamma` | [MSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MSAVI.html) | Primary soil line parameter. gamma = N/R (slope of the soil line, only for soil pixels/measurements) |
| `gamma` | [NDTI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDTI4RE.html), [SNDTI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SNDTI4RE.html), [STI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/STI4RE.html) | Weighting coefficient for the ratio SWIR1/SWIR2 (Sentinel-2) |
| `gamma` | [ARVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ARVI.html), [SARVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARVI.html) | Weighting coefficient used for reducing atmospheric effects |
| `k` | [NIRvH2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NIRvH2.html) | Slope parameter by soil. Derived by fitting a linear model on refletances against wavelengths in either the red region (675-681 nm) or the NIR region (778-800 nm) |
| `L` | [SAVISR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVISR.html) | Background Adjustment Factor |
| `L` | [EVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI.html), [EVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI2.html), [GSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GSAVI.html), [IBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IBI.html), [kEVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kEVI.html), [MNLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MNLI.html), [NBUI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBUI.html), [SARVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARVI.html), [SAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI.html), [SAVIT](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVIT.html) | Canopy background adjustment |
| `L` | [SNDTI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SNDTI.html) | Soil adjustment factor |
| `lambdaG` | [DVIplus](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DVIplus.html), [NDGI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDGI.html) | Green central wavelength (nm) |
| `lambdaN` | [DVIplus](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DVIplus.html), [FAI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FAI.html), [FDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FDI.html), [NDGI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDGI.html), [NIRvH2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NIRvH2.html) | NIR central wavelength (nm) |
| `lambdaN2` | [CRSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CRSWIR.html) | NIR2 central wavelength (nm) |
| `lambdaR` | [DVIplus](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DVIplus.html), [FAI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FAI.html), [FDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FDI.html), [NDGI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDGI.html), [NIRvH2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NIRvH2.html) | Red central wavelength (nm) |
| `lambdaS1` | [CRSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CRSWIR.html), [FAI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FAI.html), [FDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FDI.html) | SWIR1 central wavelength (nm) |
| `lambdaS2` | [CRSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CRSWIR.html) | SWIR2 central wavelength (nm) |
| `lmb` | [GARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GARI.html), [GRARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GRARI.html) | Parameter that controls the atmospheric correction |
| `n` | [RWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RWI.html) | Adjustment factor. This constant is calculated as `n = median(G ** (1.0 / 2.71828)) / median(G)`, reducing the spatial dimension (see https://doi.org/10.1109/JSTARS.2025.3562089) |
| `n` | [GDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GDVI.html) | Power operation exponent to amplify the dynamic range |
| `omega` | [MBWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MBWI.html) | Coefficient that maximizes the difference between water and non-water surfaces |
| `sla` | [ATSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ATSAVI.html), [SAVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI2.html), [TSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TSAVI.html) | Soil line slope. N = sla * R + slb (only for soil pixels/measurements) |
| `sla` | [WDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WDVI.html) | Soil line slope. sla = N/R (only for soil pixels/measurements) |
| `slb` | [ATSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ATSAVI.html), [SAVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI2.html), [TSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TSAVI.html) | Soil line intercept.  N = sla * R + slb (only for soil pixels/measurements) |
| `X` | [ATSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ATSAVI.html) | Negative abscissa of a reference point located on the soil line |

### External variables

External variables are formula inputs supplied outside spectral data. Their
descriptions are also specific to each index.

| Variable | Index | Description |
| --- | --- | --- |
| `PAR` | [NIRvP](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NIRvP.html) | Photosynthetically Active Radiation |

# Spectral Indices by Sensing Modality and Application Domain

<a id="modality-multispectral"></a>

## Multispectral

<a id="multispectral-vegetation"></a>

### Vegetation

- [AFRI1600](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/AFRI1600.html): Aerosol Free Vegetation Index (1600 nm)
- [AFRI2100](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/AFRI2100.html): Aerosol Free Vegetation Index (2100 nm)
- [ARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ARI.html): Anthocyanin Reflectance Index
- [ARI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ARI2.html): Anthocyanin Reflectance Index 2
- [ARVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ARVI.html): Atmospherically Resistant Vegetation Index
- [AshburnVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/AshburnVI.html): Ashburn Vegetation Index
- [ATSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ATSAVI.html): Adjusted Transformed Soil-Adjusted Vegetation Index
- [AVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/AVI.html): Advanced Vegetation Index
- [BCC](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BCC.html): Blue Chromatic Coordinate
- [BNDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BNDVI.html): Blue Normalized Difference Vegetation Index
- [bNIRv](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/bNIRv.html): Blue Near-Infrared Reflectance of Vegetation
- [BWDRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BWDRVI.html): Blue Wide Dynamic Range Vegetation Index
- [CCI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CCI.html): Chlorophyll Carotenoid Index
- [CIG](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CIG.html): Chlorophyll Index Green
- [CIRE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CIRE.html): Chlorophyll Index Red Edge
- [CRSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CRSWIR.html): Continuum Removal SWIR
- [CVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CVI.html): Chlorophyll Vegetation Index
- [DSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DSI.html): Drought Stress Index
- [DSWI1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DSWI1.html): Disease-Water Stress Index 1
- [DSWI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DSWI2.html): Disease-Water Stress Index 2
- [DSWI3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DSWI3.html): Disease-Water Stress Index 3
- [DSWI4](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DSWI4.html): Disease-Water Stress Index 4
- [DSWI5](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DSWI5.html): Disease-Water Stress Index 5
- [DVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DVI.html): Difference Vegetation Index
- [DVIplus](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DVIplus.html): Difference Vegetation Index Plus
- [EBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EBI.html): Enhanced Bloom Index
- [ENDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ENDVI.html): Enhanced Normalized Difference Vegetation Index
- [EVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI.html): Enhanced Vegetation Index
- [EVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVI2.html): Two-Band Enhanced Vegetation Index
- [EVIv](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EVIv.html): Enhanced Vegetation Index of Vegetation
- [ExG](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ExG.html): Excess Green Index
- [ExGR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ExGR.html): ExG - ExR Vegetation Index
- [ExR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ExR.html): Excess Red Index
- [FCVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FCVI.html): Fluorescence Correction Vegetation Index
- [GARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GARI.html): Green Atmospherically Resistant Vegetation Index
- [GBNDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GBNDVI.html): Green-Blue Normalized Difference Vegetation Index
- [GCC](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GCC.html): Green Chromatic Coordinate
- [GDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GDVI.html): Generalized Difference Vegetation Index
- [GEMI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GEMI.html): Global Environment Monitoring Index
- [GLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GLI.html): Green Leaf Index
- [GM1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GM1.html): Gitelson and Merzlyak Index 1
- [GM2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GM2.html): Gitelson and Merzlyak Index 2
- [GNDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GNDVI.html): Green Normalized Difference Vegetation Index
- [GOSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GOSAVI.html): Green Optimized Soil Adjusted Vegetation Index
- [GRARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GRARI.html): Atmospheric Resistant Green-Red Index
- [GreenDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GreenDVI.html): Green Difference Vegetation Index
- [GRNDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GRNDVI.html): Green-Red Normalized Difference Vegetation Index
- [GRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GRVI.html): Green Ratio Vegetation Index
- [GSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GSAVI.html): Green Soil Adjusted Vegetation Index
- [GVMI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/GVMI.html): Global Vegetation Moisture Index
- [IAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IAVI.html): New Atmospherically Resistant Vegetation Index
- [IKAW](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IKAW.html): Kawashima Index
- [IPVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IPVI.html): Infrared Percentage Vegetation Index
- [IRECI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IRECI.html): Inverted Red-Edge Chlorophyll Index
- [IRGBVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IRGBVI.html): Improved-Red-Green-Blue Vegetation Index
- [KDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/KDI.html): Kochia Detection Index
- [kEVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kEVI.html): Kernel Enhanced Vegetation Index
- [kIPVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kIPVI.html): Kernel Infrared Percentage Vegetation Index
- [kNDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kNDVI.html): Kernel Normalized Difference Vegetation Index
- [kRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kRVI.html): Kernel Ratio Vegetation Index
- [kVARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/kVARI.html): Kernel Visible Atmospherically Resistant Index
- [MCARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MCARI.html): Modified Chlorophyll Absorption in Reflectance Index
- [MCARI1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MCARI1.html): Modified Chlorophyll Absorption in Reflectance Index 1
- [MCARI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MCARI2.html): Modified Chlorophyll Absorption in Reflectance Index 2
- [MCARI705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MCARI705.html): Modified Chlorophyll Absorption in Reflectance Index (705 and 750 nm)
- [MCARIOSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MCARIOSAVI.html): MCARI/OSAVI Ratio
- [MCARIOSAVI705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MCARIOSAVI705.html): MCARI/OSAVI Ratio (705 and 750 nm)
- [MGRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MGRVI.html): Modified Green Red Vegetation Index
- [MI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MI.html): Mangrove Index
- [mND705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/mND705.html): Modified Normalized Difference (705, 750 and 445 nm)
- [MNDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MNDVI.html): Modified Normalized Difference Vegetation Index
- [MNLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MNLI.html): Modified Non-Linear Vegetation Index
- [MRBVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MRBVI.html): Modified Red Blue Vegetation Index
- [MSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MSAVI.html): Modified Soil-Adjusted Vegetation Index
- [MSAVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MSAVI2.html): Modified Soil-Adjusted Vegetation Index 2
- [MSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MSI.html): Moisture Stress Index
- [MSR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MSR.html): Modified Simple Ratio
- [MSR705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MSR705-ratio.html): Modified Simple Ratio (705 and 750 nm)
- [mSR705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/mSR705-modified.html): Modified Simple Ratio (705 and 445 nm)
- [MTCI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MTCI.html): MERIS Terrestrial Chlorophyll Index
- [MTVI1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MTVI1.html): Modified Triangular Vegetation Index 1
- [MTVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MTVI2.html): Modified Triangular Vegetation Index 2
- [MVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MVI.html): Mangrove Vegetation Index
- [ND705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ND705.html): Normalized Difference (705 and 750 nm)
- [NDDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDDI.html): Normalized Difference Drought Index
- [NDGI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDGI.html): Normalized Difference Greenness Index
- [NDII](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDII.html): Normalized Difference Infrared Index
- [NDMI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDMI.html): Normalized Difference Moisture Index
- [NDPI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDPI.html): Normalized Difference Phenology Index
- [NDREI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDREI.html): Normalized Difference Red Edge Index
- [NDTI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDTI4RE.html): 4-band Red Edge Normalized Difference Tillage Index
- [NDTillI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDTillI.html): Normalized Difference Tillage Index
- [NDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVI.html): Normalized Difference Vegetation Index
- [NDVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVI4RE.html): 4-band Red Edge Normalized Difference Vegetation Index
- [NDVI705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVI705.html): Normalized Difference Vegetation Index (705 and 750 nm)
- [NDVISR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVISR.html): Normalized Difference Vegetation Index with Simple Ratio
- [NDYI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDYI.html): Normalized Difference Yellowness Index
- [NGRDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NGRDI.html): Normalized Green Red Difference Index
- [NIRv](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NIRv.html): Near-Infrared Reflectance of Vegetation
- [NIRvH2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NIRvH2.html): Hyperspectral Near-Infrared Reflectance of Vegetation
- [NIRvP](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NIRvP.html): Near-Infrared Reflectance of Vegetation and Incoming PAR
- [NLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NLI.html): Non-Linear Vegetation Index
- [NMDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NMDI.html): Normalized Multi-band Drought Index
- [NormG](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NormG.html): Normalized Green
- [NormNIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NormNIR.html): Normalized NIR
- [NormR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NormR.html): Normalized Red
- [NPCI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NPCI.html): Normalized Pigments Chlorophyll Ratio Index
- [NRFIg](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NRFIg.html): Normalized Rapeseed Flowering Index Green
- [NRFIr](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NRFIr.html): Normalized Rapeseed Flowering Index Red
- [OCVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OCVI.html): Optimized Chlorophyll Vegetation Index
- [OSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OSAVI.html): Optimized Soil-Adjusted Vegetation Index
- [RCC](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RCC.html): Red Chromatic Coordinate
- [RDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RDVI.html): Renormalized Difference Vegetation Index
- [REDSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/REDSI.html): Red-Edge Disease Stress Index
- [RENDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RENDVI.html): Red Edge Normalized Difference Vegetation Index
- [RGBVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RGBVI.html): Red Green Blue Vegetation Index
- [RGRI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RGRI.html): Red-Green Ratio Index
- [RI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RI.html): Redness Index
- [RVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RVI.html): Ratio Vegetation Index
- [RVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RVI4RE.html): 4-band Red Edge Ratio Vegetation Index
- [S2REP](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/S2REP.html): Sentinel-2 Red-Edge Position
- [SARVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARVI.html): Soil Adjusted and Atmospherically Resistant Vegetation Index
- [SAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI.html): Soil-Adjusted Vegetation Index
- [SAVI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI2.html): Soil-Adjusted Vegetation Index 2
- [SAVI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVI4RE.html): 4-band Red Edge Soil Adjusted Vegetation Index
- [SAVISR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVISR.html): Soil-Adjusted Vegetation Index with Simple Ratio
- [SeLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SeLI.html): Sentinel-2 LAI Green Index
- [SEVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SEVI.html): Shadow-Eliminated Vegetation Index
- [SI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SI.html): Shadow Index
- [SIPI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SIPI.html): Structure Insensitive Pigment Index
- [SLAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SLAVI.html): Specific Leaf Area Vegetation Index
- [SNDTI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SNDTI.html): Soil-Adjusted Normalized Difference Tillage Index
- [SNDTI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SNDTI4RE.html): 4-band Red Edge Soil-Adjusted Normalized Difference Tillage Index
- [sNIRvLSWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/sNIRvLSWI.html): SWIR-enhanced Near-Infrared Reflectance of Vegetation for LSWI
- [sNIRvNDPI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/sNIRvNDPI.html): SWIR-enhanced Near-Infrared Reflectance of Vegetation for NDPI
- [sNIRvNDVILSWIP](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/sNIRvNDVILSWIP.html): SWIR-enhanced Near-Infrared Reflectance of Vegetation for the NDVI-LSWI Product
- [sNIRvNDVILSWIS](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/sNIRvNDVILSWIS.html): SWIR-enhanced Near-Infrared Reflectance of Vegetation for the NDVI-LSWI Sum
- [sNIRvSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/sNIRvSWIR.html): SWIR-enhanced Near-Infrared Reflectance of Vegetation
- [SR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SR.html): Simple Ratio
- [SR2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SR2.html): Simple Ratio (800 and 550 nm)
- [SR555](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SR555.html): Simple Ratio (555 and 750 nm)
- [SR705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SR705.html): Simple Ratio (705 and 750 nm)
- [SRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SRVI.html): Symbolic Regression Vegetation Index
- [STI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/STI.html): Simple Tillage Index
- [STI4RE](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/STI4RE.html): 4-band Red Edge Soil Tillage Index
- [TCARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TCARI.html): Transformed Chlorophyll Absorption in Reflectance Index
- [TCARIOSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TCARIOSAVI.html): TCARI/OSAVI Ratio
- [TCARIOSAVI705](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TCARIOSAVI705.html): TCARI/OSAVI Ratio (705 and 750 nm)
- [TCI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TCI.html): Triangular Chlorophyll Index
- [TDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TDVI.html): Transformed Difference Vegetation Index
- [TGI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TGI.html): Triangular Greenness Index
- [TMTCbrightness](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TMTCbrightness.html): Thematic Mapper Tasseled Cap Brightness Feature
- [TMTCfifth](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TMTCfifth.html): Thematic Mapper Tasseled Cap Fifth Feature
- [TMTCfourth](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TMTCfourth.html): Thematic Mapper Tasseled Cap Fourth Feature
- [TMTCgreenness](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TMTCgreenness.html): Thematic Mapper Tasseled Cap Greenness Feature
- [TMTCsixth](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TMTCsixth.html): Thematic Mapper Tasseled Cap Sixth Feature
- [TMTCwetness](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TMTCwetness.html): Thematic Mapper Tasseled Cap Wetness Feature
- [TriVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TriVI.html): Triangular Vegetation Index
- [TRRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TRRVI.html): Transformed Red Range Vegetation Index
- [TSAVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TSAVI.html): Transformed Soil-Adjusted Vegetation Index
- [TTVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TTVI.html): Transformed Triangular Vegetation Index
- [TVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TVI.html): Transformed Vegetation Index
- [VARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VARI.html): Visible Atmospherically Resistant Index
- [VARI700](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VARI700.html): Visible Atmospherically Resistant Index (700 nm)
- [VI700](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VI700.html): Vegetation Index (700 nm)
- [VIG](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VIG.html): Vegetation Index Green
- [WCI1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WCI1.html): Wheat Canopy Index (Growth Stage 1)
- [WCI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WCI2.html): Wheat Canopy Index (Growth Stage 2)
- [WCI3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WCI3.html): Wheat Canopy Index (Growth Stage 3)
- [WDRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WDRVI.html): Wide Dynamic Range Vegetation Index
- [WDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WDVI.html): Weighted Difference Vegetation Index

<a id="multispectral-water"></a>

### Water

- [ANDWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/ANDWI.html): Augmented Normalized Difference Water Index
- [AWEInsh](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/AWEInsh.html): Automated Water Extraction Index
- [AWEIsh](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/AWEIsh.html): Automated Water Extraction Index with Shadows Elimination
- [CWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CWI.html): Coastal Water Index
- [FAI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FAI.html): Floating Algae Index
- [FDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FDI.html): Floating Debris Index
- [FWEI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/FWEI.html): Flood/Water Extraction Index
- [LSWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/LSWI.html): Land Surface Water Index
- [MBWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MBWI.html): Multi-Band Water Index
- [MLSWI26](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MLSWI26.html): Modified Land Surface Water Index (MODIS Bands 2 and 6)
- [MLSWI27](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MLSWI27.html): Modified Land Surface Water Index (MODIS Bands 2 and 7)
- [MNDWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MNDWI.html): Modified Normalized Difference Water Index
- [MuWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MuWIR.html): Revised Multi-Spectral Water Index
- [NDCI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDCI.html): Normalized Difference Chlorophyll Index
- [NDPonI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDPonI.html): Normalized Difference Pond Index
- [NDTI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDTI.html): Normalized Difference Turbidity Index
- [NDVIMNDWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVIMNDWI.html): NDVI-MNDWI Model
- [NDWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDWI.html): Normalized Difference Water Index
- [NDWIns](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDWIns.html): Normalized Difference Water Index with no Snow Cover and Glaciers
- [NWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NWI.html): New Water Index
- [OSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OSI.html): Oil Spill Index
- [PI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PI.html): Plastic Index
- [RNDVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RNDVI.html): Reversed Normalized Difference Vegetation Index
- [RWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RWI.html): Rescaled Water Index
- [S2WI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/S2WI.html): Sentinel-2 Water Index
- [SCoWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SCoWI.html): Subtractive Coastal Water Index
- [SRWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SRWI.html): Symbolic Regression Water Index
- [SWM](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SWM.html): Sentinel Water Mask
- [TWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/TWI.html): Triangle Water Index
- [WI1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WI1.html): Water Index 1
- [WI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WI2.html): Water Index 2
- [WI2015](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WI2015.html): Water Index 2015
- [WRI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/WRI.html): Water Ratio Index

<a id="multispectral-burn"></a>

### Burn

- [BAI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BAI-burn.html): Burned Area Index
- [BAIM](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BAIM.html): Burned Area Index adapted to MODIS
- [BAIS2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BAIS2.html): Burned Area Index for Sentinel 2
- [CSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CSI.html): Char Soil Index
- [MIRBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MIRBI.html): Mid-Infrared Burn Index
- [NBR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBR.html): Normalized Burn Ratio
- [NBR2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBR2.html): Normalized Burn Ratio 2
- [NBRplus](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBRplus.html): Normalized Burn Ratio Plus
- [NBRSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBRSWIR.html): Normalized Burn Ratio SWIR
- [NDSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSWIR.html): Normalized Difference SWIR

<a id="multispectral-snow"></a>

### Snow

- [NBSIMS](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBSIMS.html): Non-Binary Snow Index for Multi-Component Surfaces
- [NDGlaI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDGlaI.html): Normalized Difference Glacier Index
- [NDSaII](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSaII.html): Normalized Difference Snow and Ice Index
- [NDSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSI.html): Normalized Difference Snow Index
- [NDSII](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSII.html): Normalized Difference Snow Ice Index
- [NDSIITM](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSIITM.html): Normalized Difference Snow/Ice Index for Landsat TM
- [NDSInw](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSInw.html): Normalized Difference Snow Index with no Water
- [S3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/S3.html): S3 Snow Index
- [SWI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SWI.html): Snow Water Index

<a id="multispectral-urban"></a>

### Urban

- [BLFEI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BLFEI.html): Built-Up Land Features Extraction Index
- [BRBA](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BRBA.html): Band Ratio for Built-up Area
- [IBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/IBI.html): Index-Based Built-Up Index
- [NBAI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBAI.html): Normalized Built-up Area Index
- [NDBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDBI.html): Normalized Difference Built-Up Index
- [NHFD](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NHFD.html): Non-Homogeneous Feature Difference
- [PISI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PISI.html): Perpendicular Impervious Surface Index
- [SUI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SUI.html): Sealed Urban Index
- [UI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/UI.html): Urban Index
- [VgNIRBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VgNIRBI.html): Visible Green-Based Built-Up Index
- [VIBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VIBI.html): Vegetation Index Built-up Index
- [VrNIRBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VrNIRBI.html): Visible Red-Based Built-Up Index

<a id="multispectral-soil"></a>

### Soil

- [BaI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BaI-soil.html): Bareness Index
- [BI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BI.html): Bare Soil Index
- [BITM](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BITM.html): Landsat TM-based Brightness Index
- [BIXS](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/BIXS.html): SPOT HRV XS-based Brightness Index
- [DBSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DBSI.html): Dry Bareness Index
- [EMBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EMBI.html): Enhanced Modified Bare Soil Index
- [MBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/MBI.html): Modified Bare Soil Index
- [NDSIWV](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSIWV.html): WorldView Normalized Difference Soil Index
- [NDSoI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDSoI.html): Normalized Difference Soil Index
- [NSDS](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NSDS.html): Normalized Shortwave Infrared Difference Soil-Moisture
- [NSDSI1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NSDSI1.html): Normalized Shortwave-Infrared Difference Bare Soil Moisture Index 1
- [NSDSI2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NSDSI2.html): Normalized Shortwave-Infrared Difference Bare Soil Moisture Index 2
- [NSDSI3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NSDSI3.html): Normalized Shortwave-Infrared Difference Bare Soil Moisture Index 3
- [RI4XS](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RI4XS.html): SPOT HRV XS-based Redness Index 4

<a id="multispectral-clouds"></a>

### Clouds

- [CI1SWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CI1SWIR.html): Cloud Index Form 1 with SWIR 1
- [CI1woSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CI1woSWIR.html): Cloud Index Form 1 without SWIR bands
- [CI2SWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CI2SWIR.html): Cloud Index Form 2 with SWIR bands
- [CI2woSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CI2woSWIR.html): Cloud Index Form 2 without SWIR bands
- [CLOSDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CLOSDI.html): Cloud Shadow Detection Index
- [CSISWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CSISWIR.html): Cloud Shadow Index with SWIR 1
- [CSIwoSWIR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CSIwoSWIR.html): Cloud Shadow Index without SWIR bands

<a id="modality-multispectral-thermal"></a>

## Multispectral + Thermal

<a id="multispectral-thermal-burn"></a>

### Burn

- [CSIT](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CSIT.html): Char Soil Index Thermal
- [NBRT1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBRT1.html): Normalized Burn Ratio Thermal 1
- [NBRT2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBRT2.html): Normalized Burn Ratio Thermal 2
- [NBRT3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBRT3.html): Normalized Burn Ratio Thermal 3
- [NDVIT](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDVIT.html): Normalized Difference Vegetation Index Thermal
- [NSTv1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NSTv1.html): NIR-SWIR-Temperature Version 1
- [NSTv2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NSTv2.html): NIR-SWIR-Temperature Version 2
- [SAVIT](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SAVIT.html): Soil-Adjusted Vegetation Index Thermal
- [VI6T](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VI6T.html): VI6T Index

<a id="multispectral-thermal-urban"></a>

### Urban

- [DBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DBI.html): Dry Built-Up Index
- [EBBI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/EBBI.html): Enhanced Built-Up and Bareness Index
- [NBUI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBUI.html): New Built-Up Index
- [NDISIb](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDISIb.html): Normalized Difference Impervious Surface Index Blue
- [NDISIg](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDISIg.html): Normalized Difference Impervious Surface Index Green
- [NDISImndwi](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDISImndwi.html): Normalized Difference Impervious Surface Index with MNDWI
- [NDISIndwi](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDISIndwi.html): Normalized Difference Impervious Surface Index with NDWI
- [NDISIr](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDISIr.html): Normalized Difference Impervious Surface Index Red

<a id="multispectral-thermal-soil"></a>

### Soil

- [NBLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBLI.html): Normalized Difference Bare Land Index
- [NBLIOLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NBLIOLI.html): Normalized Difference Bare Land Index for Landsat-OLI
- [NDBaI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDBaI.html): Normalized Difference Bareness Index

<a id="modality-hyperspectral"></a>

## Hyperspectral

<a id="hyperspectral-vegetation"></a>

### Vegetation

- [CARI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CARI.html): Carotenoid Index
- [CCRI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CCRI.html): Carotenoid-Chlorophyll Ratio Index
- [CRI550](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CRI550.html): Carotenoid Reflectance Index at 550 nm
- [CRI700](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/CRI700.html): Carotenoid Reflectance Index at 700 nm
- [LCI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/LCI.html): Leaf Chlorophyll Index
- [NDLI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDLI.html): Normalized Difference Lignin Index
- [NDNI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDNI.html): Normalized Difference Nitrogen Index
- [OPSNDa](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OPSNDa.html): Optimized Pigment Specific Normalized Difference for Chlorophyll a
- [OPSNDb](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OPSNDb.html): Optimized Pigment Specific Normalized Difference for Chlorophyll b
- [OPSNDc](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OPSNDc.html): Optimized Pigment Specific Normalized Difference for Carotenoids
- [OPSSRa](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OPSSRa.html): Optimized Pigment Specific Simple Ratio for Chlorophyll a
- [OPSSRb](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OPSSRb.html): Optimized Pigment Specific Simple Ratio for Chlorophyll b
- [OPSSRc](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/OPSSRc.html): Optimized Pigment Specific Simple Ratio for Carotenoids
- [PRI550](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PRI550.html): Physiological Reflectance Index at 550 nm
- [PRI570](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PRI570.html): Physiological Reflectance Index at 570 nm
- [PRIm1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PRIm1.html): Modified Photochemical Reflectance Index 1
- [PRIm4](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PRIm4.html): Modified Photochemical Reflectance Index 4
- [PSNDa](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PSNDa.html): Pigment Specific Normalized Difference for Chlorophyll a
- [PSNDb](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PSNDb.html): Pigment Specific Normalized Difference for Chlorophyll b
- [PSNDc](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PSNDc.html): Pigment Specific Normalized Difference for Carotenoids
- [PSRI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PSRI.html): Plant Senescence Reflectance Index
- [PSSRa](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PSSRa.html): Pigment Specific Simple Ratio for Chlorophyll a
- [PSSRb](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PSSRb.html): Pigment Specific Simple Ratio for Chlorophyll b
- [PSSRc](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/PSSRc.html): Pigment Specific Simple Ratio for Carotenoids
- [RARSa](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RARSa.html): Ratio Analysis of Reflectance Spectra for Chlorophyll a
- [RARSb](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RARSb.html): Ratio Analysis of Reflectance Spectra for Chlorophyll b
- [RARSc](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RARSc.html): Ratio Analysis of Reflectance Spectra for Carotenoids
- [RVSI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RVSI.html): Red-edge Vegetation Stress Index
- [SARBR1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARBR1.html): Scatter-Adjusted Reflectance Band Ratio 1
- [SARBR2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARBR2.html): Scatter-Adjusted Reflectance Band Ratio 2
- [SARBR3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARBR3.html): Scatter-Adjusted Reflectance Band Ratio 3
- [SARBR4](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARBR4.html): Scatter-Adjusted Reflectance Band Ratio 4
- [SARBR5](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/SARBR5.html): Scatter-Adjusted Reflectance Band Ratio 5
- [URBR1](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/URBR1.html): Untransformed Reflectance Band Ratio 1
- [URBR2](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/URBR2.html): Untransformed Reflectance Band Ratio 2
- [URBR3](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/URBR3.html): Untransformed Reflectance Band Ratio 3
- [URBR4](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/URBR4.html): Untransformed Reflectance Band Ratio 4
- [URBR5](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/URBR5.html): Untransformed Reflectance Band Ratio 5

<a id="hyperspectral-snow"></a>

### Snow

- [NDISI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDISI.html): Normalized Difference Ice-Snow Index

<a id="modality-radar"></a>

## Radar

<a id="radar-vegetation"></a>

### Vegetation

- [DPDD](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DPDD.html): Dual-Pol Diagonal Distance
- [DpRVIHH](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DpRVIHH.html): Dual-Polarized Radar Vegetation Index HH
- [DpRVIVV](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/DpRVIVV.html): Dual-Polarized Radar Vegetation Index VV
- [QpRVI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/QpRVI.html): Quad-Polarized Radar Vegetation Index
- [RFDI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/RFDI.html): Radar Forest Degradation Index
- [VDDPI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VDDPI.html): Vertical Dual De-Polarization Index
- [VHVVD](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VHVVD.html): VH-VV Difference
- [VHVVP](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VHVVP.html): VH-VV Product
- [VHVVR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VHVVR.html): VH-VV Ratio
- [VVVHD](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VVVHD.html): VV-VH Difference
- [VVVHR](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VVVHR.html): VV-VH Ratio
- [VVVHS](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/VVVHS.html): VV-VH Sum

<a id="radar-geology"></a>

### Geology

- [NDPolI](https://awesome-spectral-indices.github.io/awesome-spectral-indices/indices/NDPolI.html): Normalized Difference Polarization Index

# Download Raw Files

You can download or clone the repository:

```
git clone https://github.com/awesome-spectral-indices/awesome-spectral-indices.git
```

Or you can download the single files here (right-click > Save link as...):

- JSON: [Raw v1 catalogue](https://raw.githubusercontent.com/awesome-spectral-indices/awesome-spectral-indices/main/output/v1/spectral-indices-dict.json)
- CSV: [Raw v1 table](https://raw.githubusercontent.com/awesome-spectral-indices/awesome-spectral-indices/main/output/v1/spectral-indices-table.csv)

# Credits

- [César Aybar](https://github.com/csaybar): The formidable [pydantic](https://github.com/samuelcolvin/pydantic/) expert and creator of [rgee](https://github.com/r-spatial/rgee).

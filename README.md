<p align="center">
  <a href="https://github.com/davemlz/awesome-spectral-indices"><img src="https://raw.githubusercontent.com/davemlz/awesome-spectral-indices/main/docs/_static/asi.png" alt="Awesome Spectral Indices"></a>
</p>
<p align="center">
    <em>A ready-to-use curated list of Spectral Indices for Remote Sensing applications.</em>
</p>
<p align="center">
<a href="https://github.com/sindresorhus/awesome" target="_blank">
    <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome">
</a>
<a href="https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-dict.json" target="_blank">
    <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/davemlz/5e9f08fa6a45d9d486e29d9d85ad5c84/raw/spectral.json" alt="Awesome Spectral Indices">
</a>
<a href="https://share.streamlit.io/davemlz/espectro/main/espectro.py" target="_blank">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Streamlit">
</a>
<a href="https://github.com/davemlz/awesome-ee-spectral-indices/actions/workflows/tests.yml" target="_blank">
    <img src="https://github.com/davemlz/awesome-ee-spectral-indices/actions/workflows/tests.yml/badge.svg" alt="Tests">
</a>
<a href="https://awesome-ee-spectral-indices.readthedocs.io/en/latest/?badge=latest" target="_blank">
    <img src="https://readthedocs.org/projects/awesome-ee-spectral-indices/badge/?version=latest" alt="Documentation">
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

**GitHub**: <a href="https://github.com/davemlz/awesome-ee-spectral-indices" target="_blank">github.com/davemlz/awesome-ee-spectral-indices</a>

**Documentation**: <a href="https://awesome-ee-spectral-indices.readthedocs.io/" target="_blank">awesome-ee-spectral-indices.readthedocs.io</a>

**Python Package**: <a href="https://github.com/davemlz/spyndex" target="_blank">github.com/davemlz/spyndex</a>

**Streamlit App**: <a href="https://github.com/davemlz/espectro" target="_blank">github.com/davemlz/espectro</a>

**Google Earth Engine**: <a href="https://github.com/davemlz/eemont" target="_blank">github.com/davemlz/eemont</a> (Python), <a href="https://github.com/davemlz/spectral" target="_blank">github.com/davemlz/spectral</a> (JavaScript) and <a href="https://github.com/r-earthengine/rgeeExtra" target="_blank">github.com/r-earthengine/rgeeExtra</a> (R)

---

# Spectral Indices

Spectral Indices are widely used in the Remote Sensing community. This repository keeps track of classical as well as novel spectral indices for different Remote Sensing applications. All spectral indices in the repository are curated and can be used in different environments and programming languages. 
You can check the [curated list of spectral indices here](https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-table.csv), and if you want to use it in your environment, it is available in [CSV](https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-table.csv) and [JSON](https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-dict.json).

## Attributes

All spectral indices follow a standard. Each item of the list has the following attributes:

- `short_name`: Short name of the index (e.g. `"NDWI"`).
- `long_name`: Long name of the index (e.g. `"Normalized Difference Water Index"`).
- `formula`: Expression/formula of the index (e.g. `"(G - N)/(G + N)"`).
- `bands`: List of required bands/parameters for the index computation (e.g. `["N","G"]`).
- `reference`: Link to the index reference/paper/doi (e.g. `"https://doi.org/10.1080/01431169608948714"`).
- `type`: Type/application of the index (e.g. `"water"`).
- `date_of_addition`: Date of addition to the list (e.g. `"2021-04-07"`).
- `contributor`: GitHub user link of the contributor (e.g. `"https://github.com/davemlz"`).

## Expressions

The formula of the index is presented as a string/expression (e.g. `"(N - R)/(N + R)"`) that can be easily evaluated. The parameters used in the expression for each index follow this standard:

<table>

<tr>

<th> Description </th>
<th> Standard </th>
<th> Sentinel-1 </th>
<th> Sentinel-2 </th>
<th> Landsat-89 </th>
<th> Landsat-457 </th>
<th> MODIS </th>

</tr>

<tr>

<td>Aerosols</td>
<td>A</td>
<td></td>
<td>B1</td>
<td>B1</td>
<td></td>
<td></td>

</tr>

<tr>

<td>Blue</td>
<td>B</td>
<td></td>
<td>B2</td>
<td>B2</td>
<td>B1</td>
<td>B3</td>

</tr>

<tr>

<td>Green</td>
<td>G</td>
<td></td>
<td>B3</td>
<td>B3</td>
<td>B2</td>
<td>B4</td>

</tr>

<tr>

<td>Red</td>
<td>R</td>
<td></td>
<td>B4</td>
<td>B4</td>
<td>B3</td>
<td>B1</td>

</tr>

<tr>

<td>Red Edge 1</td>
<td>RE1</td>
<td></td>
<td>B5</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Red Edge 2</td>
<td>RE2</td>
<td></td>
<td>B6</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Red Edge 3</td>
<td>RE3</td>
<td></td>
<td>B7</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>NIR</td>
<td>N</td>
<td></td>
<td>B8</td>
<td>B5</td>
<td>B4</td>
<td>B2</td>

</tr>

<tr>

<td>NIR 2</td>
<td>N2</td>
<td></td>
<td>B8A</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>SWIR 1</td>
<td>S1</td>
<td></td>
<td>B11</td>
<td>B6</td>
<td>B5</td>
<td>B6</td>

</tr>

<tr>

<td>SWIR 2</td>
<td>S2</td>
<td></td>
<td>B12</td>
<td>B7</td>
<td>B7</td>
<td>B7</td>

</tr>

<tr>

<td>Thermal 1</td>
<td>T1</td>
<td></td>
<td></td>
<td>B10</td>
<td>B6</td>
<td></td>

</tr>

<tr>

<td>Thermal 2</td>
<td>T2</td>
<td></td>
<td></td>
<td>B11</td>
<td></td>
<td></td>

</tr>

<tr>

<td>Backscattering Coefficient HV</td>
<td>HV</td>
<td>HV</td>
<td></td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Backscattering Coefficient VH</td>
<td>VH</td>
<td>VH</td>
<td></td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Backscattering Coefficient HH</td>
<td>HH</td>
<td>HH</td>
<td></td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Backscattering Coefficient VV</td>
<td>VV</td>
<td>VV</td>
<td></td>
<td></td>
<td></td>
<td></td>

</tr>

</table>

Additional index parameters also follow a standard:

- `g`: Gain factor (e.g. Used for EVI).
- `L`: Canopy background adjustment (e.g. Used for SAVI and EVI).
- `C1`: Coefficient 1 for the aerosol resistance term (e.g. Used for EVI).
- `C2`: Coefficient 2 for the aerosol resistance term (e.g. Used for EVI).
- `cexp`: Exponent used for OCVI.
- `nexp`: Exponent used for GDVI.
- `alpha`: Weighting coefficient used for WDRVI, BWDRVI and NDPI.
- `beta`: Calibration parameter used for NDSIns.
- `gamma`: Weighting coefficient used for ARVI.
- `omega`: Weighting coefficient used for MBWI.
- `sla`: Soil line slope.
- `slb`: Soil line intercept.
- `PAR`: Photosynthetically Active Radiation.
- `k`: Slope parameter by soil used for NIRvH2.
- `lambdaN`: NIR wavelength used for NIRvH2 and NDGI.
- `lambdaR`: Red wavelength used for NIRvH2 and NDGI.
- `lambdaG`: Green wavelength used for NDGI.

The kernel indices are constructed using a special type of parameters:

- `kAB`: Kernel of bands/parameters `A` and `B` (e.g. `kNR` means `k(N,R)`, where `k` is the kernel function).
- `p`: Kernel degree (used for the polynomial kernel).
- `c`: Free parameter that trades off the influence of higher-order versus lower-order terms (used for the polynomial kernel).

# Call for Indices! :rotating_light:

Researchers that have published (or aim to publish) their novel spectral indices are encouraged to add them to this repository! The list of spectral indices is used as a source for different resources that allow spectral indices computation in different environments (such as Python and Google Earth Engine). To add an index, please follow the [Contribution Guidelines](https://awesome-ee-spectral-indices.readthedocs.io/en/latest/contributing.html).

In the same line, if you know an spectral index that is not included in this repository, you are encouraged to add it! Please follow the [Contribution Guidelines](https://awesome-ee-spectral-indices.readthedocs.io/en/latest/contributing.html) in order to add it.

And one more thing: If you see an error in one or several indices, please report it or update the index (indices) by following the [Contribution Guidelines](https://awesome-ee-spectral-indices.readthedocs.io/en/latest/contributing.html)!

There is no deadline. The repository is continuously updated!

# Used by

## JavaScript

- [spectral](https://github.com/davemlz/spectral): Awesome Spectral Indices for the Google Earth Engine JavaScript API (Code Editor).

## Python

- [eemont](https://github.com/davemlz/eemont): A Python package that extends Google Earth Engine.
- [eeExtra](https://github.com/r-earthengine/ee_extra): A Python package that unifies the Google Earth Engine ecosystem.
- [Espectro](https://github.com/davemlz/espectro): The Awesome Spectral Indices Streamlit App.
- [spyndex](https://github.com/davemlz/spyndex): Awesome Spectral Indices in Python.

## R

- [rgeeExtra](https://github.com/r-earthengine/rgeeExtra): High-level functions to process spatial and simple Earth Engine objects.

# Spectral Indices by Type

## Vegetation

### A
<table><tr><td>[AFRI1600](https://doi.org/10.1016/S0034-4257(01)00190-0): Aerosol Free Vegetation Index (1600 nm).</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[AFRI2100](https://doi.org/10.1016/S0034-4257(01)00190-0): Aerosol Free Vegetation Index (2100 nm).</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[ARI](https://doi.org/10.1562/0031-8655(2001)074%3C0038:OPANEO%3E2.0.CO;2): Anthocyanin Reflectance Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[ARI2](https://doi.org/10.1562/0031-8655(2001)074%3C0038:OPANEO%3E2.0.CO;2): Anthocyanin Reflectance Index 2.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[ARVI](https://doi.org/10.1109/36.134076): Atmospherically Resistant Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[ATSAVI](https://doi.org/10.1016/0034-4257(91)90009-U): Adjusted Transformed Soil-Adjusted Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[AVI](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.8749&rep=rep1&type=pdf): Advanced Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### B
<table><tr><td>[BCC](https://doi.org/10.1016/0034-4257(87)90088-5): Blue Chromatic Coordinate.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[BNDVI](https://doi.org/10.1016/S1672-6308(07)60027-4): Blue Normalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[BWDRVI](https://doi.org/10.2135/cropsci2007.01.0031): Blue Wide Dynamic Range Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### C
<table><tr><td>[CIG](https://doi.org/10.1078/0176-1617-00887): Chlorophyll Index Green.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[CIRE](https://doi.org/10.1078/0176-1617-00887): Chlorophyll Index Red Edge.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[CVI](https://www.cabdirect.org/cabdirect/abstract/20073176046): Chlorophyll Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### D
<table><tr><td>[DVI](https://doi.org/10.1016/0034-4257(94)00114-3): Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[DVIplus](https://doi.org/10.1016/j.rse.2019.03.028): Difference Vegetation Index Plus.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### E
<table><tr><td>[EVI](https://doi.org/10.1016/S0034-4257(96)00112-5): Enhanced Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[EVI2](https://doi.org/10.1016/j.rse.2008.06.006): Two-Band Enhanced Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[ExG](https://doi.org/10.13031/2013.27838): Excess Green Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[ExGR](https://doi.org/10.1016/j.compag.2008.03.009): ExG - ExR Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[ExR](https://doi.org/10.1117/12.336896): Excess Red Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### F
<table><tr><td>[FCVI](https://doi.org/10.1016/j.rse.2020.111676): Fluorescence Correction Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### G
<table><tr><td>[GARI](https://www.indexdatabase.de/db/i-single.php?id=363): Green Atmospherically Resistant Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GBNDVI](https://www.indexdatabase.de/db/i-single.php?id=186): Green-Blue Normalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GCC](https://doi.org/10.1016/0034-4257(87)90088-5): Green Chromatic Coordinate.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GDVI](https://doi.org/10.3390/rs6021211): Generalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GEMI](http://dx.doi.org/10.1007/bf00031911): Global Environment Monitoring Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GLI](http://dx.doi.org/10.1080/10106040108542184): Green Leaf Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GM1](https://doi.org/10.1016/S0176-1617(96)80284-7): Gitelson and Merzlyak Index 1.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GM2](https://doi.org/10.1016/S0176-1617(96)80284-7): Gitelson and Merzlyak Index 2.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GNDVI](https://doi.org/10.1016/S0034-4257(96)00072-7): Green Normalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GOSAVI](https://doi.org/10.2134/agronj2004.0314): Green Optimized Soil Adjusted Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GRNDVI](https://www.indexdatabase.de/db/i-single.php?id=185): Green-Red Normalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GRVI](https://doi.org/10.2134/agronj2004.0314): Green Ratio Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GSAVI](https://doi.org/10.2134/agronj2004.0314): Green Soil Adjusted Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[GVMI](https://doi.org/10.1016/S0034-4257(02)00037-8): Global Vegetation Moisture Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### I
<table><tr><td>[IAVI](https://www.jipb.net/EN/abstract/abstract23925.shtml): New Atmospherically Resistant Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[IKAW](https://doi.org/10.1006/anbo.1997.0544): Kawashima Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[IPVI](https://doi.org/10.1016/0034-4257(90)90085-Z): Infrared Percentage Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[IRECI](https://doi.org/10.1016/j.isprsjprs.2013.04.007): Inverted Red-Edge Chlorophyll Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### M
<table><tr><td>[MCARI](http://dx.doi.org/10.1016/S0034-4257(00)00113-9): Modified Chlorophyll Absorption in Reflectance Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MCARI1](https://doi.org/10.1016/j.rse.2003.12.013): Modified Chlorophyll Absorption in Reflectance Index 1.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MCARI2](https://doi.org/10.1016/j.rse.2003.12.013): Modified Chlorophyll Absorption in Reflectance Index 2.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MCARI705](https://doi.org/10.1016/j.agrformet.2008.03.005): Modified Chlorophyll Absorption in Reflectance Index (705 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MCARIOSAVI](https://doi.org/10.1016/S0034-4257(00)00113-9): MCARI/OSAVI Ratio.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MCARIOSAVI705](https://doi.org/10.1016/j.agrformet.2008.03.005): MCARI/OSAVI Ratio (705 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MGRVI](https://doi.org/10.1016/j.jag.2015.02.012): Modified Green Red Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MNDVI](https://doi.org/10.1080/014311697216810): Modified Normalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MNLI](https://doi.org/10.1109/TGRS.2003.812910): Modified Non-Linear Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MRBVI](https://doi.org/10.3390/s20185055): Modified Red Blue Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MSAVI](https://doi.org/10.1016/0034-4257(94)90134-1): Modified Soil-Adjusted Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MSI](https://doi.org/10.1016/0034-4257(89)90046-1): Moisture Stress Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MSR](https://doi.org/10.1080/07038992.1996.10855178): Modified Simple Ratio.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MSR705](https://doi.org/10.1016/j.agrformet.2008.03.005): Modified Simple Ratio (705 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MTCI](https://doi.org/10.1080/0143116042000274015): MERIS Terrestrial Chlorophyll Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MTVI1](https://doi.org/10.1016/j.rse.2003.12.013): Modified Triangular Vegetation Index 1.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MTVI2](https://doi.org/10.1016/j.rse.2003.12.013): Modified Triangular Vegetation Index 2.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[mND705](https://doi.org/10.1016/S0034-4257(02)00010-X): Modified Normalized Difference (705, 750 and 445 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[mSR705](https://doi.org/10.1016/S0034-4257(02)00010-X): Modified Simple Ratio (705 and 445 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### N
<table><tr><td>[ND705](https://doi.org/10.1016/S0034-4257(02)00010-X): Normalized Difference (705 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDDI](https://doi.org/10.1029/2006GL029127): Normalized Difference Drought Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDGI](https://doi.org/10.1016/j.rse.2019.03.028): Normalized Difference Greenness Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDII](https://www.asprs.org/wp-content/uploads/pers/1983journal/jan/1983_jan_77-83.pdf): Normalized Difference Infrared Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDMI](https://doi.org/10.1016/S0034-4257(01)00318-2): Normalized Difference Moisture Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDPI](https://doi.org/10.1016/j.rse.2017.04.031): Normalized Difference Phenology Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDREI](https://doi.org/10.1016/1011-1344(93)06963-4): Normalized Difference Red Edge Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDVI](https://ntrs.nasa.gov/citations/19740022614): Normalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDVI705](https://doi.org/10.1016/S0176-1617(11)81633-0): Normalized Difference Vegetation Index (705 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDYI](https://doi.org/10.1016/j.rse.2016.06.016): Normalized Difference Yellowness Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NGRDI](https://doi.org/10.1016/0034-4257(79)90013-0): Normalized Green Red Difference Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NIRv](https://doi.org/10.1126/sciadv.1602244): Near-Infrared Reflectance of Vegetation.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NIRvH2](https://doi.org/10.1016/j.rse.2021.112723): Hyperspectral Near-Infrared Reflectance of Vegetation.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NIRvP](https://doi.org/10.1016/j.rse.2021.112763): Near-Infrared Reflectance of Vegetation and Incoming PAR.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NLI](https://doi.org/10.1080/02757259409532252): Non-Linear Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NMDI](https://doi.org/10.1029/2007GL031021): Normalized Multi-band Drought Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NRFIg](https://doi.org/10.3390/rs13010105): Normalized Rapeseed Flowering Index Green.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NRFIr](https://doi.org/10.3390/rs13010105): Normalized Rapeseed Flowering Index Red.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NormG](https://doi.org/10.2134/agronj2004.0314): Normalized Green.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NormNIR](https://doi.org/10.2134/agronj2004.0314): Normalized NIR.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NormR](https://doi.org/10.2134/agronj2004.0314): Normalized Red.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### O
<table><tr><td>[OCVI](http://dx.doi.org/10.1007/s11119-008-9075-z): Optimized Chlorophyll Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[OSAVI](https://doi.org/10.1016/0034-4257(95)00186-7): Optimized Soil-Adjusted Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### P
<table><tr><td>[PSRI](https://doi.org/10.1034/j.1399-3054.1999.106119.x): Plant Senescing Reflectance Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### R
<table><tr><td>[RCC](https://doi.org/10.1016/0034-4257(87)90088-5): Red Chromatic Coordinate.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[RDVI](https://doi.org/10.1016/0034-4257(94)00114-3): Renormalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[REDSI](https://doi.org/10.3390/s18030868): Red-Edge Disease Stress Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[RENDVI](https://doi.org/10.1016/S0176-1617(11)81633-0): Red Edge Normalized Difference Vegetation Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[RGBVI](https://doi.org/10.1016/j.jag.2015.02.012): Red Green Blue Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[RGRI](https://doi.org/10.1016/j.jag.2014.03.018): Red-Green Ratio Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[RI](https://www.documentation.ird.fr/hor/fdi:34390): Redness Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[RVI](https://doi.org/10.2134/agronj1968.00021962006000060016x): Ratio Vegetation Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### S
<table><tr><td>[S2REP](https://doi.org/10.1016/j.isprsjprs.2013.04.007): Sentinel-2 Red-Edge Position.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SARVI](https://doi.org/10.1109/36.134076): Soil Adjusted and Atmospherically Resistant Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SAVI](https://doi.org/10.1016/0034-4257(88)90106-X): Soil-Adjusted Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SAVI2](https://doi.org/10.1080/01431169008955053): Soil-Adjusted Vegetation Index 2.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SI](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.8749&rep=rep1&type=pdf): Shadow Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SIPI](https://eurekamag.com/research/009/395/009395053.php): Structure Insensitive Pigment Index.</td><td> ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SR](https://doi.org/10.2307/1936256): Simple Ratio.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SR2](https://doi.org/10.1080/01431169308904370): Simple Ratio (800 and 550 nm).</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SR3](https://doi.org/10.1016/S0034-4257(98)00046-7): Simple Ratio (860, 550 and 708 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SR555](https://doi.org/10.1016/S0176-1617(11)81633-0): Simple Ratio (555 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SR705](https://doi.org/10.1016/S0176-1617(11)81633-0): Simple Ratio (705 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SeLI](https://doi.org/10.3390/s19040904): Sentinel-2 LAI Green Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### T
<table><tr><td>[TCARI](https://doi.org/10.1016/S0034-4257(02)00018-4): Transformed Chlorophyll Absorption in Reflectance Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TCARIOSAVI](https://doi.org/10.1016/S0034-4257(02)00018-4): TCARI/OSAVI Ratio.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TCARIOSAVI705](https://doi.org/10.1016/j.agrformet.2008.03.005): TCARI/OSAVI Ratio (705 and 750 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TCI](http://dx.doi.org/10.1109/TGRS.2007.904836): Triangular Chlorophyll Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TDVI](https://doi.org/10.1109/IGARSS.2002.1026867): Transformed Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TGI](http://dx.doi.org/10.1016/j.jag.2012.07.020): Triangular Greenness Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TRRVI](https://doi.org/10.3390/rs12152359): Transformed Red Range Vegetation Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TSAVI](https://doi.org/10.1109/IGARSS.1989.576128): Transformed Soil-Adjusted Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TTVI](https://doi.org/10.3390/rs12010016): Transformed Triangular Vegetation Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TVI](https://ntrs.nasa.gov/citations/19740022614): Transformed Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[TriVI](http://dx.doi.org/10.1016/S0034-4257(00)00197-8): Triangular Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### V
<table><tr><td>[VARI](https://doi.org/10.1016/S0034-4257(01)00289-9): Visible Atmospherically Resistant Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[VARI700](https://doi.org/10.1016/S0034-4257(01)00289-9): Visible Atmospherically Resistant Index (700 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[VI700](https://doi.org/10.1016/S0034-4257(01)00289-9): Vegetation Index (700 nm).</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[VIG](https://doi.org/10.1016/S0034-4257(01)00289-9): Vegetation Index Green.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### W
<table><tr><td>[WDRVI](https://doi.org/10.1078/0176-1617-01176): Wide Dynamic Range Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[WDVI](https://doi.org/10.1016/0034-4257(89)90076-X): Weighted Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
## Water

### A
<table><tr><td>[AWEInsh](https://doi.org/10.1016/j.rse.2013.08.029): Automated Water Extraction Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[AWEIsh](https://doi.org/10.1016/j.rse.2013.08.029): Automated Water Extraction Index with Shadows Elimination.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### L
<table><tr><td>[LSWI](https://doi.org/10.1016/j.rse.2003.11.008): Land Surface Water Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### M
<table><tr><td>[MBWI](https://doi.org/10.1016/j.jag.2018.01.018): Multi-Band Water Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MLSWI26](https://doi.org/10.3390/rs71215805): Modified Land Surface Water Index (MODIS Bands 2 and 6).</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MLSWI27](https://doi.org/10.3390/rs71215805): Modified Land Surface Water Index (MODIS Bands 2 and 7).</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MNDWI](https://doi.org/10.1080/01431160600589179): Modified Normalized Difference Water Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[MuWIR](https://doi.org/10.3390/rs10101643): Revised Multi-Spectral Water Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### N
<table><tr><td>[NDVIMNDWI](https://doi.org/10.1007/978-3-662-45737-5_51): NDVI-MNDWI Model.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDWI](https://doi.org/10.1080/01431169608948714): Normalized Difference Water Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDWIns](https://doi.org/10.3390/w12051339): Normalized Difference Water Index with no Snow Cover and Glaciers.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NWI](https://doi.org/10.11873/j.issn.1004-0323.2009.2.167): New Water Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### S
<table><tr><td>[S2WI](https://doi.org/10.3390/w13121647): Sentinel-2 Water Index.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SWM](https://eoscience.esa.int/landtraining2017/files/posters/MILCZAREK.pdf): Sentinel Water Mask.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### W
<table><tr><td>[WI1](https://doi.org/10.3390/rs11182186): Water Index 1.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[WI2](https://doi.org/10.3390/rs11182186): Water Index 2.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[WRI](https://doi.org/10.1109/GEOINFORMATICS.2010.5567762): Water Ratio Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
## Burn

### B
<table><tr><td>[BAI](https://digital.csic.es/bitstream/10261/6426/1/Martin_Isabel_Serie_Geografica.pdf): Burned Area Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[BAIM](https://doi.org/10.1016/j.foreco.2006.08.248): Burned Area Index adapted to MODIS.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[BAIS2](https://doi.org/10.3390/ecrs-2-05177): Burned Area Index for Sentinel 2.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### C
<table><tr><td>[CSI](https://doi.org/10.1016/j.rse.2005.04.014): Char Soil Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[CSIT](https://doi.org/10.1080/01431160600954704): Char Soil Index Thermal.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
### M
<table><tr><td>[MIRBI](https://doi.org/10.1080/01431160110053185): Mid-Infrared Burn Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### N
<table><tr><td>[NBR](https://doi.org/10.3133/ofr0211): Normalized Burn Ratio.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NBR2](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-normalized-burn-ratio-2): Normalized Burn Ratio 2.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NBRT1](https://doi.org/10.1080/01431160500239008): Normalized Burn Ratio Thermal 1.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NBRT2](https://doi.org/10.1080/01431160500239008): Normalized Burn Ratio Thermal 2.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NBRT3](https://doi.org/10.1080/01431160500239008): Normalized Burn Ratio Thermal 3.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDVIT](https://doi.org/10.1080/01431160600954704): Normalized Difference Vegetation Index Thermal.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
### S
<table><tr><td>[SAVIT](https://doi.org/10.1080/01431160600954704): Soil-Adjusted Vegetation Index Thermal.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
### V
<table><tr><td>[VI6T](https://doi.org/10.1080/01431160500239008): VI6T Index.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
## Snow

### N
<table><tr><td>[NBSIMS](https://doi.org/10.3390/rs13142777): Non-Binary Snow Index for Multi-Component Surfaces.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDGlaI](https://doi.org/10.1080/01431160802385459): Normalized Difference Glacier Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDSI](https://doi.org/10.1109/IGARSS.1994.399618): Normalized Difference Snow Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDSII](https://doi.org/10.1080/01431160802385459): Normalized Difference Snow Ice Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDSInw](https://doi.org/10.3390/w12051339): Normalized Difference Snow Index with no Water.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDSaII](https://doi.org/10.1080/01431160119766): Normalized Difference Snow and Ice Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### S
<table><tr><td>[S3](https://doi.org/10.3178/jjshwr.12.28): S3 Snow Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[SWI](https://doi.org/10.3390/rs11232774): Snow Water Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
## Urban

### B
<table><tr><td>[BI](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.8749&rep=rep1&type=pdf): Bare Soil Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[BLFEI](https://doi.org/10.1080/10106049.2018.1497094): Built-Up Land Features Extraction Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[BaI](https://doi.org/10.1109/IGARSS.2005.1525743): Bareness Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### D
<table><tr><td>[DBI](https://doi.org/10.3390/land7030081): Dry Built-Up Index.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[DBSI](https://doi.org/10.3390/land7030081): Dry Bareness Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### E
<table><tr><td>[EBBI](https://doi.org/10.3390/rs4102957): Enhanced Built-Up and Bareness Index.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[EMBI](https://doi.org/10.1016/j.jag.2022.102703): Enhanced Modified Bare Soil Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### I
<table><tr><td>[IBI](https://doi.org/10.1080/01431160802039957): Index-Based Built-Up Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### M
<table><tr><td>[MBI](https://doi.org/10.3390/land10030231): Modified Bare Soil Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### N
<table><tr><td>[NBLI](https://doi.org/10.3390/rs9030249): Normalized Difference Bare Land Index.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NBUI](https://hdl.handle.net/1959.11/29500): New Built-Up Index.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDBI](http://dx.doi.org/10.1080/01431160304987): Normalized Difference Built-Up Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NDBaI](https://doi.org/10.1109/IGARSS.2005.1526319): Normalized Difference Bareness Index.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDISIb](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index Blue.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDISIg](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index Green.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDISImndwi](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index with MNDWI.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDISIndwi](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index with NDWI.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDISIr](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index Red.</td><td> ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) </td></tr></table>
<tr><td>[NDSoI](https://doi.org/10.1016/j.jag.2015.02.010): Normalized Difference Soil Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NHFD](https://www.semanticscholar.org/paper/Using-WorldView-2-Vis-NIR-MSI-Imagery-to-Support-Wolf/5e5063ccc4ee76b56b721c866e871d47a77f9fb4): Non-Homogeneous Feature Difference.</td><td> ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[NSDS](https://doi.org/10.3390/land10030231): Normalized Shortwave Infrared Difference Soil-Moisture.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### P
<table><tr><td>[PISI](https://doi.org/10.3390/rs10101521): Perpendicular Impervious Surface Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### U
<table><tr><td>[UI](https://www.isprs.org/proceedings/XXXI/congress/part7/321_XXXI-part7.pdf): Urban Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
### V
<table><tr><td>[VgNIRBI](https://doi.org/10.1016/j.ecolind.2015.03.037): Visible Green-Based Built-Up Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[VrNIRBI](https://doi.org/10.1016/j.ecolind.2015.03.037): Visible Red-Based Built-Up Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
## Kernel

### K
<table><tr><td>[kEVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Enhanced Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[kIPVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Infrared Percentage Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[kNDVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Normalized Difference Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[kRVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Ratio Vegetation Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
<tr><td>[kVARI](https://doi.org/10.1126/sciadv.abc7447): Kernel Visible Atmospherically Resistant Index.</td><td> ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) </td></tr></table>
## Radar

### D
<table><tr><td>[DPDD](https://doi.org/10.1016/j.rse.2018.09.003): Dual-Pol Diagonal Distance.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[DpRVIHH](https://www.tandfonline.com/doi/abs/10.5589/m12-043): Dual-Polarized Radar Vegetation Index HH.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[DpRVIVV](https://doi.org/10.3390/app9040655): Dual-Polarized Radar Vegetation Index VV.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
### N
<table><tr><td>[NDPolI](https://www.isprs.org/proceedings/XXXVII/congress/4_pdf/267.pdf): Normalized Difference Polarization Index.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
### Q
<table><tr><td>[QpRVI](https://doi.org/10.1109/IGARSS.2001.976856): Quad-Polarized Radar Vegetation Index.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
### R
<table><tr><td>[RFDI](https://doi.org/10.5194/bg-9-179-2012): Radar Forest Degradation Index.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
### V
<table><tr><td>[VDDPI](https://doi.org/10.1016/j.rse.2018.09.003): Vertical Dual De-Polarization Index.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[VHVVD](https://doi.org/10.3390/app9040655): VH-VV Difference.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[VHVVP](https://doi.org/10.1109/IGARSS47720.2021.9554099): VH-VV Product.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[VHVVR](https://doi.org/10.1109/IGARSS47720.2021.9554099): VH-VV Ratio.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[VVVHD](https://doi.org/10.1109/IGARSS47720.2021.9554099): VV-VH Difference.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[VVVHR](https://doi.org/10.3390/app9040655): VV-VH Ratio.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>
<tr><td>[VVVHS](https://doi.org/10.1109/IGARSS47720.2021.9554099): VV-VH Sum.</td><td> ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) </td></tr></table>

# List

Check the full list of spectral indices with their formulas [here](https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-table.csv).

# Download Raw Files

You can download or clone the repository:

```
git clone https://github.com/davemlz/awesome-ee-spectral-indices.git
```

Or you can download the single files here (right-click > Save link as...):

- JSON: [Raw list](https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-dict.json)
- CSV: [Raw list](https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-table.csv)

# Credits

- [César Aybar](https://github.com/csaybar): The formidable [pydantic](https://github.com/samuelcolvin/pydantic/) expert and creator of [rgee](https://github.com/r-spatial/rgee).

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
- [AFRI1600](https://doi.org/10.1016/S0034-4257(01)00190-0): Aerosol Free Vegetation Index (1600 nm). ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [AFRI2100](https://doi.org/10.1016/S0034-4257(01)00190-0): Aerosol Free Vegetation Index (2100 nm). ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [ARI](https://doi.org/10.1562/0031-8655(2001)074%3C0038:OPANEO%3E2.0.CO;2): Anthocyanin Reflectance Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [ARI2](https://doi.org/10.1562/0031-8655(2001)074%3C0038:OPANEO%3E2.0.CO;2): Anthocyanin Reflectance Index 2. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [ARVI](https://doi.org/10.1109/36.134076): Atmospherically Resistant Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [ATSAVI](https://doi.org/10.1016/0034-4257(91)90009-U): Adjusted Transformed Soil-Adjusted Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [AVI](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.8749&rep=rep1&type=pdf): Advanced Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### B
- [BCC](https://doi.org/10.1016/0034-4257(87)90088-5): Blue Chromatic Coordinate. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [BNDVI](https://doi.org/10.1016/S1672-6308(07)60027-4): Blue Normalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [BWDRVI](https://doi.org/10.2135/cropsci2007.01.0031): Blue Wide Dynamic Range Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### C
- [CIG](https://doi.org/10.1078/0176-1617-00887): Chlorophyll Index Green. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [CIRE](https://doi.org/10.1078/0176-1617-00887): Chlorophyll Index Red Edge. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [CVI](https://www.cabdirect.org/cabdirect/abstract/20073176046): Chlorophyll Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### D
- [DVI](https://doi.org/10.1016/0034-4257(94)00114-3): Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [DVIplus](https://doi.org/10.1016/j.rse.2019.03.028): Difference Vegetation Index Plus. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### E
- [EVI](https://doi.org/10.1016/S0034-4257(96)00112-5): Enhanced Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [EVI2](https://doi.org/10.1016/j.rse.2008.06.006): Two-Band Enhanced Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [ExG](https://doi.org/10.13031/2013.27838): Excess Green Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [ExGR](https://doi.org/10.1016/j.compag.2008.03.009): ExG - ExR Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [ExR](https://doi.org/10.1117/12.336896): Excess Red Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### F
- [FCVI](https://doi.org/10.1016/j.rse.2020.111676): Fluorescence Correction Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### G
- [GARI](https://www.indexdatabase.de/db/i-single.php?id=363): Green Atmospherically Resistant Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GBNDVI](https://www.indexdatabase.de/db/i-single.php?id=186): Green-Blue Normalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GCC](https://doi.org/10.1016/0034-4257(87)90088-5): Green Chromatic Coordinate. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GDVI](https://doi.org/10.3390/rs6021211): Generalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GEMI](http://dx.doi.org/10.1007/bf00031911): Global Environment Monitoring Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GLI](http://dx.doi.org/10.1080/10106040108542184): Green Leaf Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GM1](https://doi.org/10.1016/S0176-1617(96)80284-7): Gitelson and Merzlyak Index 1. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GM2](https://doi.org/10.1016/S0176-1617(96)80284-7): Gitelson and Merzlyak Index 2. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GNDVI](https://doi.org/10.1016/S0034-4257(96)00072-7): Green Normalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GOSAVI](https://doi.org/10.2134/agronj2004.0314): Green Optimized Soil Adjusted Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GRNDVI](https://www.indexdatabase.de/db/i-single.php?id=185): Green-Red Normalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GRVI](https://doi.org/10.2134/agronj2004.0314): Green Ratio Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GSAVI](https://doi.org/10.2134/agronj2004.0314): Green Soil Adjusted Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [GVMI](https://doi.org/10.1016/S0034-4257(02)00037-8): Global Vegetation Moisture Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### I
- [IAVI](https://www.jipb.net/EN/abstract/abstract23925.shtml): New Atmospherically Resistant Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [IKAW](https://doi.org/10.1006/anbo.1997.0544): Kawashima Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [IPVI](https://doi.org/10.1016/0034-4257(90)90085-Z): Infrared Percentage Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [IRECI](https://doi.org/10.1016/j.isprsjprs.2013.04.007): Inverted Red-Edge Chlorophyll Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### K
- [kIPVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Infrared Percentage Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### M
- [MCARI](http://dx.doi.org/10.1016/S0034-4257(00)00113-9): Modified Chlorophyll Absorption in Reflectance Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MCARI1](https://doi.org/10.1016/j.rse.2003.12.013): Modified Chlorophyll Absorption in Reflectance Index 1. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MCARI2](https://doi.org/10.1016/j.rse.2003.12.013): Modified Chlorophyll Absorption in Reflectance Index 2. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MCARI705](https://doi.org/10.1016/j.agrformet.2008.03.005): Modified Chlorophyll Absorption in Reflectance Index (705 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MCARIOSAVI](https://doi.org/10.1016/S0034-4257(00)00113-9): MCARI/OSAVI Ratio. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MCARIOSAVI705](https://doi.org/10.1016/j.agrformet.2008.03.005): MCARI/OSAVI Ratio (705 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MGRVI](https://doi.org/10.1016/j.jag.2015.02.012): Modified Green Red Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MNDVI](https://doi.org/10.1080/014311697216810): Modified Normalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MNLI](https://doi.org/10.1109/TGRS.2003.812910): Modified Non-Linear Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MRBVI](https://doi.org/10.3390/s20185055): Modified Red Blue Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MSAVI](https://doi.org/10.1016/0034-4257(94)90134-1): Modified Soil-Adjusted Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MSI](https://doi.org/10.1016/0034-4257(89)90046-1): Moisture Stress Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MSR](https://doi.org/10.1080/07038992.1996.10855178): Modified Simple Ratio. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MSR705](https://doi.org/10.1016/j.agrformet.2008.03.005): Modified Simple Ratio (705 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MTCI](https://doi.org/10.1080/0143116042000274015): MERIS Terrestrial Chlorophyll Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MTVI1](https://doi.org/10.1016/j.rse.2003.12.013): Modified Triangular Vegetation Index 1. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MTVI2](https://doi.org/10.1016/j.rse.2003.12.013): Modified Triangular Vegetation Index 2. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [mND705](https://doi.org/10.1016/S0034-4257(02)00010-X): Modified Normalized Difference (705, 750 and 445 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [mSR705](https://doi.org/10.1016/S0034-4257(02)00010-X): Modified Simple Ratio (705 and 445 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### N
- [ND705](https://doi.org/10.1016/S0034-4257(02)00010-X): Normalized Difference (705 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDDI](https://doi.org/10.1029/2006GL029127): Normalized Difference Drought Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDGI](https://doi.org/10.1016/j.rse.2019.03.028): Normalized Difference Greenness Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDII](https://www.asprs.org/wp-content/uploads/pers/1983journal/jan/1983_jan_77-83.pdf): Normalized Difference Infrared Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDMI](https://doi.org/10.1016/S0034-4257(01)00318-2): Normalized Difference Moisture Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDPI](https://doi.org/10.1016/j.rse.2017.04.031): Normalized Difference Phenology Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDREI](https://doi.org/10.1016/1011-1344(93)06963-4): Normalized Difference Red Edge Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDVI](https://ntrs.nasa.gov/citations/19740022614): Normalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDVI705](https://doi.org/10.1016/S0176-1617(11)81633-0): Normalized Difference Vegetation Index (705 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDYI](https://doi.org/10.1016/j.rse.2016.06.016): Normalized Difference Yellowness Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NGRDI](https://doi.org/10.1016/0034-4257(79)90013-0): Normalized Green Red Difference Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NIRv](https://doi.org/10.1126/sciadv.1602244): Near-Infrared Reflectance of Vegetation. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NIRvH2](https://doi.org/10.1016/j.rse.2021.112723): Hyperspectral Near-Infrared Reflectance of Vegetation. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NIRvP](https://doi.org/10.1016/j.rse.2021.112763): Near-Infrared Reflectance of Vegetation and Incoming PAR. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NLI](https://doi.org/10.1080/02757259409532252): Non-Linear Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NMDI](https://doi.org/10.1029/2007GL031021): Normalized Multi-band Drought Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NRFIg](https://doi.org/10.3390/rs13010105): Normalized Rapeseed Flowering Index Green. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NRFIr](https://doi.org/10.3390/rs13010105): Normalized Rapeseed Flowering Index Red. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NormG](https://doi.org/10.2134/agronj2004.0314): Normalized Green. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NormNIR](https://doi.org/10.2134/agronj2004.0314): Normalized NIR. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NormR](https://doi.org/10.2134/agronj2004.0314): Normalized Red. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### O
- [OCVI](http://dx.doi.org/10.1007/s11119-008-9075-z): Optimized Chlorophyll Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [OSAVI](https://doi.org/10.1016/0034-4257(95)00186-7): Optimized Soil-Adjusted Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### P
- [PSRI](https://doi.org/10.1034/j.1399-3054.1999.106119.x): Plant Senescing Reflectance Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### R
- [RCC](https://doi.org/10.1016/0034-4257(87)90088-5): Red Chromatic Coordinate. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [RDVI](https://doi.org/10.1016/0034-4257(94)00114-3): Renormalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [REDSI](https://doi.org/10.3390/s18030868): Red-Edge Disease Stress Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [RENDVI](https://doi.org/10.1016/S0176-1617(11)81633-0): Red Edge Normalized Difference Vegetation Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [RGBVI](https://doi.org/10.1016/j.jag.2015.02.012): Red Green Blue Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [RGRI](https://doi.org/10.1016/j.jag.2014.03.018): Red-Green Ratio Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [RI](https://www.documentation.ird.fr/hor/fdi:34390): Redness Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [RVI](https://doi.org/10.2134/agronj1968.00021962006000060016x): Ratio Vegetation Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### S
- [S2REP](https://doi.org/10.1016/j.isprsjprs.2013.04.007): Sentinel-2 Red-Edge Position. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SARVI](https://doi.org/10.1109/36.134076): Soil Adjusted and Atmospherically Resistant Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SAVI](https://doi.org/10.1016/0034-4257(88)90106-X): Soil-Adjusted Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SAVI2](https://doi.org/10.1080/01431169008955053): Soil-Adjusted Vegetation Index 2. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SI](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.8749&rep=rep1&type=pdf): Shadow Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SIPI](https://eurekamag.com/research/009/395/009395053.php): Structure Insensitive Pigment Index. ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SR](https://doi.org/10.2307/1936256): Simple Ratio. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SR2](https://doi.org/10.1080/01431169308904370): Simple Ratio (800 and 550 nm). ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SR3](https://doi.org/10.1016/S0034-4257(98)00046-7): Simple Ratio (860, 550 and 708 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SR555](https://doi.org/10.1016/S0176-1617(11)81633-0): Simple Ratio (555 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SR705](https://doi.org/10.1016/S0176-1617(11)81633-0): Simple Ratio (705 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SeLI](https://doi.org/10.3390/s19040904): Sentinel-2 LAI Green Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### T
- [TCARI](https://doi.org/10.1016/S0034-4257(02)00018-4): Transformed Chlorophyll Absorption in Reflectance Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TCARIOSAVI](https://doi.org/10.1016/S0034-4257(02)00018-4): TCARI/OSAVI Ratio. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TCARIOSAVI705](https://doi.org/10.1016/j.agrformet.2008.03.005): TCARI/OSAVI Ratio (705 and 750 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TCI](http://dx.doi.org/10.1109/TGRS.2007.904836): Triangular Chlorophyll Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TDVI](https://doi.org/10.1109/IGARSS.2002.1026867): Transformed Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TGI](http://dx.doi.org/10.1016/j.jag.2012.07.020): Triangular Greenness Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TRRVI](https://doi.org/10.3390/rs12152359): Transformed Red Range Vegetation Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TSAVI](https://doi.org/10.1109/IGARSS.1989.576128): Transformed Soil-Adjusted Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TTVI](https://doi.org/10.3390/rs12010016): Transformed Triangular Vegetation Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TVI](https://ntrs.nasa.gov/citations/19740022614): Transformed Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [TriVI](http://dx.doi.org/10.1016/S0034-4257(00)00197-8): Triangular Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### V
- [VARI](https://doi.org/10.1016/S0034-4257(01)00289-9): Visible Atmospherically Resistant Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [VARI700](https://doi.org/10.1016/S0034-4257(01)00289-9): Visible Atmospherically Resistant Index (700 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [VI700](https://doi.org/10.1016/S0034-4257(01)00289-9): Vegetation Index (700 nm). ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [VIG](https://doi.org/10.1016/S0034-4257(01)00289-9): Vegetation Index Green. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### W
- [WDRVI](https://doi.org/10.1078/0176-1617-01176): Wide Dynamic Range Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [WDVI](https://doi.org/10.1016/0034-4257(89)90076-X): Weighted Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
## Water

### A
- [AWEInsh](https://doi.org/10.1016/j.rse.2013.08.029): Automated Water Extraction Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [AWEIsh](https://doi.org/10.1016/j.rse.2013.08.029): Automated Water Extraction Index with Shadows Elimination. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### L
- [LSWI](https://doi.org/10.1016/j.rse.2003.11.008): Land Surface Water Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### M
- [MBWI](https://doi.org/10.1016/j.jag.2018.01.018): Multi-Band Water Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MLSWI26](https://doi.org/10.3390/rs71215805): Modified Land Surface Water Index (MODIS Bands 2 and 6). ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MLSWI27](https://doi.org/10.3390/rs71215805): Modified Land Surface Water Index (MODIS Bands 2 and 7). ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MNDWI](https://doi.org/10.1080/01431160600589179): Modified Normalized Difference Water Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [MuWIR](https://doi.org/10.3390/rs10101643): Revised Multi-Spectral Water Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### N
- [NDVIMNDWI](https://doi.org/10.1007/978-3-662-45737-5_51): NDVI-MNDWI Model. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDWI](https://doi.org/10.1080/01431169608948714): Normalized Difference Water Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDWIns](https://doi.org/10.3390/w12051339): Normalized Difference Water Index with no Snow Cover and Glaciers. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NWI](https://doi.org/10.11873/j.issn.1004-0323.2009.2.167): New Water Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### S
- [S2WI](https://doi.org/10.3390/w13121647): Sentinel-2 Water Index. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SWM](https://eoscience.esa.int/landtraining2017/files/posters/MILCZAREK.pdf): Sentinel Water Mask. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### W
- [WI1](https://doi.org/10.3390/rs11182186): Water Index 1. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [WI2](https://doi.org/10.3390/rs11182186): Water Index 2. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [WRI](https://doi.org/10.1109/GEOINFORMATICS.2010.5567762): Water Ratio Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
## Burn

### B
- [BAI](https://digital.csic.es/bitstream/10261/6426/1/Martin_Isabel_Serie_Geografica.pdf): Burned Area Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [BAIM](https://doi.org/10.1016/j.foreco.2006.08.248): Burned Area Index adapted to MODIS. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [BAIS2](https://doi.org/10.3390/ecrs-2-05177): Burned Area Index for Sentinel 2. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### C
- [CSI](https://doi.org/10.1016/j.rse.2005.04.014): Char Soil Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [CSIT](https://doi.org/10.1080/01431160600954704): Char Soil Index Thermal. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
### M
- [MIRBI](https://doi.org/10.1080/01431160110053185): Mid-Infrared Burn Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### N
- [NBR](https://doi.org/10.3133/ofr0211): Normalized Burn Ratio. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NBR2](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-normalized-burn-ratio-2): Normalized Burn Ratio 2. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NBRT1](https://doi.org/10.1080/01431160500239008): Normalized Burn Ratio Thermal 1. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NBRT2](https://doi.org/10.1080/01431160500239008): Normalized Burn Ratio Thermal 2. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NBRT3](https://doi.org/10.1080/01431160500239008): Normalized Burn Ratio Thermal 3. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDVIT](https://doi.org/10.1080/01431160600954704): Normalized Difference Vegetation Index Thermal. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
### S
- [SAVIT](https://doi.org/10.1080/01431160600954704): Soil-Adjusted Vegetation Index Thermal. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
### V
- [VI6T](https://doi.org/10.1080/01431160500239008): VI6T Index. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
## Snow

### N
- [NBSIMS](https://doi.org/10.3390/rs13142777): Non-Binary Snow Index for Multi-Component Surfaces. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDGlaI](https://doi.org/10.1080/01431160802385459): Normalized Difference Glacier Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDSI](https://doi.org/10.1109/IGARSS.1994.399618): Normalized Difference Snow Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDSII](https://doi.org/10.1080/01431160802385459): Normalized Difference Snow Ice Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDSInw](https://doi.org/10.3390/w12051339): Normalized Difference Snow Index with no Water. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDSaII](https://doi.org/10.1080/01431160119766): Normalized Difference Snow and Ice Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### S
- [S3](https://doi.org/10.3178/jjshwr.12.28): S3 Snow Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [SWI](https://doi.org/10.3390/rs11232774): Snow Water Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
## Urban

### B
- [BI](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.8749&rep=rep1&type=pdf): Bare Soil Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [BLFEI](https://doi.org/10.1080/10106049.2018.1497094): Built-Up Land Features Extraction Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [BaI](https://doi.org/10.1109/IGARSS.2005.1525743): Bareness Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### D
- [DBI](https://doi.org/10.3390/land7030081): Dry Built-Up Index. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [DBSI](https://doi.org/10.3390/land7030081): Dry Bareness Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### E
- [EBBI](https://doi.org/10.3390/rs4102957): Enhanced Built-Up and Bareness Index. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [EMBI](https://doi.org/10.1016/j.jag.2022.102703): Enhanced Modified Bare Soil Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### I
- [IBI](https://doi.org/10.1080/01431160802039957): Index-Based Built-Up Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### M
- [MBI](https://doi.org/10.3390/land10030231): Modified Bare Soil Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### N
- [NBLI](https://doi.org/10.3390/rs9030249): Normalized Difference Bare Land Index. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NBUI](https://hdl.handle.net/1959.11/29500): New Built-Up Index. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDBI](http://dx.doi.org/10.1080/01431160304987): Normalized Difference Built-Up Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NDBaI](https://doi.org/10.1109/IGARSS.2005.1526319): Normalized Difference Bareness Index. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDISIb](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index Blue. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDISIg](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index Green. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDISImndwi](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index with MNDWI. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDISIndwi](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index with NDWI. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDISIr](https://doi.org/10.14358/PERS.76.5.557): Normalized Difference Impervious Surface Index Red. ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square) 
- [NDSoI](https://doi.org/10.1016/j.jag.2015.02.010): Normalized Difference Soil Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NHFD](https://www.semanticscholar.org/paper/Using-WorldView-2-Vis-NIR-MSI-Imagery-to-Support-Wolf/5e5063ccc4ee76b56b721c866e871d47a77f9fb4): Non-Homogeneous Feature Difference. ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [NSDS](https://doi.org/10.3390/land10030231): Normalized Shortwave Infrared Difference Soil-Moisture. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### P
- [PISI](https://doi.org/10.3390/rs10101521): Perpendicular Impervious Surface Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### U
- [UI](https://www.isprs.org/proceedings/XXXI/congress/part7/321_XXXI-part7.pdf): Urban Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
### V
- [VgNIRBI](https://doi.org/10.1016/j.ecolind.2015.03.037): Visible Green-Based Built-Up Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [VrNIRBI](https://doi.org/10.1016/j.ecolind.2015.03.037): Visible Red-Based Built-Up Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
## Kernel

### K
- [kEVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Enhanced Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [kNDVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Normalized Difference Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [kRVI](https://doi.org/10.1126/sciadv.abc7447): Kernel Ratio Vegetation Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
- [kVARI](https://doi.org/10.1126/sciadv.abc7447): Kernel Visible Atmospherically Resistant Index. ![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)  ![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)  ![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)  ![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square) 
## Radar

### D
- [DPDD](https://doi.org/10.1016/j.rse.2018.09.003): Dual-Pol Diagonal Distance. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [DpRVIHH](https://www.tandfonline.com/doi/abs/10.5589/m12-043): Dual-Polarized Radar Vegetation Index HH. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [DpRVIVV](https://doi.org/10.3390/app9040655): Dual-Polarized Radar Vegetation Index VV. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
### N
- [NDPolI](https://www.isprs.org/proceedings/XXXVII/congress/4_pdf/267.pdf): Normalized Difference Polarization Index. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
### Q
- [QpRVI](https://doi.org/10.1109/IGARSS.2001.976856): Quad-Polarized Radar Vegetation Index. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
### R
- [RFDI](https://doi.org/10.5194/bg-9-179-2012): Radar Forest Degradation Index. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
### V
- [VDDPI](https://doi.org/10.1016/j.rse.2018.09.003): Vertical Dual De-Polarization Index. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [VHVVD](https://doi.org/10.3390/app9040655): VH-VV Difference. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [VHVVP](https://doi.org/10.1109/IGARSS47720.2021.9554099): VH-VV Product. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [VHVVR](https://doi.org/10.1109/IGARSS47720.2021.9554099): VH-VV Ratio. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [VVVHD](https://doi.org/10.1109/IGARSS47720.2021.9554099): VV-VH Difference. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [VVVHR](https://doi.org/10.3390/app9040655): VV-VH Ratio. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 
- [VVVHS](https://doi.org/10.1109/IGARSS47720.2021.9554099): VV-VH Sum. ![Sentinel-1](https://img.shields.io/badge/-Sentinel%201-gray?style=flat-square) 

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

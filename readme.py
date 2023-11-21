import json

with open("output/spectral-indices-dict.json", "r") as f:
    data = json.load(f)

previousText = """<p align="center">
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

**GitHub**: <a href="https://github.com/awesome-spectral-indices/awesome-spectral-indices" target="_blank">github.com/awesome-spectral-indices/awesome-spectral-indices</a>

**Documentation**: <a href="https://awesome-ee-spectral-indices.readthedocs.io/" target="_blank">awesome-ee-spectral-indices.readthedocs.io</a>

**Python Package**: <a href="https://github.com/awesome-spectral-indices/spyndex" target="_blank">github.com/awesome-spectral-indices/spyndex</a>

**Paper**: <a href="https://doi.org/10.1038/s41597-023-02096-0" target="_blank">doi.org/10.1038/s41597-023-02096-0</a>

**Streamlit App**: <a href="https://github.com/awesome-spectral-indices/espectro" target="_blank">github.com/awesome-spectral-indices/espectro</a>

**Google Earth Engine**: <a href="https://github.com/davemlz/eemont" target="_blank">github.com/davemlz/eemont</a> (Python), <a href="https://github.com/awesome-spectral-indices/spectral" target="_blank">github.com/awesome-spectral-indices/spectral</a> (JavaScript) and <a href="https://github.com/r-earthengine/rgeeExtra" target="_blank">github.com/r-earthengine/rgeeExtra</a> (R)

---

# Spectral Indices

Spectral Indices are widely used in the Remote Sensing community. This repository keeps track of classical as well as novel spectral indices for different Remote Sensing applications. All spectral indices in the repository are curated and can be used in different environments and programming languages. 
You can check the [curated list of spectral indices here](https://github.com/awesome-spectral-indices/awesome-spectral-indices/blob/main/output/spectral-indices-table.csv), and if you want to use it in your environment, it is available in [CSV](https://raw.githubusercontent.com/awesome-spectral-indices/awesome-spectral-indices/main/output/spectral-indices-table.csv) and [JSON](https://raw.githubusercontent.com/awesome-spectral-indices/awesome-spectral-indices/main/output/spectral-indices-dict.json).

## Citation

If you use this work, please consider citing the following paper:

```bibtex
@article{montero2023standardized,
  title={A standardized catalogue of spectral indices to advance the use of remote sensing in Earth system research},
  author={Montero, David and Aybar, C{\'e}sar and Mahecha, Miguel D and Martinuzzi, Francesco and S{\"o}chting, Maximilian and Wieneke, Sebastian},
  journal={Scientific Data},
  volume={10},
  number={1},
  pages={197},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```

## Attributes

All spectral indices follow a standard. Each item of the list has the following attributes:

- `short_name`: Short name of the index (e.g. `"NDWI"`).
- `long_name`: Long name of the index (e.g. `"Normalized Difference Water Index"`).
- `formula`: Expression/formula of the index (e.g. `"(G - N)/(G + N)"`).
- `bands`: List of required bands/parameters for the index computation (e.g. `["N","G"]`).
- `platforms`: List of platforms with the required bands for the index computation (e.g. `["MODIS", "Landsat-457", "Landsat-89", "Sentinel-2"]`).
- `reference`: Link to the index reference/paper/doi (e.g. `"https://doi.org/10.1080/01431169608948714"`).
- `application_domain`: Application domain of the index (e.g. `"water"`).
- `date_of_addition`: Date of addition to the list (e.g. `"2021-04-07"`).
- `contributor`: GitHub user link of the contributor (e.g. `"https://github.com/davemlz"`).

## Expressions

The formula of the index is presented as a string/expression (e.g. `"(N - R)/(N + R)"`) that can be easily evaluated. The parameters used in the expression for each index follow this standard:

<table>

<tr>

<th> Description </th>
<th> Standard </th>
<th> Spectral Range (nm) </th>
<th> Sentinel-2 </th>
<th> Landsat-89 </th>
<th> Landsat-457 </th>
<th> MODIS </th>

</tr>

<tr>

<td>Aerosols</td>
<td>A</td>
<td>400 - 455</td>
<td>B1</td>
<td>B1</td>
<td></td>
<td></td>

</tr>

<tr>

<td>Blue</td>
<td>B</td>
<td>450 - 530</td>
<td>B2</td>
<td>B2</td>
<td>B1</td>
<td>B3</td>

</tr>

<tr>

<td>Green 1</td>
<td>G1</td>
<td>510 - 550</td>
<td></td>
<td></td>
<td></td>
<td>B11</td>

</tr>

<tr>

<td>Green</td>
<td>G</td>
<td>510 - 600</td>
<td>B3</td>
<td>B3</td>
<td>B2</td>
<td>B4</td>

</tr>

<tr>

<td>Yellow</td>
<td>Y</td>
<td>585 - 625</td>
<td></td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Red</td>
<td>R</td>
<td>620 - 690</td>
<td>B4</td>
<td>B4</td>
<td>B3</td>
<td>B1</td>

</tr>

<tr>

<td>Red Edge 1</td>
<td>RE1</td>
<td>695 - 715</td>
<td>B5</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Red Edge 2</td>
<td>RE2</td>
<td>730 - 750</td>
<td>B6</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Red Edge 3</td>
<td>RE3</td>
<td>765 - 795</td>
<td>B7</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>NIR</td>
<td>N</td>
<td>760 - 900</td>
<td>B8</td>
<td>B5</td>
<td>B4</td>
<td>B2</td>

</tr>

<tr>

<td>NIR 2</td>
<td>N2</td>
<td>850 - 880</td>
<td>B8A</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>Water Vapour</td>
<td>WV</td>
<td>930 - 960</td>
<td>B9</td>
<td></td>
<td></td>
<td></td>

</tr>

<tr>

<td>SWIR 1</td>
<td>S1</td>
<td>1550 - 1750</td>
<td>B11</td>
<td>B6</td>
<td>B5</td>
<td>B6</td>

</tr>

<tr>

<td>SWIR 2</td>
<td>S2</td>
<td>2080 - 2350</td>
<td>B12</td>
<td>B7</td>
<td>B7</td>
<td>B7</td>

</tr>

<tr>

<td>Thermal</td>
<td>T</td>
<td>10400 - 12500</td>
<td></td>
<td></td>
<td>B6</td>
<td></td>

</tr>

<tr>

<td>Thermal 1</td>
<td>T1</td>
<td>10600 - 11190</td>
<td></td>
<td>B10</td>
<td></td>
<td></td>

</tr>

<tr>

<td>Thermal 2</td>
<td>T2</td>
<td>11500 - 12510</td>
<td></td>
<td>B11</td>
<td></td>
<td></td>

</tr>

</table>

In the case of RADAR Indices, the bands follow this standard:

<table>

<tr>

<th> Description </th>
<th> Standard </th>
<th> Sentinel-1 </th>

</tr>

<tr>

<td>Backscattering Coefficient HV</td>
<td>HV</td>
<td>HV</td>

</tr>

<tr>

<td>Backscattering Coefficient VH</td>
<td>VH</td>
<td>VH</td>

</tr>

<tr>

<td>Backscattering Coefficient HH</td>
<td>HH</td>
<td>HH</td>

</tr>

<tr>

<td>Backscattering Coefficient VV</td>
<td>VV</td>
<td>VV</td>

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

# Spectral Indices by Application Domain

"""

nextText = """
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
"""

platformBadges = {
    "MODIS": "![MODIS](https://img.shields.io/badge/-MODIS-green?style=flat-square)",
    "Landsat-457": "![Landsat-457](https://img.shields.io/badge/-Landsat%20457-blueviolet?style=flat-square)",
    "Landsat-89": "![Landsat-89](https://img.shields.io/badge/-Landsat%2089-blue?style=flat-square)",
    "Sentinel-1 (Dual Polarisation VV-VH)": "![Sentinel-1 (Dual Polarisation VV-VH)](https://img.shields.io/badge/-Sentinel%201%20(Dual%20VV%20VH)-lightgray?style=flat-square)",
    "Sentinel-1 (Dual Polarisation HH-HV)": "![Sentinel-1 (Dual Polarisation HH-HV)](https://img.shields.io/badge/-Sentinel%201%20(Dual%20HH%20HV)-gray?style=flat-square)",
    "Sentinel-2": "![Sentinel-2](https://img.shields.io/badge/-Sentinel%202-red?style=flat-square)",
    "Planet-Fusion": "![Planet-Fusion](https://img.shields.io/badge/-Planet%20Fusion-yellow?style=flat-square)",
}

platformBadgesHTML = {
    "MODIS": '<img src="https://img.shields.io/badge/-MODIS-green?style=flat-square" alt="MODIS">',
    "Landsat-TM": '<img src="https://img.shields.io/badge/-Landsat%20TM-blueviolet?style=flat-square" alt="Landsat-TM">',
    "Landsat-ETM+": '<img src="https://img.shields.io/badge/-Landsat%20ETM+-purple?style=flat-square" alt="Landsat-ETM+">',
    "Landsat-OLI": '<img src="https://img.shields.io/badge/-Landsat%20OLI-blue?style=flat-square" alt="Landsat-OLI">',
    "Sentinel-1 (Dual Polarisation VV-VH)": '<img src="https://img.shields.io/badge/-Sentinel%201%20(Dual%20VV%20VH)-lightgray?style=flat-square" alt="(Dual Polarisation VV-VH)">',
    "Sentinel-1 (Dual Polarisation HH-HV)": '<img src="https://img.shields.io/badge/-Sentinel%201%20(Dual%20HH%20HV)-gray?style=flat-square" alt="(Dual Polarisation HH-HV)">',
    "Sentinel-2": '<img src="https://img.shields.io/badge/-Sentinel%202-red?style=flat-square" alt="Sentinel-2">',
    "Planet-Fusion": '<img src="https://img.shields.io/badge/-Planet%20Fusion-yellow?style=flat-square" alt="Planet-Fusion">',
}

letters = list(map(chr, range(65, 91)))


def filterByAppDomain():
    indices = []
    for index, attributes in data["SpectralIndices"].items():
        if attributes["application_domain"] == appDomain:
            indices.append(index)
    return indices


# text = []
# for appDomain in ["vegetation","water","burn","snow","urban","kernel","radar"]:
#    text.append(f"## {appDomain.capitalize()}\n\n")
#    for letter in letters:
#        if any([x.upper().startswith(letter) for x in filterByAppDomain()]):
#            text.append(f"### {letter}\n")
#            for index, attributes in data["SpectralIndices"].items():
#                if attributes['type'] == appDomain:
#                    if index.startswith(letter) or index.startswith(letter.lower()):
#                        line = f"- [{index}]({attributes['reference']}): {attributes['long_name']}."
#                        text.append(line)
#                        for platform, badge in platformBadges.items():
#                            if platform in attributes['platforms']:
#                                text.append(f" {badge} ")
#                        text.append("\n")

text = []
for appDomain in [
    "vegetation",
    "water",
    "burn",
    "snow",
    "urban",
    "soil",
    "kernel",
    "radar",
]:
    text.append(f"\n## {appDomain.capitalize()}\n\n<table>")
    for letter in letters:
        if any([x.upper().startswith(letter) for x in filterByAppDomain()]):
            # text.append(f'\n### {letter}\n<table>')
            for index, attributes in data["SpectralIndices"].items():
                if attributes["application_domain"] == appDomain:
                    if index.startswith(letter) or index.startswith(letter.lower()):
                        link = attributes["reference"]
                        name = attributes["long_name"]
                        line = f'<tr><td width="50%"><a href="{link}" target="_blank">{index}</a>: {name}.</td><td width="50%">'
                        text.append(line)
                        for platform, badge in platformBadgesHTML.items():
                            if platform in attributes["platforms"]:
                                text.append(f" {badge} ")
                        text.append("</td></tr>\n")
    text.append("</table>\n")

with open("README.md", "w") as f:
    f.write(previousText + "".join(text) + nextText)

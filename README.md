# Awesome Spectral Indices for Google Earth Engine [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A ready-to-use curated list of spectral indices for Google Earth Engine.

## Spectral Indices

The ready-to-use curated list of spectral indices is presented in the `spectral-indices-list.json` file. From the `json` file a `csv` file is created: `spectral-indices-list.csv`.
Additionally, the `spectral-indices-dict.json` is created from the original `json` file to be used by the [eemont Python package](https://github.com/davemlz/eemont).

Each element of the list has the following attributes:

- `short_name`: Short name of the index (e.g. `"NDWI"`).
- `long_name`: Long name of the index (e.g. `"Normalized Difference Water Index"`).
- `formula`: Expression/formula of the index (e.g. `"(N - G)/(N + G)"`).
- `bands`: List of required bands/parameters for the index computation (e.g. `["N","G"]`).
- `reference`: Link to the index reference/paper/doi (e.g. `"https://doi.org/10.1080/01431169608948714"`).
- `type`: Type/application of the index (e.g. `"water"`).
- `date_of_addition`: Date of addition to the list (e.g. `"2021-04-07"`).

### Expressions

The formula of the index is presented as a string/expression (e.g. `"(N - R)/(N + R)"`) to be used by the [ee.Image.expression()](https://developers.google.com/earth-engine/apidocs/ee-image-expression) method in [Google Earth Engine](https://earthengine.google.com/). The parameters used in the expression for each index follow this standard:

- `A`: Aerosol band (e.g. B1 of Sentinel-2).
- `B`: Blue band (e.g. B2 of Sentinel-2).
- `G`: Green band (e.g. B3 of Sentinel-2).
- `R`: Red band (e.g. B4 of Sentinel-2).
- `N`: Near Infrared (NIR) band (e.g. B8 of Sentinel-2).
- `RE1`: Red Edge 1 band of Sentinel-2 (B5).
- `RE2`: Red Edge 2 band of Sentinel-2 (B6).
- `RE3`: Red Edge 3 band of Sentinel-2 (B7).
- `RE4`: Red Edge 4 band of Sentinel-2 (B8A).
- `S1`: Shortwave Infrared 1 band (e.g. B11 of Sentinel-2).
- `S2`: Shortwave Infrared 2 band (e.g. B12 of Sentinel-2).
- `T1`: Thermal 1 band (e.g. B10 of Landsat-8).
- `T2`: Thermal 2 band (e.g. B11 of Landsat-8).

Additional index parameters also follow a standard:

- `g`: Gain factor (e.g. Used for EVI).
- `L`: Canopy background adjustment (e.g. Used for SAVI and EVI).
- `C1`: Coefficient 1 for the aerosol resistance term (e.g. Used for EVI).
- `C2`: Coefficient 2 for the aerosol resistance term (e.g. Used for EVI).

The kernel indices are constructed using a special type of parameters:

- `kAB`: Kernel of bands/parameters `A` and `B` (e.g. `kNR` means `k(N,R)`, where `k` is the kernel function).
- `p`: Kernel degree (used for the polynomial kernel).
- `c`: Free parameter that trades off the influence of higher-order versus lower-order terms (used for the polynomial kernel).

## List

Check the full list of spectral indices [here](https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/spectral-indices-list.csv).

## Download Raw Files

You can download or clone the repository:

```
git clone https://github.com/davemlz/awesome-ee-spectral-indices.git
```

Or you can download the single files here (right-click > Save link as...):

- json file: ([Raw list](https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/spectral-indices-list.json), [Raw dict](https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/spectral-indices-dict.json)).
- csv file: [Raw csv](https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/spectral-indices-list.csv).
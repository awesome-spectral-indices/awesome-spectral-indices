# Awesome Spectral Indices for Google Earth Engine [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A ready-to-use curated list of spectral indices for Google Earth Engine.

## Spectral Indices

The ready-to-use curated list of spectral indices ([check the list here](https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/spectral-indices-list.csv)) is presented in the `spectral-indices-list.json` file. From the `json` file a `csv` file is created: `spectral-indices-list.csv`.
Additionally, the `spectral-indices-dict.json` is created from the original `json` file to be used by the [eemont Python package](https://github.com/davemlz/eemont).

### Attributes

Each item of the list has the following attributes:

- `short_name`: Short name of the index (e.g. `"NDWI"`).
- `long_name`: Long name of the index (e.g. `"Normalized Difference Water Index"`).
- `formula`: Expression/formula of the index (e.g. `"(N - G)/(N + G)"`).
- `bands`: List of required bands/parameters for the index computation (e.g. `["N","G"]`).
- `reference`: Link to the index reference/paper/doi (e.g. `"https://doi.org/10.1080/01431169608948714"`).
- `type`: Type/application of the index (e.g. `"water"`).
- `date_of_addition`: Date of addition to the list (e.g. `"2021-04-07"`).
- `contributor`: GitHub user link of the vcontributor (e.g. `"https://github.com/davemlz"`).

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

## How to use the list?

### JavaScript API (Code Editor)

If you want to use the list of spectral indices in the Code Editor, please follow these steps:

1. Accept the `spectral` module [here](https://code.earthengine.google.com/?accept_repo=users/dmlmont/spectral).
2. In a new script, require the spectral module:

```javascript
var spectral = require('users/dmlmont/spectral:spectral');
```

3. Access the indices using the `indices` attribute:

```javascript
print(spectral.indices);
```

4. Access a specific index using dot notation or the classic notation:

```javascript
print(spectral.indices.NDWI);
print(spectral.indices['NDWI']);
```

5. Access the attributes of a specific index:

```javascript
print(spectral.indices.NDWI.long_name);
print(spectral.indices.NDWI.formula);
print(spectral.indices.NDWI.bands);
print(spectral.indices.NDWI.reference);
print(spectral.indices.NDWI.type);
print(spectral.indices.NDWI.date_of_addition);
```

The formula of each index can be used for its computation. Here you can find a tutorial on how to use them and the additional code required to achieve it: [Computing BAIS2 using the Awesome List of Spectral Indices](https://code.earthengine.google.com/15716a9f3e91e454538eebe1dcb5efbe).

### Python API

If you want to use the list of spectral indices in the Python API, please follow these steps:

1. Install [Earth Engine](https://developers.google.com/earth-engine/guides/python_install):

```
pip install earthengine-api
```

2. Install [eemont](https://github.com/davemlz/eemont):

```
pip install eemont
```

3. Open a new Jupyter Notebook or a Python script.
4. Import Earth Engine and eemont:

```python
import ee, eemont
```

5. Authenticate and initialize Earth Engine:

```python
ee.Authenticate()
ee.Initialize()
```

6. The awesome spectral indices list is included in the `.index()` method for `ee.ImageCollection` and `ee.Image` classes extensions:

```python
S2 = (ee.ImageCollection('COPERNICUS/S2_SR')
      .first()
      .maskClouds()
      .scale()
      .index(['NDWI','NDVI','kNDVI']))
```

A list of eemont tutorials of spectral indices computation is shown below:

- [004 Computing Spectral indices for Landsat 8](https://github.com/davemlz/eemont/blob/master/tutorials/004-Computing-Spectral-Indices-Landsat-8.ipynb)
- [005 Computing EVI with Overloaded Operators for Sentinel-2](https://github.com/davemlz/eemont/blob/master/tutorials/005-EVI-with-Overloaded-Operators-Sentinel-2.ipynb)
- [006 NDSI and Snow Cover for Sentinel-2](https://github.com/davemlz/eemont/blob/master/tutorials/006-NDSI-and-Snow-Cover-Sentinel-2-MOD10A2.ipynb)
- [012 Computing Spectral indices for the MOD09GA MODIS Product](https://github.com/davemlz/eemont/blob/master/tutorials/012-Spectral-Indices-MODIS-MOD09GA.ipynb)

### R (rgee)

The instructions to use the list of spectral indices with [rgee](https://github.com/r-spatial/rgee) and [rgeeExtraa](https://github.com/r-earthengine/rgeeExtra) will be here soon!

## Do you want to contribute?

Contributing to the list is pretty simple:

1. **The easiest way:** Open an issue with the following information:

- `short_name`: Short name of the index (e.g. `"NDWI"`).
- `long_name`: Long name of the index (e.g. `"Normalized Difference Water Index"`).
- `formula`: Expression/formula of the index (e.g. `"(N - G)/(N + G)"`).
- `reference`: Link to the index reference/paper/doi (e.g. `"https://doi.org/10.1080/01431169608948714"`).
- `type`: Type/application of the index (e.g. `"water"`).
- `date_of_addition`: Date of addition to the list (e.g. `"2021-04-07"`).
- `contributor`: GitHub user link of the vcontributor (e.g. `"https://github.com/davemlz"`).

    I'll take the information to create a new index, test the index and add it to the list!

2. **The not so hard way:**

    1. Install the required dependencies:
    
        ```
        pydantic
        typing
        py_expression_eval
        ```
    
    2. Fork the repository and clone it to your local machine.
    3. Create a development branch:
    
        ```
        git checkout -b name-of-dev-branch
        ```
    
    4. Open the `indices.py` file: The list of indices is stored in a variable called `indices`. At the end of the file, add a new index (example shown below):
    
        ```python
        indices.append(
            SpectralIndex(
                short_name = 'SeLI',
                long_name = 'Sentinel-2 LAI Green Index',
                formula = '(RE4 - RE1) / (RE4 + RE1)',
                reference = 'https://doi.org/10.3390/s19040904',
                type = 'vegetation',
                date_of_addition = '2021-04-08',
                contributor = "https://github.com/davemlz"
            )
        )
        ```
    
        - The `SpectralIndex` class is a validator created using `pydantic`. This validator *validates* the added data.
        
    5. Test the new index (or indices):
    
        ```
        python test_indices.py
        ```
    
    6. Commit your changes:
    
        ```
        git add .
        git commit -m "short-name-of-the-index ADDED"
        git push origin name-of-dev-branch
        ```
    
    7. Submit a pull request with the tests.
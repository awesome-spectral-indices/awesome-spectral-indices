Awesome Spectral Indices for Google Earth Engine!
=================================================

.. raw:: html

  <embed>
    <p align="center">
      <a href="https://github.com/davemlz/awesome-ee-spectral-indices"><img src="https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/docs/_static/asi.png" alt="Awesome Spectral Indices"></a>
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
    <a href="https://github.com/davemlz/awesome-ee-spectral-indices/actions/workflows/tests.yml" target="_blank">
        <img src="https://github.com/davemlz/awesome-ee-spectral-indices/actions/workflows/tests.yml/badge.svg" alt="Tests">
    </a>
    <a href="https://awesome-ee-spectral-indices.readthedocs.io/en/latest/?badge=latest" target="_blank">
        <img src="https://readthedocs.org/projects/awesome-ee-spectral-indices/badge/?version=latest" alt="Documentation">
    </a>
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
  </embed>

.. toctree::   
   :maxdepth: 2
   :caption: Contents
   :hidden:
   
   list   
   contributing

Spectral Indices
--------------------

The ready-to-use curated list of spectral indices 
(`check the list here <https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-table.csv>`_) for remote sensing applications 
is presented here. The list is available in two formats 
(`CSV <https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-table.csv>`_, 
`JSON <https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-dict.json>`_) so it can be easily used in any 
programming language.

Attributes
~~~~~~~~~~~~~~~~

Each item of the list has the following attributes:

- :code:`short_name`: Short name of the index (e.g. :code:`"NDWI"`).
- :code:`long_name`: Long name of the index (e.g. :code:`"Normalized Difference Water Index"`).
- :code:`formula`: Expression/formula of the index (e.g. :code:`"(G - N)/(G + N)"`).
- :code:`bands`: List of required bands/parameters for the index computation (e.g. :code:`["N","G"]`).
- :code:`reference`: Link to the index reference/paper/doi (e.g. :code:`"https://doi.org/10.1080/01431169608948714"`).
- :code:`type`: Type/application of the index (e.g. :code:`"water"`).
- :code:`date_of_addition`: Date of addition to the list (e.g. :code:`"2021-04-07"`).
- :code:`contributor`: GitHub user link of the contributor (e.g. :code:`"https://github.com/davemlz"`).

Expressions
~~~~~~~~~~~~~~~~

The formula of the index is presented as a string/expression (e.g. :code:`"(N - R)/(N + R)"`) that can be easily evaluated. The parameters used in the expression for each index follow this standard:

.. list-table:: Standard variables for spectral indices expressions and satellite equivalents.   
   :header-rows: 1

   * - Description
     - Standard     
     - Sentinel-2
     - Landsat 8
     - Landsat 457
     - MODIS     
   * - Aerosols
     - A
     - B1
     - B1
     -
     -     
   * - Blue
     - B
     - B2
     - B2
     - B1
     - B3 
   * - Green
     - G
     - B3
     - B3
     - B2
     - B4    
   * - Red
     - R
     - B4
     - B4
     - B3
     - B1
   * - Red Edge 1
     - RE1
     - B5
     - 
     -
     -     
   * - Red Edge 2
     - RE2
     - B6
     - 
     -
     -     
   * - Red Edge 3
     - RE3
     - B7
     - 
     -
     -     
   * - Red Edge 4
     - RE4
     - B8A
     - 
     -
     -     
   * - NIR
     - N
     - B8
     - B5
     - B4
     - B2
   * - SWIR 1
     - S1
     - B11
     - B6
     - B5
     - B6     
   * - SWIR 2
     - S2
     - B12
     - B7
     - B7
     - B7   
   * - Thermal 1
     - T1
     - 
     - B10
     - B6
     -     
   * - Thermal 2
     - T2
     - 
     - B11
     - 
     -    

Additional index parameters also follow a standard:

- :code:`g`: Gain factor (e.g. Used for EVI).
- :code:`L`: Canopy background adjustment (e.g. Used for SAVI and EVI).
- :code:`C1`: Coefficient 1 for the aerosol resistance term (e.g. Used for EVI).
- :code:`C2`: Coefficient 2 for the aerosol resistance term (e.g. Used for EVI).
- :code:`cexp`: Exponent used for OCVI.
- :code:`nexp`: Exponent used for GDVI.
- :code:`alpha`: Weighting coefficient used for WDRVI.
- :code:`sla`: Soil line slope.
- :code:`slb`: Soil line intercept.

The kernel indices are constructed using a special type of parameters:

- :code:`kAB`: Kernel of bands/parameters `A` and `B` (e.g. `kNR` means `k(N,R)`, where `k` is the kernel function).
- :code:`p`: Kernel degree (used for the polynomial kernel).
- :code:`c`: Free parameter that trades off the influence of higher-order versus lower-order terms (used for the polynomial kernel).

Used by
---------

JavaScript
~~~~~~~~~~

- `spectral <https://github.com/davemlz/spectral>`_: Awesome Spectral Indices for the Google Earth Engine JavaScript API (Code Editor).

Python
~~~~~~

- `eemont <https://github.com/davemlz/eemont>`_: A python package that extends Google Earth Engine.
- `eeExtra <https://github.com/r-earthengine/ee_extra>`_: A ninja Python package behind rgee, rgeeExtra and eemont.
- `spnydex <https://github.com/davemlz/spyndex>`_: Awesome Spectral Indices in Python.

R
~

- `rgeeExtra <https://github.com/r-earthengine/rgeeExtra>`_: High-level functions to process spatial and simple Earth Engine objects. Popular Third-party GEE algorithms are re-coded from Javascript and Python to R.

List
-------

Check the full list of spectral indices `here <https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-table.csv>`_.

Download Raw Files
------------------------

You can download or clone the repository:

.. code-block::

    git clone https://github.com/davemlz/awesome-ee-spectral-indices.git

Or you can download the single files here (right-click > Save link as...):

- JSON: `Raw list <https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-dict.json>`_
- CSV: `Raw list <https://raw.githubusercontent.com/davemlz/awesome-ee-spectral-indices/main/output/spectral-indices-table.csv>`_

Credits
------------------------

- `César Aybar <https://github.com/csaybar>`_: The formidable `pydantic <https://github.com/samuelcolvin/pydantic/>`_ expert and creator of `rgee <https://github.com/r-spatial/rgee>`_.
Awesome Spectral Indices for Google Earth Engine!
=================================================

.. image:: https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg
        :target: https://github.com/sindresorhus/awesome
        
.. image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/davemlz/5e9f08fa6a45d9d486e29d9d85ad5c84/raw/spectral.json
        :target: https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-dict.json
        
.. image:: https://github.com/davemlz/awesome-ee-spectral-indices/actions/workflows/tests.yml/badge.svg
        :target: https://github.com/davemlz/awesome-ee-spectral-indices/actions/workflows/tests.yml

.. image:: https://img.shields.io/github/stars/davemlz/awesome-ee-spectral-indices?style=social
        :alt: GitHub Repo stars
        
.. image:: https://readthedocs.org/projects/awesome-ee-spectral-indices/badge/?version=latest
        :target: https://awesome-ee-spectral-indices.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

**A ready-to-use curated list of spectral indices for Google Earth Engine.**

Spectral Indices
--------------------

The ready-to-use curated list of spectral indices (`check the list here <https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-dict.json>`_) is presented in the `spectral-indices-dict.json` file. This file is used by the `eemont Python package <https://github.com/davemlz/eemont>`_ in order to compute spectral indices (Python API) and by the `spectral module <https://code.earthengine.google.com/?accept_repo=users/dmlmont/spectral>`_ in order to access the spectral indices in the Code Editor (JavaScript API).

Attributes
~~~~~~~~~~~~~~~~

Each item of the list has the following attributes:

- :code:`short_name`: Short name of the index (e.g. :code:`"NDWI"`).
- :code:`long_name`: Long name of the index (e.g. :code:`"Normalized Difference Water Index"`).
- :code:`formula`: Expression/formula of the index (e.g. :code:`"(N - G)/(N + G)"`).
- :code:`bands`: List of required bands/parameters for the index computation (e.g. :code:`["N","G"]`).
- :code:`reference`: Link to the index reference/paper/doi (e.g. :code:`"https://doi.org/10.1080/01431169608948714"`).
- :code:`type`: Type/application of the index (e.g. :code:`"water"`).
- :code:`date_of_addition`: Date of addition to the list (e.g. :code:`"2021-04-07"`).
- :code:`contributor`: GitHub user link of the contributor (e.g. :code:`"https://github.com/davemlz"`).

Expressions
~~~~~~~~~~~~~~~~

The formula of the index is presented as a string/expression (e.g. `"(N - R)/(N + R)"`) to be used by the `ee.Image.expression() <https://developers.google.com/earth-engine/apidocs/ee-image-expression>`_ method in `Google Earth Engine <https://earthengine.google.com/>`_. The parameters used in the expression for each index follow this standard:

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

The kernel indices are constructed using a special type of parameters:

- :code:`kAB`: Kernel of bands/parameters `A` and `B` (e.g. `kNR` means `k(N,R)`, where `k` is the kernel function).
- :code:`p`: Kernel degree (used for the polynomial kernel).
- :code:`c`: Free parameter that trades off the influence of higher-order versus lower-order terms (used for the polynomial kernel).

List
-------

Check the full list of spectral indices `here <https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-dict.json>`_.

Download Raw Files
------------------------

You can download or clone the repository:

.. code-block::

    git clone https://github.com/davemlz/awesome-ee-spectral-indices.git

Or you can download the single file here (right-click > Save link as...):

- json file: `Raw list <https://github.com/davemlz/awesome-ee-spectral-indices/blob/main/output/spectral-indices-dict.json>`_

Credits
------------------------

- `César Aybar <https://github.com/csaybar>`_: The formidable `pydantic <https://github.com/samuelcolvin/pydantic/>`_ expert and creator of `rgee <https://github.com/r-spatial/rgee>`_.
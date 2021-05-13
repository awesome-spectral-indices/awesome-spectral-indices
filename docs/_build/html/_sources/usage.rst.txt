How to use the list?
=======================

JavaScript API (Code Editor)
--------------------------------

If you want to use the list of spectral indices in the Code Editor, please follow these steps:

1. Accept the `spectral` module `here <https://code.earthengine.google.com/?accept_repo=users/dmlmont/spectral>`_.
2. In a new script, require the spectral module:

.. code-block:: javascript

    var spectral = require('users/dmlmont/spectral:spectral');

3. Access the indices using the `indices` attribute:

.. code-block:: javascript

    print(spectral.indices);

4. Access a specific index using dot notation or the classic notation:

.. code-block:: javascript

    print(spectral.indices.NDWI);
    print(spectral.indices['NDWI']);

5. Access the attributes of a specific index:

.. code-block:: javascript

    print(spectral.indices.NDWI.long_name);
    print(spectral.indices.NDWI.formula);
    print(spectral.indices.NDWI.bands);
    print(spectral.indices.NDWI.reference);
    print(spectral.indices.NDWI.type);
    print(spectral.indices.NDWI.date_of_addition);
    print(spectral.indices.NDWI.contributor);

The formula of each index can be used for its computation. Here you can find a tutorial on how to use them and the additional code required to achieve it: `Computing BAIS2 using the Awesome List of Spectral Indices <https://code.earthengine.google.com/15716a9f3e91e454538eebe1dcb5efbe>`_.

Python API
--------------------------------

If you want to use the list of spectral indices in the Python API, please follow these steps:

1. Install `Earth Engine <https://developers.google.com/earth-engine/guides/python_install>`_:

.. code-block:: 

    pip install earthengine-api

2. Install `eemont <https://github.com/davemlz/eemont>`_:

.. code-block::

    pip install eemont

3. Open a new Jupyter Notebook or a Python script.
4. Import Earth Engine and eemont:

.. code-block:: python

    import ee, eemont

5. Authenticate and initialize Earth Engine:

.. code-block:: python

    ee.Authenticate()
    ee.Initialize()

6. The awesome spectral indices list is included in the `.index()` method for `ee.ImageCollection` and `ee.Image` classes extensions:

.. code-block:: python

    S2 = (ee.ImageCollection('COPERNICUS/S2_SR')
          .first()
          .maskClouds()
          .scale()
          .index(['NDWI','NDVI','kNDVI']))

A list of eemont tutorials of spectral indices computation is shown below:

- `004 Computing Spectral indices for Landsat 8 <https://github.com/davemlz/eemont/blob/master/tutorials/004-Computing-Spectral-Indices-Landsat-8.ipynb>`_
- `005 Computing EVI with Overloaded Operators for Sentinel-2 <https://github.com/davemlz/eemont/blob/master/tutorials/005-EVI-with-Overloaded-Operators-Sentinel-2.ipynb>`_
- `006 NDSI and Snow Cover for Sentinel-2 <https://github.com/davemlz/eemont/blob/master/tutorials/006-NDSI-and-Snow-Cover-Sentinel-2-MOD10A2.ipynb>`_
- `012 Computing Spectral indices for the MOD09GA MODIS Product <https://github.com/davemlz/eemont/blob/master/tutorials/012-Spectral-Indices-MODIS-MOD09GA.ipynb>`_

R (rgee)
--------------------------------

The instructions to use the list of spectral indices with `rgee <https://github.com/r-spatial/rgee>`_ and `rgeeExtra <https://github.com/r-earthengine/rgeeExtra>`_ will be here soon!
Do you want to contribute?
==============================

Contributing to the list is pretty simple:

The easiest way
-------------------------------

Open an issue with the following information:

- :code:`short_name`: Short name of the index (e.g. :code:`"NDWI"`).
- :code:`long_name`: Long name of the index (e.g. :code:`"Normalized Difference Water Index"`).
- :code:`formula`: Expression/formula of the index (e.g. :code:`"(N - G)/(N + G)"`).
- :code:`reference`: Link to the index reference/paper/doi (e.g. :code:`"https://doi.org/10.1080/01431169608948714"`).
- :code:`type`: Type/application of the index (e.g. :code:`"water"`).
- :code:`date_of_addition`: Date of addition to the list (e.g. :code:`"2021-04-07"`).
- :code:`contributor`: GitHub user link of the vcontributor (e.g. :code:`"https://github.com/davemlz"`).

For the formula attribute, the standard variables for spectral indices expressions must be followed:

.. list-table:: Standard variables for bands and parameters.   
   :header-rows: 1

   * - Description
     - Standard  
   * - Aerosols
     - A
   * - Blue
     - B
   * - Green
     - G    
   * - Red
     - R
   * - Red Edge 1
     - RE1 
   * - Red Edge 2
     - RE2 
   * - Red Edge 3
     - RE3 
   * - Red Edge 4
     - RE4 
   * - NIR
     - N
   * - SWIR 1
     - S1     
   * - SWIR 2
     - S2   
   * - Thermal 1
     - T1  
   * - Thermal 2
     - T2
   * - Gain Factor
     - g
   * - Canopy Background Adjustment
     - L
   * - Coefficient 1 for the aerosol resistance term
     - C1
   * - Coefficient 2 for the aerosol resistance term
     - C2
   * - c exponent for OCVI.
     - cexp
   * - k(A,B)
     - kAB

We'll take the information to create a new index, test the index and add it to the list!

The not so hard way
-------------------------------

1. Install the required dependencies:

.. code-block::

    pydantic
    typing
    orjson
    py_expression_eval

2. Fork the repository and clone it to your local machine.
3. Create a development branch:

.. code-block::

    git checkout -b name-of-dev-branch        

4. Open the `src/indices.py` file: The list of indices is stored in a DataClass called `SpectralIndices`. At the end of the file, add a new index (example shown below):

.. code-block:: python

    SeLI=SpectralIndex(
        short_name='SeLI',
        long_name='Sentinel-2 LAI Green Index',
        formula='(RE4 - RE1) / (RE4 + RE1)',
        reference='https://doi.org/10.3390/s19040904',
        type='vegetation',
        date_of_addition='2021-04-08',
        contributor="https://github.com/davemlz"
    )

- The `SpectralIndex` class is a validator created using `pydantic`. This validator *validates* the added data.

.. important::
   The formula must follow the standard variables for each band or parameter.

5. Test the new index (or indices):

.. code-block:: python

    python test/test_indices.py        

6. Commit your changes:

.. code-block::

    git add .
    git commit -m "short-name-of-the-index ADDED"
    git push origin name-of-dev-branch

7. Submit a pull request with the tests.
# Contributing

Contributing to the catalogue is straightforward. You can propose an index
through a GitHub issue or add it directly in a code contribution.

Before proposing a new index, read the
[AI and Scientific Validation Policy](AI%20POLICY.md).

## The easiest way

Open a [new spectral index issue](https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=new-spectral-index.md)
with the following information:

- `short_name`: Short name of the index, such as `"NDWI"`.
- `long_name`: Long name of the index, such as `"Normalized Difference Water Index"`.
- `formula`: Expression for the index, such as `"(N - G)/(N + G)"`.
- `reference`: Link to the index reference, paper, or DOI.
- `application_domain`: One of `vegetation`, `burn`, `water`, `snow`,
  `urban`, `soil`, `clouds`, `kernel`, or `radar`.
- `date_of_addition`: Date of addition in `YYYY-MM-DD` format.
- `contributor`: GitHub profile URL or email address.

The formula must use the standard variables supported by the catalogue.
Common variables include:

| Description | Standard |
| --- | --- |
| Aerosols | `A` |
| Blue | `B` |
| Green 1 | `G1` |
| Green | `G` |
| Yellow | `Y` |
| Red | `R` |
| Red Edge 1 | `RE1` |
| Red Edge 2 | `RE2` |
| Red Edge 3 | `RE3` |
| NIR | `N` |
| NIR 2 | `N2` |
| Water vapour | `WV` |
| SWIR 1 | `S1` |
| SWIR 2 | `S2` |
| Thermal | `T` |
| Thermal 1 | `T1` |
| Thermal 2 | `T2` |
| Gain factor | `g` |
| Canopy background adjustment | `L` |
| Coefficient 1 for the aerosol resistance term | `C1` |
| Coefficient 2 for the aerosol resistance term | `C2` |
| Exponent used for OCVI | `cexp` |
| Exponent used for GDVI | `nexp` |
| Weighting coefficient used for WDRVI | `alpha` |
| Weighting coefficient used for ARVI | `gamma` |
| Weighting coefficient used for MBWI | `omega` |
| Soil line slope | `sla` |
| Soil line intercept | `slb` |
| Photosynthetically Active Radiation | `PAR` |
| Slope parameter by soil used for NIRvH2 | `k` |
| NIR central wavelength | `lambdaN` |
| Red central wavelength | `lambdaR` |
| Green central wavelength | `lambdaG` |
| Kernel of variables A and B | `kAB` |

The complete, authoritative list is defined by the `Bands` enum in
[`src/utils.py`](src/utils.py).

## Contributing through code

1. Fork and clone the repository.

2. Create and activate an isolated Python environment. For example, with
   Conda:

   ```bash
   conda create --name asi-dev python=3.10
   conda activate asi-dev
   python -m pip install -r requirements-test.txt
   ```

   Alternatively, using Python's built-in `venv`:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install -r requirements-test.txt
   ```

   On Windows, activate the virtual environment with
   `.venv\Scripts\activate`.

3. Create a development branch:

   ```bash
   git switch -c name-of-development-branch
   ```

4. Add the index to the `SpectralIndices` catalogue in
   [`src/indices.py`](src/indices.py):

   ```python
   SeLI = SpectralIndex(
       short_name="SeLI",
       long_name="Sentinel-2 LAI Green Index",
       formula="(N2 - RE1) / (N2 + RE1)",
       reference="https://doi.org/10.3390/s19040904",
       application_domain="vegetation",
       date_of_addition="2021-04-08",
       contributor="https://github.com/davemlz",
   )
   ```

   `SpectralIndex` is a Pydantic model that validates the submitted metadata
   and formula. The formula must use supported bands and parameters.

5. Run the tests:

   ```bash
   pytest test
   ```

6. Commit and push the changes:

   ```bash
   git add src/indices.py
   git commit -m "Add short-name-of-the-index"
   git push origin name-of-development-branch
   ```

7. Submit a pull request with the test results and scientific reference.

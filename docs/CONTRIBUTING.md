# Contributing

Thank you for helping improve Awesome Spectral Indices. You can propose a new
index through a GitHub issue or add it directly through a code contribution.

The catalogue is currently being migrated to v1. The v1 schema is
experimental and may continue to change; its current structure and validation
rules are documented in
[v1 Explained](https://awesome-spectral-indices.github.io/awesome-spectral-indices/v1.html).

Before proposing an index, read the
[AI and Scientific Validation Policy](https://github.com/awesome-spectral-indices/awesome-spectral-indices/blob/main/AI%20POLICY.md).

## The easiest way

Open a
[new spectral index issue](https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=new-spectral-index.md)
and provide, at minimum:

- the index acronym and full name;
- the published formula;
- a link to the original scientific source;
- the application domain;
- your GitHub profile URL or email address; and
- any constant descriptions and values required by the formula.

The issue does not need to reproduce every generated catalogue property.
Sensing modalities, bands, polarizations, source status, publication metadata,
citations, and other derived fields are added automatically.

## Contributing through code

### 1. Prepare the repository

Fork and clone the repository, then create a development branch:

```bash
git switch -c add-name-of-index
```

Create and activate an isolated Python environment. With Conda:

```bash
conda create --name asi-dev python=3.10
conda activate asi-dev
python -m pip install -r requirements-test.txt
```

Alternatively, use Python's built-in `venv`:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-test.txt
```

On Windows, activate the virtual environment with
`.venv\Scripts\activate`.

### 2. Add the v1 index definition

Add the index to the `SpectralIndices` mapping in
[`src/v1/indices.py`](https://github.com/awesome-spectral-indices/awesome-spectral-indices/blob/main/src/v1/indices.py):

```python
SeLI = SpectralIndex(
    acronym="SeLI",
    name="Sentinel-2 LAI Green Index",
    formula="(N2 - RE1) / (N2 + RE1)",
    source={
        "source_link": "https://doi.org/10.3390/s19040904",
    },
    classification={
        "application_domain": "vegetation",
    },
    date_of_addition="2021-04-08",
    contributor="https://github.com/davemlz",
)
```

The Python mapping key is the case-sensitive catalogue identifier. It does not
have to equal `acronym`, although using the acronym is normally the clearest
choice. Acronyms and names do not have to be unique.

The required contributor-provided properties are:

| Property | What to provide |
| --- | --- |
| `acronym` | Display acronym |
| `name` | Full index name |
| `formula` | Published formula using supported v1 syntax |
| `source.source_link` | Original HTTP(S) source, preferably a DOI when available |
| `classification.application_domain` | `vegetation`, `water`, `burn`, `snow`, `urban`, `soil`, `geology`, or `clouds` |
| `date_of_addition` | Contribution date in `YYYY-MM-DD` format |
| `contributor` | GitHub profile URL or email address |

`classification.family` is optional and currently accepts `kernel`,
`tasseled_cap`, and `radar`. Do not provide `sensing_modalities`; they are
generated from the formula inputs.

### 3. Describe constants when needed

If the formula uses a registered constant, add a `constants` object with a
description for that constant. A numeric default is optional:

```python
constants={
    "L": {
        "description": "Canopy background adjustment",
        "default_value": 0.5,
    },
}
```

The index definition must describe every constant it uses and cannot include
unused constants. Optional `suggested_values` and `suggested_range` metadata
may be added when supported by the scientific source.

External variables use a similar `external_variables` object, but require only
a description. Contextual `spatial_max()`, `spatial_min()`, and
`spatial_mean()` calls require a matching `reductions` definition. See
[v1 Explained](https://awesome-spectral-indices.github.io/awesome-spectral-indices/v1.html)
for examples.

### 4. Use supported formula syntax

Broad spectral and thermal bands use standards such as `B`, `G`, `R`, `N`,
`S1`, and `T1`. Radar formulas use `HH`, `HV`, `VH`, or `VV`.
Hyperspectral inputs use either an exact integer wavelength such as `R720` or a
selectable inclusive range such as `R750_800`; wavelengths must be between 300
and 2500 nm.

V1 formulas currently support arithmetic plus `min()`, `max()`, `tanh()`,
`log()`, `kernel()`, `spatial_max()`, `spatial_min()`, and `spatial_mean()`.
The generated
[README](https://github.com/awesome-spectral-indices/awesome-spectral-indices#formula-expressions)
contains the current standards and index-specific constant descriptions.

### 5. Validate the contribution

Run the v1 tests:

```bash
python -m pytest test/v1
```

Generated JSON, CSV, bibliography, README, and website pages are refreshed by
repository automation. Do not edit generated catalogue fields by hand.

### 6. Submit the change

Commit and push your source definition:

```bash
git add src/v1/indices.py
git commit -m "Add acronym-of-index"
git push origin add-name-of-index
```

Open a pull request and include the scientific source plus the test result.

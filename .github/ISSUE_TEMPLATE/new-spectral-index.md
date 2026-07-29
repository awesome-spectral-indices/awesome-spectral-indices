---
name: New Spectral Index
about: Suggest a new Spectral Index
title: 'NEW INDEX: short-name-of-index (long-name-of-index)'
labels: NEW INDEX
assignees: ''

---

Please, complete the following information:

Before submitting, review the
[Contribution Guidelines](https://github.com/awesome-spectral-indices/awesome-spectral-indices/blob/main/CONTRIBUTING.md)
and the
[AI and Scientific Validation Policy](https://github.com/awesome-spectral-indices/awesome-spectral-indices/blob/main/AI%20POLICY.md).

## Index definition

```python
short-name-of-index=SpectralIndex(
    short_name='short-name-of-index',
    long_name='long-name-of-index',
    formula='expression-formula (please see the README for more info)',
    reference='link-to-original-reference-or-doi',
    application_domain='one of [vegetation, burn, water, snow, urban, soil, clouds, kernel, radar]',
    date_of_addition='yyyy-mm-dd',
    contributor="github-user-page"
)
```

Example:

```python
SeLI=SpectralIndex(
    short_name='SeLI',
    long_name='Sentinel-2 LAI Green Index',
    formula='(N2 - RE1) / (N2 + RE1)',
    reference='https://doi.org/10.3390/s19040904',
    application_domain='vegetation',
    date_of_addition='2021-04-08',
    contributor="https://github.com/davemlz"
)
```

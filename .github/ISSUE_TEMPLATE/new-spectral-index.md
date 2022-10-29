---
name: New Spectral Index
about: Suggest a new Spectral Index
title: 'NEW INDEX: short-name-of-index'
labels: NEW INDEX
assignees: ''

---

Please, complete the following information:

```python
short-name-of-index=SpectralIndex(
    short_name='short-name-of-index',
    long_name='long-name-of-index',
    formula='expression-formula (please see the README for more info)',
    reference='link-to-reference-doi-paper',
    application_domain='type-of-index (one of [vegetation, burn, water, drought, snow, kernel])',
    date_of_addition='yyyy-mm-dd',
    contributor="github-user-page"
)
```

Example:

```python
SeLI=SpectralIndex(
    short_name='SeLI',
    long_name='Sentinel-2 LAI Green Index',
    formula='(RE4 - RE1) / (RE4 + RE1)',
    reference='https://doi.org/10.3390/s19040904',
    application_domain='vegetation',
    date_of_addition='2021-04-08',
    contributor="https://github.com/davemlz"
)
```

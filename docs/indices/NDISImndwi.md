---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "NDISImndwi"
  text: "Normalized Difference Impervious Surface Index with MNDWI"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.14358/PERS.76.5.557"
---

## Formula

```
(T - (((G - S1)/(G + S1)) + N + S1) / 3.0)/(T + (((G - S1)/(G + S1)) + N + S1) / 3.0)
```

### Classification

- Application domain: `Urban`
- Sensing modalities: `Multispectral`, `Thermal`

### Bands

- `T`: Thermal Infrared.
- `G`: Green.
- `S1`: Short-wave Infrared (SWIR) 1.
- `N`: Near-Infrared (NIR).

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`NDISIr`](/indices/NDISIr)
- [`NDISIg`](/indices/NDISIg)
- [`NDISIb`](/indices/NDISIb)
- [`NDISIndwi`](/indices/NDISIndwi)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-18.

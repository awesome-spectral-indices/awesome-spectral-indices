---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MCARI2"
  text: "Modified Chlorophyll Absorption in Reflectance Index 2"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2003.12.013"
---

## Formula

```
(1.5 * (2.5 * (N - R) - 1.3 * (N - G))) / ((((2.0 * N + 1) ** 2) - (6.0 * N - 5 * (R ** 0.5)) - 0.5) ** 0.5)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `G`: Green.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`MCARI1`](/indices/MCARI1)
- [`MTVI1`](/indices/MTVI1)
- [`MTVI2`](/indices/MTVI2)

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

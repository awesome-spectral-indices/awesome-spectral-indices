---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDLI"
  text: "Normalized Difference Lignin Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(02)00011-1"
---

## Formula

```
(log(1.0 / R1754) - log(1.0 / R1680))/(log(1.0 / R1754) + log(1.0 / R1680))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Hyperspectral`

### Bands

- `R1754`: Reflectance at 1754 nm.
- `R1680`: Reflectance at 1680 nm.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`NDNI`](/indices/NDNI)

## Contributor

Index contributed by https://github.com/MartinuzziFrancesco on 2026-08-08.

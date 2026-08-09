---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-snow"

hero:
  name: "NDISI"
  text: "Normalized Difference Ice-Snow Index"
  tagline: "Snow"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1029/2021JD035742"
---

## Formula

```
(R1080_1120 - R1760_1800)/(R1080_1120 + R1760_1800)
```

### Classification

- Application domain: `Snow`
- Sensing modalities: `Hyperspectral`

### Bands

- `R1080_1120`: Reflectance at one selected wavelength from 1080 to 1120 nm, inclusive.
- `R1760_1800`: Reflectance at one selected wavelength from 1760 to 1800 nm, inclusive.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/MartinuzziFrancesco on 2026-08-09.

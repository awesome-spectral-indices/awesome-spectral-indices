---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-snow"

hero:
  name: "NDSIITM"
  text: "Normalized Difference Snow/Ice Index for Landsat TM"
  tagline: "Snow"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/01431160119766"
---

## Formula

```
(R - S1)/(R + S1)
```

### Classification

- Application domain: `Snow`
- Sensing modalities: `Multispectral`

### Bands

- `R`: Red.
- `S1`: Short-wave Infrared (SWIR) 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`NDSaII`](/indices/NDSaII)

## Contributor

Index contributed by https://github.com/davemlz on 2026-01-10.

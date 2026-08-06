---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "NBLIOLI"
  text: "Normalized Difference Bare Land Index for Landsat-OLI"
  tagline: "Soil"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs9030249"
---

## Formula

```
(R - T1)/(R + T1)
```

### Classification

- Application domain: `Soil`
- Sensing modalities: `Multispectral`, `Thermal`

### Bands

- `R`: Red.
- `T1`: Thermal Infrared 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`NBLI`](/indices/NBLI)

## Contributor

Index contributed by https://github.com/davemlz on 2023-03-12.

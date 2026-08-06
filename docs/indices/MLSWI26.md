---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "MLSWI26"
  text: "Modified Land Surface Water Index (MODIS Bands 2 and 6)"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs71215805"
---

## Formula

```
(1.0 - N - S1)/(1.0 - N + S1)
```

### Classification

- Application domain: `Water`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`MLSWI27`](/indices/MLSWI27)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-20.

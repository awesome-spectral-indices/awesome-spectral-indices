---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SNDTI4RE"
  text: "4-band Red Edge Soil-Adjusted Normalized Difference Tillage Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/j.jag.2022.102793"
---

## Formula

```
gamma * ((S1 - S2) * 2.0)/(S1 + S2 + 1.0) + (1 - gamma) * ((N - RE3) * 2.0)/(N + RE3 + 1.0)
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.
- `N`: Near-Infrared (NIR).
- `RE3`: Red Edge 3.

### Constants

- `gamma`: Weighting coefficient used for ARVI. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2025-09-30.

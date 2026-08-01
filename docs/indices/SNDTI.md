---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SNDTI"
  text: "Soil-Adjusted Normalized Difference Tillage Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/22797254.2017.1418186"
---

## Formula

```
(1.0 + L) * (S1 - S2) / (S1 + S2 + L)
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

- `L`: Canopy background adjustment. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2025-10-11.

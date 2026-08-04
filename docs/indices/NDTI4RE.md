---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDTI4RE"
  text: "4-band Red Edge Normalized Difference Tillage Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2022.102793"
---

## Formula

```
gamma * (S1 - S2)/(S1 + S2) + (1 - gamma) * (N - RE3)/(N + RE3)
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.
- `N`: Near-Infrared (NIR).
- `RE3`: Red Edge 3.

### Constants

- `gamma`: Weighting coefficient for the ratio SWIR1/SWIR2 (Sentinel-2). Default: `0.4`. Suggested range: `0.0`–`1.0`. Suggested values: April: `0.4`; November: `0.5`.

## Contributor

Index contributed by https://github.com/davemlz on 2025-09-30.

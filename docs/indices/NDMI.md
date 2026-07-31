---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDMI"
  text: "Normalized Difference Moisture Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/S0034-4257(01)00318-2"
---

## Formula

```
(N - S1)/(N + S1)
```

### Bands

- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/bpurinton on 2021-12-01.

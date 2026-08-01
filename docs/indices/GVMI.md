---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GVMI"
  text: "Global Vegetation Moisture Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(02)00037-8"
---

## Formula

```
((N + 0.1) - (S2 + 0.02)) / ((N + 0.1) + (S2 + 0.02))
```

### Bands

- `N`: Near-Infrared (NIR).
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

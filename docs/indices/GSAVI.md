---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GSAVI"
  text: "Green Soil Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.2134/agronj2004.0314"
---

## Formula

```
(1.0 + L) * (N - G) / (N + G + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.

### Constants

- `L`: Canopy background adjustment. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

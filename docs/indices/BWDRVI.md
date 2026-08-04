---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "BWDRVI"
  text: "Blue Wide Dynamic Range Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.2135/cropsci2007.01.0031"
---

## Formula

```
(alpha * N - B) / (alpha * N + B)
```

### Bands

- `N`: Near-Infrared (NIR).
- `B`: Blue.

### Constants

- `alpha`: NIR reflectance scalar. Default: `0.01`. Suggested values: Dense biomass/High yield: `0.01`; Low-to-moderate biomass: `0.1`; Moderate biomass: `0.05`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-20.

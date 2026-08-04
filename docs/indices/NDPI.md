---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDPI"
  text: "Normalized Difference Phenology Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2017.04.031"
---

## Formula

```
(N - (alpha * R + (1.0 - alpha) * S1))/(N + (alpha * R + (1.0 - alpha) * S1))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

- `alpha`: Weighting coefficient. Default: `0.74`. Suggested range: `0.0`–`1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-20.

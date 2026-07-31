---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "EVI2"
  text: "Two-Band Enhanced Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/j.rse.2008.06.006"
---

## Formula

```
g * (N - R) / (N + 2.4 * R + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `g`: Gain factor. Default: `2.5`.
- `L`: Canopy background adjustment. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

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
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2008.06.006"
---

## Formula

```
g * (N - R) / (N + (C1 - (C2 / c)) * R + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `C1`: Coefficient 1 for the aerosol resistance term. Default: `6.0`.
- `C2`: Coefficient 2 for the aerosol resistance term. Default: `7.5`.
- `L`: Canopy background adjustment. Default: `1.0`.
- `c`: Ratio of red to blue reflectances. Red = c * Blue. Default: `2.08`.
- `g`: Gain factor. Default: `2.5`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

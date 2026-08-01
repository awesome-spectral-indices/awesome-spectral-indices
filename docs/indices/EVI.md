---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "EVI"
  text: "Enhanced Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(96)00112-5"
---

## Formula

```
g * (N - R) / (N + C1 * R - C2 * B + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Constants

- `g`: Gain factor. Default: `2.5`.
- `C1`: Coefficient 1 for the aerosol resistance term. Default: `6.0`.
- `C2`: Coefficient 2 for the aerosol resistance term. Default: `7.5`.
- `L`: Canopy background adjustment. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

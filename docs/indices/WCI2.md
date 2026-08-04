---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WCI2"
  text: "Wheat Canopy Index (Growth Stage 2)"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.mlwa.2026.100914"
---

## Formula

```
-1.0 * ((B + G + RE1)/(R + epsilon)) * ((B + R + RE1)/(N + epsilon))
```

### Bands

- `B`: Blue.
- `G`: Green.
- `RE1`: Red Edge 1.
- `R`: Red.
- `N`: Near-Infrared (NIR).

### Constants

- `epsilon`: Adjustment constant for numerical stability. Default: `1e-10`.

## Contributor

Index contributed by https://github.com/davemlz on 2026-05-27.

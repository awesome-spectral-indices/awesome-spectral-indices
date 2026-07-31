---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WCI1"
  text: "Wheat Canopy Index (Growth Stage 1)"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/j.mlwa.2026.100914"
---

## Formula

```
-1.0 * ((B - R + RE1)/(B + R + RE1 + epsilon)) * ((G + R)/(B + N + epsilon))
```

### Bands

- `B`: Blue.
- `R`: Red.
- `RE1`: Red Edge 1.
- `G`: Green.
- `N`: Near-Infrared (NIR).

### Constants

- `epsilon`: Adjustment constant used for EBI, WC1 and WC2. For WCx indices use epsilon = 1e-10. Default: `1`.

## Contributor

Index contributed by https://github.com/davemlz on 2026-05-27.

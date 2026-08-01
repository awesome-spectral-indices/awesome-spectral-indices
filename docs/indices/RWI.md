---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "RWI"
  text: "Rescaled Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/JSTARS.2025.3562089"
---

## Formula

```
((G ** (1.0 / 2.71828)) * (1.0 / n) - S1) / ((G ** (1.0 / 2.71828)) * (1.0 / n) + S1)
```

### Bands

- `G`: Green.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

- `n`: Adjustment factor used for RWI. This constant is calculated as `n = median(G ** (1.0 / 2.71828)) / median(G)`, reducing the spatial dimension (see https://doi.org/10.1109/JSTARS.2025.3562089). Default: `5`.

## Contributor

Index contributed by https://github.com/edujusti on 2026-03-31.

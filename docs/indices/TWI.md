---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "TWI"
  text: "Triangle Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.3390/rs14215289"
---

## Formula

```
(2.84 * (RE1 - RE2) / (G + S2)) + ((1.25 * (G - B) - (N - B)) / (N + 1.25 * G - 0.25 * B))
```

### Bands

- `RE1`: Red Edge 1.
- `RE2`: Red Edge 2.
- `G`: Green.
- `S2`: Short-wave Infrared (SWIR) 2.
- `B`: Blue.
- `N`: Near-Infrared (NIR).

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/remi-braun on 2023-02-10.

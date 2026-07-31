---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "SCoWI"
  text: "Subtractive Coastal Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.3390/rs16152795"
---

## Formula

```
B + 2.0 * (G - N) - 0.75 * S1 - 0.5 * S2
```

### Bands

- `B`: Blue.
- `G`: Green.
- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/cmayet on 2026-03-31.

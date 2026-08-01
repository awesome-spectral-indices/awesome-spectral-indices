---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "ANDWI"
  text: "Augmented Normalized Difference Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.envsoft.2021.105030"
---

## Formula

```
(B + G + R - N - S1 - S2)/(B + G + R + N + S1 + S2)
```

### Bands

- `B`: Blue.
- `G`: Green.
- `R`: Red.
- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-09-22.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "MuWIR"
  text: "Revised Multi-Spectral Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.3390/rs10101643"
---

## Formula

```
-4.0 * ((B - G)/(B + G)) + 2.0 * ((G - N)/(G + N)) + 2.0 * ((G - S2)/(G + S2)) - ((G - S1)/(G + S1))
```

### Bands

- `B`: Blue.
- `G`: Green.
- `N`: Near-Infrared (NIR).
- `S2`: Short-wave Infrared (SWIR) 2.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-09.

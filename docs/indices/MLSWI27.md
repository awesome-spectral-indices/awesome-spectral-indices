---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "MLSWI27"
  text: "Modified Land Surface Water Index (MODIS Bands 2 and 7)"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs71215805"
---

## Formula

```
(1.0 - N - S2)/(1.0 - N + S2)
```

### Bands

- `N`: Near-Infrared (NIR).
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-20.

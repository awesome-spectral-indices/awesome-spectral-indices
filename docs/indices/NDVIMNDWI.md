---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "NDVIMNDWI"
  text: "NDVI-MNDWI Model"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1007/978-3-662-45737-5_51"
---

## Formula

```
((N - R)/(N + R)) - ((G - S1)/(G + S1))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `G`: Green.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-17.

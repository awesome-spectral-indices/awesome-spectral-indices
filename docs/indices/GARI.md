---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GARI"
  text: "Green Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/S0034-4257(96)00072-7"
---

## Formula

```
(N - (G - (B - R))) / (N + (G - (B - R)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `B`: Blue.
- `R`: Red.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

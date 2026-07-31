---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MCARI2"
  text: "Modified Chlorophyll Absorption in Reflectance Index 2"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/j.rse.2003.12.013"
---

## Formula

```
(1.5 * (2.5 * (N - R) - 1.3 * (N - G))) / ((((2.0 * N + 1) ** 2) - (6.0 * N - 5 * (R ** 0.5)) - 0.5) ** 0.5)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `G`: Green.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TriVI"
  text: "Triangular Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "http://dx.doi.org/10.1016/S0034-4257(00)00197-8"
---

## Formula

```
0.5 * (120 * (N - G) - 200 * (R - G))
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

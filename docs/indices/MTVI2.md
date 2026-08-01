---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MTVI2"
  text: "Modified Triangular Vegetation Index 2"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2003.12.013"
---

## Formula

```
(1.5 * (1.2 * (N - G) - 2.5 * (R - G))) / ((((2.0 * N + 1) ** 2) - (6.0 * N - 5 * (R ** 0.5)) - 0.5) ** 0.5)
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

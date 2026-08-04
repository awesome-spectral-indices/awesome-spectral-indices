---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "NDWIns"
  text: "Normalized Difference Water Index with no Snow Cover and Glaciers"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/w12051339"
---

## Formula

```
(G - a * N)/(G + N)
```

### Bands

- `G`: Green.
- `N`: Near-Infrared (NIR).

### Constants

- `a`: Empirical parameter weighting NIR reflectance. Default: `2.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

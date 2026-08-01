---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WDRVI"
  text: "Wide Dynamic Range Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1078/0176-1617-01176"
---

## Formula

```
(alpha * N - R) / (alpha * N + R)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `alpha`: Weighting coefficient used for WDRVI. Default: `0.1`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

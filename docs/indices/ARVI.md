---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "ARVI"
  text: "Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1109/36.134076"
---

## Formula

```
(N - (R - gamma * (R - B))) / (N + (R - gamma * (R - B)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Constants

- `gamma`: Weighting coefficient used for ARVI. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-11.

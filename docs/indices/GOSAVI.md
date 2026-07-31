---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GOSAVI"
  text: "Green Optimized Soil Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.2134/agronj2004.0314"
---

## Formula

```
(N - G) / (N + G + 0.16)
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

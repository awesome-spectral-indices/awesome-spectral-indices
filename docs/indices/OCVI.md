---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "OCVI"
  text: "Optimized Chlorophyll Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "http://dx.doi.org/10.1007/s11119-008-9075-z"
---

## Formula

```
(N / G) * (R / G) ** cexp
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.

### Constants

- `cexp`: Exponent used for OCVI. Default: `1.16`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-13.

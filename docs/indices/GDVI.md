---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GDVI"
  text: "Generalized Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs6021211"
---

## Formula

```
((N ** nexp) - (R ** nexp)) / ((N ** nexp) + (R ** nexp))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `nexp`: Exponent used for GDVI. Default: `2.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TRRVI"
  text: "Transformed Red Range Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.3390/rs12152359"
---

## Formula

```
((RE2 - R) / (RE2 + R)) / (((N - R) / (N + R)) + 1.0)
```

### Bands

- `RE2`: Red Edge 2.
- `R`: Red.
- `N`: Near-Infrared (NIR).

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-18.

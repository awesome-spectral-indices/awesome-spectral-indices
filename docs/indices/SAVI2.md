---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SAVI2"
  text: "Soil-Adjusted Vegetation Index 2"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1080/01431169008955053"
---

## Formula

```
N / (R + (slb / sla))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `slb`: Soil line intercept. Default: `0.0`.
- `sla`: Soil line slope. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

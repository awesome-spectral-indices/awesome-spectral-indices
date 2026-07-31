---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "ATSAVI"
  text: "Adjusted Transformed Soil-Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/0034-4257(91)90009-U"
---

## Formula

```
sla * (N - sla * R - slb) / (sla * N + R - sla * slb + 0.08 * (1 + sla ** 2.0))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `sla`: Soil line slope. Default: `1.0`.
- `slb`: Soil line intercept. Default: `0.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

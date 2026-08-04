---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TSAVI"
  text: "Transformed Soil-Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/IGARSS.1989.576128"
---

## Formula

```
sla * (N - sla * R - slb) / (sla * N + R - sla * slb)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `sla`: Soil line slope. N = sla * R + slb (only for soil pixels/measurements). Default: `1.0`. Suggested values: Equal TSAVI to NDVI when slb is 0.0: `1.0`.
- `slb`: Soil line intercept.  N = sla * R + slb (only for soil pixels/measurements). Default: `0.0`. Suggested values: Equal TSAVI to NDVI when sla is 1.0: `0.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

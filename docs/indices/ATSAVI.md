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
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(91)90009-U"
---

## Formula

```
sla * (N - sla * R - slb) / (sla * N + R - sla * slb + X * (1 + sla ** 2.0))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `X`: Negative abscissa of a reference point located on the soil line. Default: `0.08`.
- `sla`: Soil line slope. N = sla * R + slb (only for soil pixels/measurements). Default: `1.0`.
- `slb`: Soil line intercept.  N = sla * R + slb (only for soil pixels/measurements). Default: `0.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

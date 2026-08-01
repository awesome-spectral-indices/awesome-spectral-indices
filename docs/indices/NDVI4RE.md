---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDVI4RE"
  text: "4-band Red Edge Normalized Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2022.102793"
---

## Formula

```
((alpha * RE3 + (1 - alpha) * RE2) - (beta * R + (1 - beta) * RE1))/((alpha * RE3 + (1 - alpha) * RE2) + (beta * R + (1 - beta) * RE1))
```

### Bands

- `RE3`: Red Edge 3.
- `RE2`: Red Edge 2.
- `R`: Red.
- `RE1`: Red Edge 1.

### Constants

- `alpha`: Weighting coefficient used for WDRVI. Default: `0.1`.
- `beta`: Calibration parameter used for NDSInw. Default: `0.05`.

## Contributor

Index contributed by https://github.com/davemlz on 2025-09-30.

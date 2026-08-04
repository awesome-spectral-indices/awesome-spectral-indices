---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "S2REP"
  text: "Sentinel-2 Red-Edge Position"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.isprsjprs.2013.04.007"
---

## Formula

```
705.0 + 35.0 * ((((RE3 + R) / 2.0) - RE1) / (RE2 - RE1))
```

### Bands

- `RE3`: Red Edge 3.
- `R`: Red.
- `RE1`: Red Edge 1.
- `RE2`: Red Edge 2.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`IRECI`](/indices/IRECI)

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-17.

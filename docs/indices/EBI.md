---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "EBI"
  text: "Enhanced Bloom Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/j.isprsjprs.2019.08.006"
---

## Formula

```
(R + G + B)/((G/B) * (R - B + epsilon))
```

### Bands

- `R`: Red.
- `G`: Green.
- `B`: Blue.

### Constants

- `epsilon`: Adjustment constant used for EBI, WC1 and WC2. For WCx indices use epsilon = 1e-10. Default: `1`.

## Contributor

Index contributed by https://github.com/geoSanjeeb on 2023-07-03.

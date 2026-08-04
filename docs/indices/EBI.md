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
      text: View source 🡕
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

- `epsilon`: Adjustment constant. Default: `1.0`. Suggested values: For raw RGB values in [0,255]: `256`; For reflectances in [0,1]: `1.0`.

## Contributor

Index contributed by https://github.com/geoSanjeeb on 2023-07-03.

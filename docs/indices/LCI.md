---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "LCI"
  text: "Leaf Chlorophyll Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0176-1617(99)80314-9"
---

## Formula

```
(R850 - R710)/(R850 - R680)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Hyperspectral`

### Bands

- `R850`: Reflectance at 850 nm.
- `R710`: Reflectance at 710 nm.
- `R680`: Reflectance at 680 nm.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/j-miszczyszyn on 2026-08-09.

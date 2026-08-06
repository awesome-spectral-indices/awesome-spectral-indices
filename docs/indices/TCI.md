---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TCI"
  text: "Triangular Chlorophyll Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1109/TGRS.2007.904836"
---

## Formula

```
1.2 * (RE1 - G) - 1.5 * (R - G) * (RE1 / R) ** 0.5
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `RE1`: Red Edge 1.
- `G`: Green.
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

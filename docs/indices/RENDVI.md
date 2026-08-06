---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "RENDVI"
  text: "Red Edge Normalized Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0176-1617(11)81633-0"
---

## Formula

```
(RE2 - RE1)/(RE2 + RE1)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `RE2`: Red Edge 2.
- `RE1`: Red Edge 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`NDVI705`](/indices/NDVI705)
- [`SR705`](/indices/SR705)
- [`SR555`](/indices/SR555)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-09.

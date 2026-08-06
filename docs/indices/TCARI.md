---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TCARI"
  text: "Transformed Chlorophyll Absorption in Reflectance Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(02)00018-4"
---

## Formula

```
3 * ((RE1 - R) - 0.2 * (RE1 - G) * (RE1 / R))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `RE1`: Red Edge 1.
- `R`: Red.
- `G`: Green.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`TCARIOSAVI`](/indices/TCARIOSAVI)

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-13.

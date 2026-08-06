---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDTillI"
  text: "Normalized Difference Tillage Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.asprs.org/wp-content/uploads/pers/1997journal/jan/1997_jan_87-93.pdf"
---

## Formula

```
(S1 - S2)/(S1 + S2)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`STI`](/indices/STI)

## Contributor

Index contributed by https://github.com/davemlz on 2025-10-11.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "VARI700"
  text: "Visible Atmospherically Resistant Index (700 nm)"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(01)00289-9"
---

## Formula

```
(RE1 - 1.7 * R + 0.7 * B) / (RE1 + 1.3 * R - 1.3 * B)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `RE1`: Red Edge 1.
- `R`: Red.
- `B`: Blue.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`VARI`](/indices/VARI)
- [`VIG`](/indices/VIG)
- [`VI700`](/indices/VI700)

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-20.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MCARIOSAVI705"
  text: "MCARI/OSAVI Ratio (705 and 750 nm)"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.agrformet.2008.03.005"
---

## Formula

```
(((RE2 - RE1) - 0.2 * (RE2 - G)) * (RE2 / RE1)) / (1.16 * (RE2 - RE1) / (RE2 + RE1 + 0.16))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `RE2`: Red Edge 2.
- `RE1`: Red Edge 1.
- `G`: Green.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`TCARIOSAVI705`](/indices/TCARIOSAVI705)
- [`MCARI705`](/indices/MCARI705)
- [`MSR705`](/indices/MSR705-ratio)

## Contributor

Index contributed by https://github.com/davemlz on 2021-11-06.

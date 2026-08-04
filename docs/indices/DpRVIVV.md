---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-radar"

hero:
  name: "DpRVIVV"
  text: "Dual-Polarized Radar Vegetation Index VV"
  tagline: "Radar"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/app9040655"
---

## Formula

```
(4.0 * VH)/(VV + VH)
```

### Bands

- `VH`: Vertical transmit, horizontal receive radar polarization.
- `VV`: Vertical transmit, vertical receive radar polarization.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`VVVHR`](/indices/VVVHR)
- [`VHVVD`](/indices/VHVVD)

## Contributor

Index contributed by https://github.com/davemlz on 2021-12-25.

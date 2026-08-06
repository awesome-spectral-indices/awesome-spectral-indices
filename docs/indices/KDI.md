---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "KDI"
  text: "Kochia Detection Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.mlwa.2026.100914"
---

## Formula

```
((N + S1 - RE3)/(N + S1 + RE3)) * ((RE1 - 2.0 * RE3 + N)/(RE1 + 2.0 * RE3 + N))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.
- `RE3`: Red Edge 3.
- `RE1`: Red Edge 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`WCI1`](/indices/WCI1)
- [`WCI2`](/indices/WCI2)
- [`WCI3`](/indices/WCI3)

## Contributor

Index contributed by https://github.com/davemlz on 2026-05-27.

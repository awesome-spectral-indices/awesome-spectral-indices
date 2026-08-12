---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDVISR"
  text: "Normalized Difference Vegetation Index with Simple Ratio"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/TGRS.2003.812910"
---

## Formula

```
(N**2 - R)/(N + R**2)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`MNLI`](/indices/MNLI)
- [`SAVISR`](/indices/SAVISR)

## Contributor

Index contributed by https://github.com/davemlz on 2026-08-12.

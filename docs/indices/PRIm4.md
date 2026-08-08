---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "PRIm4"
  text: "Modified Photochemical Reflectance Index 4"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2011.04.036"
---

## Formula

```
(R570 - R531 - R670)/(R570 + R531 + R670)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Hyperspectral`

### Bands

- `R570`: Reflectance at 570 nm.
- `R531`: Reflectance at 531 nm.
- `R670`: Reflectance at 670 nm.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`PRIm1`](/indices/PRIm1)

## Contributor

Index contributed by https://github.com/davemlz on 2026-08-08.

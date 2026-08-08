---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "RVSI"
  text: "Red-edge Vegetation Stress Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://popo.jpl.nasa.gov/pub/docs/workshops/98_docs/37.pdf"
---

## Formula

```
((R714 + R752)/2.0)-R733
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Hyperspectral`

### Bands

- `R714`: Reflectance at 714 nm.
- `R752`: Reflectance at 752 nm.
- `R733`: Reflectance at 733 nm.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/MartinuzziFrancesco on 2026-08-08.

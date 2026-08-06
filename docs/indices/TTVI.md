---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TTVI"
  text: "Transformed Triangular Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs12010016"
---

## Formula

```
0.5 * ((865.0 - 740.0) * (RE3 - RE2) - (N2 - RE2) * (783.0 - 740))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `RE3`: Red Edge 3.
- `RE2`: Red Edge 2.
- `N2`: Near-Infrared (NIR) 2.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-18.

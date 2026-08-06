---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "REDSI"
  text: "Red-Edge Disease Stress Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/s18030868"
---

## Formula

```
((705.0 - 665.0) * (RE3 - R) - (783.0 - 665.0) * (RE1 - R)) / (2.0 * R)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `RE3`: Red Edge 3.
- `R`: Red.
- `RE1`: Red Edge 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-11-06.

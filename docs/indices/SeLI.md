---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SeLI"
  text: "Sentinel-2 LAI Green Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/s19040904"
---

## Formula

```
(N2 - RE1) / (N2 + RE1)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N2`: Near-Infrared (NIR) 2.
- `RE1`: Red Edge 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-08.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TriVI"
  text: "Triangular Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1016/S0034-4257(00)00197-8"
---

## Formula

```
0.5 * (120 * (N - G) - 200 * (R - G))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

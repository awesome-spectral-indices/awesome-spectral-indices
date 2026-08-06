---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TDVI"
  text: "Transformed Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/IGARSS.2002.1026867"
---

## Formula

```
1.5 * ((N - R)/((N ** 2.0 + R + 0.5) ** 0.5))
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

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-09.

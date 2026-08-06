---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-clouds"

hero:
  name: "CLOSDI"
  text: "Cloud Shadow Detection Index"
  tagline: "Clouds"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rsase.2026.101990"
---

## Formula

```
(1.0 - 1.5 * N - 0.1 * R) / (1.0 + 3.5 * N + 4.9 * R)
```

### Classification

- Application domain: `Clouds`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/atca1977 on 2026-03-30.

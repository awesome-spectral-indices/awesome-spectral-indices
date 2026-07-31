---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "EVIv"
  text: "Enhanced Vegetation Index of Vegetation"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1029/2024JG008240"
---

## Formula

```
2.5 * ((N - R)/(N + 6 * R - 7.5 * B + 1.0)) * N
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2024-05-16.

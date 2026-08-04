---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SRVI"
  text: "Symbolic Regression Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1038/s41598-025-34720-x"
---

## Formula

```
(2.0 * N - 3.0 * R) / (N + R + 0.5 * (G + S1))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `G`: Green.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`SRWI`](/indices/SRWI)

## Contributor

Index contributed by https://github.com/c-chrysostomou on 2026-05-25.

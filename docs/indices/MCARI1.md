---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MCARI1"
  text: "Modified Chlorophyll Absorption in Reflectance Index 1"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2003.12.013"
---

## Formula

```
1.2 * (2.5 * (N - R) - 1.3 * (N - G))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `G`: Green.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`MTVI1`](/indices/MTVI1)
- [`MCARI2`](/indices/MCARI2)
- [`MTVI2`](/indices/MTVI2)

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

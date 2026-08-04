---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "NDVIT"
  text: "Normalized Difference Vegetation Index Thermal"
  tagline: "Burn"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/01431160600954704"
---

## Formula

```
(N - (R * T / 10000.0))/(N + (R * T / 10000.0))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `T`: Thermal Infrared.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`CSIT`](/indices/CSIT)
- [`SAVIT`](/indices/SAVIT)

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

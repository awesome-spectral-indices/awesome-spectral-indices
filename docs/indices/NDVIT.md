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
      text: Read the paper 🡕
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

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

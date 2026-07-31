---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "NBRT2"
  text: "Normalized Burn Ratio Thermal 2"
  tagline: "Burn"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1080/01431160500239008"
---

## Formula

```
((N / (T / 10000.0)) - S2) / ((N / (T / 10000.0)) + S2)
```

### Bands

- `N`: Near-Infrared (NIR).
- `T`: Thermal Infrared.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-19.

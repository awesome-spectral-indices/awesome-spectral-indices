---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-snow"

hero:
  name: "NDSInw"
  text: "Normalized Difference Snow Index with no Water"
  tagline: "Snow"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.3390/w12051339"
---

## Formula

```
(N - S1 - beta)/(N + S1)
```

### Bands

- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

- `beta`: Calibration parameter used for NDSInw. Default: `0.05`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

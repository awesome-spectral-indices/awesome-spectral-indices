---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "FAI"
  text: "Floating Algae Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2009.05.012"
---

## Formula

```
N - (R + (S1 - R)*((lambdaN - lambdaR)/(lambdaS1 - lambdaR)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

- `lambdaN`: NIR central wavelength (nm).
- `lambdaR`: Red central wavelength (nm).
- `lambdaS1`: SWIR1 central wavelength (nm).

## Contributor

Index contributed by https://github.com/emanuelcastanho on 2024-05-03.

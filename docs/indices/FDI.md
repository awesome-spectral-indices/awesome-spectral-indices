---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "FDI"
  text: "Floating Debris Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1038/s41598-020-62298-z"
---

## Formula

```
N - (RE2 + 10 * (S1 - RE2) * (lambdaN - lambdaR)/(lambdaS1 - lambdaR))
```

### Bands

- `N`: Near-Infrared (NIR).
- `RE2`: Red Edge 2.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

- `lambdaN`: NIR central wavelength (nm).
- `lambdaR`: Red central wavelength (nm).
- `lambdaS1`: SWIR1 central wavelength (nm).

## Contributor

Index contributed by https://github.com/guillemc23 on 2025-07-18.

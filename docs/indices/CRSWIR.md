---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "CRSWIR"
  text: "Continuum Removal SWIR"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.onf.fr/onf/+/cec::les-rendez-vous-techniques-de-lonf-no69-70.html"
---

## Formula

```
S1 / (N2 + ((S2 - N2) / (lambdaS2 - lambdaN2)) * (lambdaS1 - lambdaN2))
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `N2`: Near-Infrared (NIR) 2.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

- `lambdaN2`: NIR2 central wavelength (nm).
- `lambdaS1`: SWIR1 central wavelength (nm).
- `lambdaS2`: SWIR2 central wavelength (nm).

## Contributor

Index contributed by https://github.com/kenoz on 2025-06-23.

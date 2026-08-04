---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NIRvH2"
  text: "Hyperspectral Near-Infrared Reflectance of Vegetation"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2021.112723"
---

## Formula

```
N - R - k * (lambdaN - lambdaR)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `k`: Slope parameter by soil. Derived by fitting a linear model on refletances against wavelengths in either the red region (675-681 nm) or the NIR region (778-800 nm). Default: `0.0`.
- `lambdaN`: NIR central wavelength (nm).
- `lambdaR`: Red central wavelength (nm).

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-17.

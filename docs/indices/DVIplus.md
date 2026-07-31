---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "DVIplus"
  text: "Difference Vegetation Index Plus"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/j.rse.2019.03.028"
---

## Formula

```
((lambdaN - lambdaR)/(lambdaN - lambdaG)) * G + (1.0 - ((lambdaN - lambdaR)/(lambdaN - lambdaG))) * N - R
```

### Bands

- `G`: Green.
- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `lambdaN`: NIR central wavelength (nm).
- `lambdaR`: Red central wavelength (nm).
- `lambdaG`: Green central wavelength (nm).

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-20.

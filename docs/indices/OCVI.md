---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "OCVI"
  text: "Optimized Chlorophyll Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1007/s11119-008-9075-z"
---

## Formula

```
(N / G) * (R / G) ** c
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.

### Constants

- `c`: Correction factor. Default: `1.0`. Suggested range: `0.3`–`1.74`. Suggested values: Broad-band and erectophile leaf orientation (~ 70°): `0.87`–`1.74`; Broad-band and intermediate leaf orientation (~ 50°): `0.72`–`1.4`; Broad-band and planophile leaf orientation (~ 30°): `0.64`–`1.31`; Broad-band reflectances: `0.64`–`1.74`; Equal OCVI to CVI: `1.0`; Narrow-band reflectances: `0.3`–`0.89`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-13.

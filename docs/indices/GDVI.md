---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GDVI"
  text: "Generalized Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs6021211"
---

## Formula

```
((N ** n) - (R ** n)) / ((N ** n) + (R ** n))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `n`: Power operation exponent to amplify the dynamic range. Default: `2.0`. Suggested values: Equal GDVI to NDVI: `1.0`; Forest/Maquis (Partly), Irrigated Cropland (Partly), Wood-Lands, Citrus/Orchard, Rainfed Cropland, Olive Plantation, Rangeland, Desert, Bare Land: `2.0`; Wood-Lands (Partly), Citrus/Orchard (Partly), Rainfed Cropland (Partly), Olive Plantation, Rangeland, Desert, Bare Land: `3.0`; Wood-Lands, Citrus/Orchard, Rainfed Cropland, Olive Plantation, Rangeland, Desert, Bare Land: `3.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

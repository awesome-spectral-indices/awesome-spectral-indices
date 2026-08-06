---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "EMBI"
  text: "Enhanced Modified Bare Soil Index"
  tagline: "Soil"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2022.102703"
---

## Formula

```
((((S1 - S2 - N)/(S1 + S2 + N)) + 0.5) - ((G - S1)/(G + S1)) - 0.5)/((((S1 - S2 - N)/(S1 + S2 + N)) + 0.5) + ((G - S1)/(G + S1)) + 1.5)
```

### Classification

- Application domain: `Soil`
- Sensing modalities: `Multispectral`

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.
- `N`: Near-Infrared (NIR).
- `G`: Green.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-18.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "DBSI"
  text: "Dry Bareness Index"
  tagline: "Soil"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/land7030081"
---

## Formula

```
((S1 - G)/(S1 + G)) - ((N - R)/(N + R))
```

### Classification

- Application domain: `Soil`
- Sensing modalities: `Multispectral`

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `G`: Green.
- `N`: Near-Infrared (NIR).
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`DBI`](/indices/DBI)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-18.

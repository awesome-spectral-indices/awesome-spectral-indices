---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "NDISIg"
  text: "Normalized Difference Impervious Surface Index Green"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.14358/PERS.76.5.557"
---

## Formula

```
(T - (G + N + S1) / 3.0)/(T + (G + N + S1) / 3.0)
```

### Bands

- `T`: Thermal Infrared.
- `G`: Green.
- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`NDISIr`](/indices/NDISIr)
- [`NDISIb`](/indices/NDISIb)
- [`NDISIndwi`](/indices/NDISIndwi)
- [`NDISImndwi`](/indices/NDISImndwi)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-18.

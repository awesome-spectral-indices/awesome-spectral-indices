---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MCARIOSAVI705"
  text: "MCARI/OSAVI Ratio (705 and 750 nm)"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.agrformet.2008.03.005"
---

## Formula

```
(((RE2 - RE1) - 0.2 * (RE2 - G)) * (RE2 / RE1)) / (1.16 * (RE2 - RE1) / (RE2 + RE1 + 0.16))
```

### Bands

- `RE2`: Red Edge 2.
- `RE1`: Red Edge 1.
- `G`: Green.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-11-06.

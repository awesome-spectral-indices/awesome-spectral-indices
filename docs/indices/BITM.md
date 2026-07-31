---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "BITM"
  text: "Landsat TM-based Brightness Index"
  tagline: "Soil"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/S0034-4257(98)00030-3"
---

## Formula

```
(((B**2.0)+(G**2.0)+(R**2.0))/3.0)**0.5
```

### Bands

- `B`: Blue.
- `G`: Green.
- `R`: Red.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-11-20.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MNLI"
  text: "Modified Non-Linear Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/TGRS.2003.812910"
---

## Formula

```
(1 + L)*((N ** 2) - R)/((N ** 2) + R + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `L`: Canopy background adjustment. Default: `0.5`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-11.

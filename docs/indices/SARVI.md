---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SARVI"
  text: "Soil Adjusted and Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/36.134076"
---

## Formula

```
(1 + L)*(N - (R - (R - B))) / (N + (R - (R - B)) + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Constants

- `L`: Canopy background adjustment. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-11.

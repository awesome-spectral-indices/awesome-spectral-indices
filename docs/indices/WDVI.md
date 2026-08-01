---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WDVI"
  text: "Weighted Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(89)90076-X"
---

## Formula

```
N - sla * R
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `sla`: Soil line slope. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

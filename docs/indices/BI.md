---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "BI"
  text: "Bare Soil Index"
  tagline: "Soil"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.465.8749&rep=rep1&type=pdf"
---

## Formula

```
((S1 + R) - (N + B))/((S1 + R) + (N + B))
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `R`: Red.
- `N`: Near-Infrared (NIR).
- `B`: Blue.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

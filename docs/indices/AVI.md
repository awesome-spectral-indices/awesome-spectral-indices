---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "AVI"
  text: "Advanced Vegetation Index"
  tagline: "Vegetation"
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
(N * (1.0 - R) * (N - R)) ** (1/3)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`BI`](/indices/BI)
- [`SI`](/indices/SI)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

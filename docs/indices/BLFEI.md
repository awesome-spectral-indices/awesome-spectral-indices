---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "BLFEI"
  text: "Built-Up Land Features Extraction Index"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/10106049.2018.1497094"
---

## Formula

```
(((G+R+S2)/3.0)-S1)/(((G+R+S2)/3.0)+S1)
```

### Bands

- `G`: Green.
- `R`: Red.
- `S2`: Short-wave Infrared (SWIR) 2.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-02-09.

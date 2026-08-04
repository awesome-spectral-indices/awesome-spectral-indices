---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "NBAI"
  text: "Normalized Built-up Area Index"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.omicsonline.org/scientific-reports/JGRS-SR136.pdf"
---

## Formula

```
(S2 - S1/G)/(S2 + S1/G)
```

### Bands

- `S2`: Short-wave Infrared (SWIR) 2.
- `S1`: Short-wave Infrared (SWIR) 1.
- `G`: Green.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`BRBA`](/indices/BRBA)

## Contributor

Index contributed by https://github.com/davemlz on 2022-09-22.

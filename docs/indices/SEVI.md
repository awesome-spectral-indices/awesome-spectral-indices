---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SEVI"
  text: "Shadow-Eliminated Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/17538947.2018.1495770"
---

## Formula

```
(N/R) + fdelta * (1.0/R)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `fdelta`: Adjustment factor used for SEVI. Default: `0.581`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-09-22.

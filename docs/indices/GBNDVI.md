---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GBNDVI"
  text: "Green-Blue Normalized Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S1672-6308(07)60027-4"
---

## Formula

```
(N - (G + B))/(N + (G + B))
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `B`: Blue.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

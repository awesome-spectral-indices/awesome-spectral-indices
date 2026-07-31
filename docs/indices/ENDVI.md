---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "ENDVI"
  text: "Enhanced Normalized Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1371/journal.pone.0186193"
---

## Formula

```
((N + G) - (2 * B)) / ((N + G) + (2 * B))
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `B`: Blue.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/gagev on 2024-04-08.

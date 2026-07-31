---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "IRGBVI"
  text: "Improved-Red-Green-Blue Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1016/j.jag.2024.103668"
---

## Formula

```
(5.0 * (G ** 2.0) - 2.0 * (R ** 2.0) - 5.0 * (B ** 2.0)) / (5.0 * (G ** 2.0) + 2.0 * (R ** 2.0) + 5.0 * (B ** 2.0))
```

### Bands

- `G`: Green.
- `R`: Red.
- `B`: Blue.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2025-07-11.

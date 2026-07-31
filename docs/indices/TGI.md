---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TGI"
  text: "Triangular Greenness Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "http://dx.doi.org/10.1016/j.jag.2012.07.020"
---

## Formula

```
- 0.5 * (190 * (R - G) - 120 * (R - B))
```

### Bands

- `R`: Red.
- `G`: Green.
- `B`: Blue.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

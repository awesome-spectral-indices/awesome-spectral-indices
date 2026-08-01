---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SI"
  text: "Shadow Index"
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
((1.0 - B) * (1.0 - G) * (1.0 - R)) ** (1/3)
```

### Bands

- `B`: Blue.
- `G`: Green.
- `R`: Red.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

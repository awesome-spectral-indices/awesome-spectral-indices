---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NLI"
  text: "Non-Linear Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1080/02757259409532252"
---

## Formula

```
((N ** 2) - R)/((N ** 2) + R)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-11.

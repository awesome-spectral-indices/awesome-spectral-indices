---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TVI"
  text: "Transformed Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://ntrs.nasa.gov/citations/19740022614"
---

## Formula

```
(((N - R)/(N + R)) + 0.5) ** 0.5
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

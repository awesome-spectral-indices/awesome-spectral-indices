---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "VIBI"
  text: "Vegetation Index Built-up Index"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1080/01431161.2012.687842"
---

## Formula

```
((N-R)/(N+R))/(((N-R)/(N+R)) + ((S1-N)/(S1+N)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-09-22.

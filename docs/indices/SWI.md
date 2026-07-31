---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-snow"

hero:
  name: "SWI"
  text: "Snow Water Index"
  tagline: "Snow"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.3390/rs11232774"
---

## Formula

```
(G * (N - S1)) / ((G + N) * (N + S1))
```

### Bands

- `G`: Green.
- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-18.

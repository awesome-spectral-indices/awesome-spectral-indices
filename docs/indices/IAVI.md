---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "IAVI"
  text: "New Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://www.jipb.net/EN/abstract/abstract23925.shtml"
---

## Formula

```
(N - (R - gamma * (B - R)))/(N + (R - gamma * (B - R)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Constants

- `gamma`: Weighting coefficient used for ARVI. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

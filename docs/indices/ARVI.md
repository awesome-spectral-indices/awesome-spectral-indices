---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "ARVI"
  text: "Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/36.134076"
---

## Formula

```
(N - (R - gamma * (R - B))) / (N + (R - gamma * (R - B)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Constants

- `gamma`: Weighting coefficient used for reducing atmospheric effects. Default: `1.0`. Suggested range: `0.0`–`2.0`. Suggested values: Bare soil, very sparse vegetation, or arid and semi-arid areas: `0.5`; Equal ARVI to NDVI: `0.0`; Lowest sensitivity for dense forests: `1.0`–`2.0`; Model-specific optimum for continental aerosol. alpha ~ 1.3: `0.9`; Model-specific optimum for maritime aerosol. alpha ~ 0.2: `1.7`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-11.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "MBWI"
  text: "Multi-Band Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2018.01.018"
---

## Formula

```
(omega * G) - R - N - S1 - S2
```

### Bands

- `G`: Green.
- `R`: Red.
- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

- `omega`: Coefficient that maximizes the difference between water and non-water surfaces. Default: `2.0`. Suggested values: For negative index values assigned to water and non-water surfaces: `1.0`; For positive index values assigned to water surfaces and built-up areas (greater values than this also deliver the same result): `5.0`; For positive index values assigned to water surfaces and negative to non-water surfaces: `2.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-17.

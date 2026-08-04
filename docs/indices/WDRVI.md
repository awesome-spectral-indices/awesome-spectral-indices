---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WDRVI"
  text: "Wide Dynamic Range Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1078/0176-1617-01176"
---

## Formula

```
(alpha * N - R) / (alpha * N + R)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

- `alpha`: Weighting coefficient. Default: `0.1`. Suggested range: `0.1`–`0.2`. Suggested values: Aggressive correction, high LAI. Underperforms in sparse vegetation: `0.05`; Conservative correction, high-biomass sensitivity without strongly down-weighting NIR: `0.2`; Equal WDRVI to NDVI: `1.0`; Stronger correction, moderate-to-high LAI, vegetation fraction where NDVI saturates: `0.1`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GRARI"
  text: "Atmospheric Resistant Green-Red Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(96)00072-7"
---

## Formula

```
(N - (eta * G + (1.0 - eta) * R - lmb * (B - R)))/(N + (eta * G + (1.0 - eta) * R - lmb * (B - R)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.
- `B`: Blue.

### Constants

- `eta`: Mix of green and red reflectances in GRARI. Default: `0.5`.
- `lmb`: Parameter that controls the atmospheric correction in GRARI. Default: `1`.

## Contributor

Index contributed by https://github.com/davemlz on 2026-07-22.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "NBUI"
  text: "New Built-Up Index"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://hdl.handle.net/1959.11/29500"
---

## Formula

```
((S1 - N)/(10.0 * (T + S1) ** 0.5)) - (((N - R) * (1.0 + L))/(N - R + L)) - (G - S1)/(G + S1)
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `N`: Near-Infrared (NIR).
- `T`: Thermal Infrared.
- `R`: Red.
- `G`: Green.

### Constants

- `L`: Canopy background adjustment. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-18.

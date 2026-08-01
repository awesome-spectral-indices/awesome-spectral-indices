---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "IBI"
  text: "Index-Based Built-Up Index"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/01431160802039957"
---

## Formula

```
(((S1-N)/(S1+N))-(((N-R)*(1.0+L)/(N+R+L))+((G-S1)/(G+S1)))/2.0)/(((S1-N)/(S1+N))+(((N-R)*(1.0+L)/(N+R+L))+((G-S1)/(G+S1)))/2.0)
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `N`: Near-Infrared (NIR).
- `R`: Red.
- `G`: Green.

### Constants

- `L`: Canopy background adjustment. Default: `1.0`.

## Contributor

Index contributed by https://github.com/davemlz on 2022-02-09.

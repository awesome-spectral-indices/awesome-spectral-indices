---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "EBBI"
  text: "Enhanced Built-Up and Bareness Index"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.3390/rs4102957"
---

## Formula

```
(S1 - N) / (10.0 * ((S1 + T) ** 0.5))
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `N`: Near-Infrared (NIR).
- `T`: Thermal Infrared.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-17.

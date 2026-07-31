---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-radar"

hero:
  name: "QpRVI"
  text: "Quad-Polarized Radar Vegetation Index"
  tagline: "Radar"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://doi.org/10.1109/IGARSS.2001.976856"
---

## Formula

```
(8.0 * HV)/(HH + VV + 2.0 * HV)
```

### Bands

- `HV`: Horizontal transmit, vertical receive radar polarization.
- `HH`: Horizontal transmit, horizontal receive radar polarization.
- `VV`: Vertical transmit, vertical receive radar polarization.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-12-24.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-radar"

hero:
  name: "NDPolI"
  text: "Normalized Difference Polarization Index"
  tagline: "Radar"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: Read the paper 🡕
      link: "https://www.isprs.org/proceedings/XXXVII/congress/4_pdf/267.pdf"
---

## Formula

```
(VV - VH)/(VV + VH)
```

### Bands

- `VV`: Vertical transmit, vertical receive radar polarization.
- `VH`: Vertical transmit, horizontal receive radar polarization.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-19.

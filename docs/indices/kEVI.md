---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-kernel"

hero:
  name: "kEVI"
  text: "Kernel Enhanced Vegetation Index"
  tagline: "Kernel"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1126/sciadv.abc7447"
---

## Formula

```
g * (kNN - kNR) / (kNN + C1 * kNR - C2 * kNB + kNL)
```

### Bands

- `kNN`: Kernel variable kNN.
- `kNR`: Kernel variable kNR.
- `kNB`: Kernel variable kNB.
- `kNL`: Kernel variable kNL.

### Constants

- `g`: Gain factor. Default: `2.5`.
- `C1`: Coefficient 1 for the aerosol resistance term. Default: `6.0`.
- `C2`: Coefficient 2 for the aerosol resistance term. Default: `7.5`.

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-10.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "BAIS2"
  text: "Burned Area Index for Sentinel 2"
  tagline: "Burn"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/ecrs-2-05177"
---

## Formula

```
(1.0 - ((RE2 * RE3 * N2) / R) ** 0.5) * (((S2 - N2)/(S2 + N2) ** 0.5) + 1.0)
```

### Classification

- Application domain: `Burn`
- Sensing modalities: `Multispectral`

### Bands

- `RE2`: Red Edge 2.
- `RE3`: Red Edge 3.
- `N2`: Near-Infrared (NIR) 2.
- `R`: Red.
- `S2`: Short-wave Infrared (SWIR) 2.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

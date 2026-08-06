---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "kNDVI"
  text: "Kernel Normalized Difference Vegetation Index"
  tagline: "Vegetation"
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
(kernel(N, N) - kernel(N, R)) / (kernel(N, N) + kernel(N, R))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`
- Family: `Kernel`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`kEVI`](/indices/kEVI)
- [`kRVI`](/indices/kRVI)
- [`kVARI`](/indices/kVARI)
- [`kIPVI`](/indices/kIPVI)

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

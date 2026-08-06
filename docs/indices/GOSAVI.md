---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GOSAVI"
  text: "Green Optimized Soil Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.2134/agronj2004.0314"
---

## Formula

```
(N - G) / (N + G + 0.16)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`NormNIR`](/indices/NormNIR)
- [`NormR`](/indices/NormR)
- [`NormG`](/indices/NormG)
- [`GRVI`](/indices/GRVI)
- [`GSAVI`](/indices/GSAVI)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

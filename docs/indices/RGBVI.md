---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "RGBVI"
  text: "Red Green Blue Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2015.02.012"
---

## Formula

```
(G ** 2.0 - B * R)/(G ** 2.0 + B * R)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `G`: Green.
- `B`: Blue.
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`MGRVI`](/indices/MGRVI)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

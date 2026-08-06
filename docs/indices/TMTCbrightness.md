---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TMTCbrightness"
  text: "Thematic Mapper Tasseled Cap Brightness Feature"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/TGRS.1984.350619"
---

## Formula

```
0.3037 * B + 0.2793 * G + 0.4743 * R + 0.5585 * N + 0.5082 * S1 + 0.1863 * S2
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`
- Family: `Tasseled Cap`

### Bands

- `B`: Blue.
- `G`: Green.
- `R`: Red.
- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`TMTCwetness`](/indices/TMTCwetness)
- [`TMTCgreenness`](/indices/TMTCgreenness)
- [`TMTCfourth`](/indices/TMTCfourth)
- [`TMTCfifth`](/indices/TMTCfifth)
- [`TMTCsixth`](/indices/TMTCsixth)

## Contributor

Index contributed by https://github.com/remi-braun on 2026-08-06.

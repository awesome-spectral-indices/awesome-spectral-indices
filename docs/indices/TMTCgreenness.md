---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TMTCgreenness"
  text: "Thematic Mapper Tasseled Cap Greenness Feature"
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
-0.2848 * B - 0.2435 * G - 0.5436 * R + 0.7243 * N + 0.0840 * S1 - 0.1800 * S2
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

- [`TMTCbrightness`](/indices/TMTCbrightness)
- [`TMTCwetness`](/indices/TMTCwetness)
- [`TMTCfourth`](/indices/TMTCfourth)
- [`TMTCfifth`](/indices/TMTCfifth)
- [`TMTCsixth`](/indices/TMTCsixth)

## Contributor

Index contributed by https://github.com/remi-braun on 2026-08-06.

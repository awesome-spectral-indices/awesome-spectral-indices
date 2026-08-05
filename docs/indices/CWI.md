---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "CWI"
  text: "Coastal Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1007/s41976-019-00030-w"
---

## Formula

```
(spatial_max(S2) * B) / (spatial_max(B) * S2)
```

### Bands

- `S2`: Short-wave Infrared (SWIR) 2.
- `B`: Blue.

### Constants

No constants are used in this index.

### Reductions

- `space`: reduction functions are evaluated across the valid pixels within the area of interest (AOI).

## Contributor

Index contributed by https://github.com/dghorai on 2026-08-05.

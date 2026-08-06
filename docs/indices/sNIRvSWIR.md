---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "sNIRvSWIR"
  text: "SWIR-enhanced Near-Infrared Reflectance of Vegetation"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1029/2024JG008240"
---

## Formula

```
((N - R - S2 ** 2.0)/(N + R + S2 ** 2.0)) * N
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S2`: Short-wave Infrared (SWIR) 2.

### Polarizations

No radar polarizations are used in this index.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`bNIRv`](/indices/bNIRv)
- [`EVIv`](/indices/EVIv)
- [`sNIRvLSWI`](/indices/sNIRvLSWI)
- [`sNIRvNDPI`](/indices/sNIRvNDPI)
- [`sNIRvNDVILSWIP`](/indices/sNIRvNDVILSWIP)
- [`sNIRvNDVILSWIS`](/indices/sNIRvNDVILSWIS)

## Contributor

Index contributed by https://github.com/MartinuzziFrancesco on 2024-05-14.

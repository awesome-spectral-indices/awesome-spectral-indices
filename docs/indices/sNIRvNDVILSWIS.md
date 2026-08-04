---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "sNIRvNDVILSWIS"
  text: "SWIR-enhanced Near-Infrared Reflectance of Vegetation for the NDVI-LSWI Sum"
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
(((N - R)/(N + R)) + ((N - S2)/(N + S2))) * N
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`bNIRv`](/indices/bNIRv)
- [`EVIv`](/indices/EVIv)
- [`sNIRvLSWI`](/indices/sNIRvLSWI)
- [`sNIRvNDPI`](/indices/sNIRvNDPI)
- [`sNIRvSWIR`](/indices/sNIRvSWIR)
- [`sNIRvNDVILSWIP`](/indices/sNIRvNDVILSWIP)

## Contributor

Index contributed by https://github.com/davemlz on 2024-05-16.

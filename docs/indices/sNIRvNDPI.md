---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "sNIRvNDPI"
  text: "SWIR-enhanced Near-Infrared Reflectance of Vegetation for NDPI"
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
(N - (alpha * R + (1.0 - alpha) * S2))/(N + (alpha * R + (1.0 - alpha) * S2)) * N
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">alpha</code>
<p>Parameter to mitigate soil and snow effects. Taken from NDPI.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.74</strong>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`bNIRv`](/indices/bNIRv)
- [`EVIv`](/indices/EVIv)
- [`sNIRvLSWI`](/indices/sNIRvLSWI)
- [`sNIRvSWIR`](/indices/sNIRvSWIR)
- [`sNIRvNDVILSWIP`](/indices/sNIRvNDVILSWIP)
- [`sNIRvNDVILSWIS`](/indices/sNIRvNDVILSWIS)

## Contributor

Index contributed by https://github.com/davemlz on 2024-05-16.

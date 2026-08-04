---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "SAVIT"
  text: "Soil-Adjusted Vegetation Index Thermal"
  tagline: "Burn"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/01431160600954704"
---

## Formula

```
(1.0 + L) * (N - (R * T / 10000.0)) / (N + (R * T / 10000.0) + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `T`: Thermal Infrared.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">L</code>
<p>Canopy background adjustment.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.5</strong>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`CSIT`](/indices/CSIT)
- [`NDVIT`](/indices/NDVIT)

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

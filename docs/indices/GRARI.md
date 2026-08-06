---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GRARI"
  text: "Atmospheric Resistant Green-Red Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(96)00072-7"
---

## Formula

```
(N - (eta * G + (1.0 - eta) * R - lmb * (B - R)))/(N + (eta * G + (1.0 - eta) * R - lmb * (B - R)))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.
- `B`: Blue.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">eta</code>
<p>Mix of green and red reflectances to get properties that are between ARVI and GARI.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.5</strong>
</div>
</div>
</article>
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lmb</code>
<p>Parameter that controls the atmospheric correction.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.0</strong>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`GARI`](/indices/GARI)
- [`GNDVI`](/indices/GNDVI)

## Contributor

Index contributed by https://github.com/davemlz on 2026-07-22.

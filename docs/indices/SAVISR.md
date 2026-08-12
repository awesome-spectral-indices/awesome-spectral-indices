---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SAVISR"
  text: "Soil-Adjusted Vegetation Index with Simple Ratio"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/TGRS.2003.812910"
---

## Formula

```
(N**2 - R)/(R * (N + R + L))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">L</code>
<p>Background Adjustment Factor.</p>
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

- [`MNLI`](/indices/MNLI)
- [`NDVISR`](/indices/NDVISR)

## Contributor

Index contributed by https://github.com/davemlz on 2026-08-12.

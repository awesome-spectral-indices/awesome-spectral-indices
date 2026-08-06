---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WCI1"
  text: "Wheat Canopy Index (Growth Stage 1)"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.mlwa.2026.100914"
---

## Formula

```
-1.0 * ((B - R + RE1)/(B + R + RE1 + epsilon)) * ((G + R)/(B + N + epsilon))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `B`: Blue.
- `R`: Red.
- `RE1`: Red Edge 1.
- `G`: Green.
- `N`: Near-Infrared (NIR).

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">epsilon</code>
<p>Adjustment constant for numerical stability.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1e-10</strong>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`KDI`](/indices/KDI)
- [`WCI2`](/indices/WCI2)
- [`WCI3`](/indices/WCI3)

## Contributor

Index contributed by https://github.com/davemlz on 2026-05-27.

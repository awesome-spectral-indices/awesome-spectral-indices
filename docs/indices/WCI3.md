---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WCI3"
  text: "Wheat Canopy Index (Growth Stage 3)"
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
((B - R)/(B + R + epsilon)) * tanh(R - max(B, G, RE1, N))
```

### Bands

- `B`: Blue.
- `R`: Red.
- `G`: Green.
- `RE1`: Red Edge 1.
- `N`: Near-Infrared (NIR).

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
- [`WCI1`](/indices/WCI1)
- [`WCI2`](/indices/WCI2)

## Contributor

Index contributed by https://github.com/davemlz on 2026-08-05.

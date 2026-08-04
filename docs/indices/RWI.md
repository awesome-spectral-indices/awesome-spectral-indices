---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "RWI"
  text: "Rescaled Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/JSTARS.2025.3562089"
---

## Formula

```
((G ** (1.0 / 2.71828)) * (1.0 / n) - S1) / ((G ** (1.0 / 2.71828)) * (1.0 / n) + S1)
```

### Bands

- `G`: Green.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">n</code>
<p>Adjustment factor. This constant is calculated as `n = median(G ** (1.0 / 2.71828)) / median(G)`, reducing the spatial dimension (see https://doi.org/10.1109/JSTARS.2025.3562089).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">5</strong>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/edujusti on 2026-03-31.

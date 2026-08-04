---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SAVI"
  text: "Soil-Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(88)90106-X"
---

## Formula

```
(1.0 + L) * (N - R) / (N + R + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

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
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.25<span aria-hidden="true">–</span>1</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>High vegetation densities</dt>
<dd>0.25</dd>
</div>
<div class="constant-suggestion-row">
<dt>Intermediate vegetation densities</dt>
<dd>0.5</dd>
</div>
<div class="constant-suggestion-row">
<dt>Low vegetation densities</dt>
<dd>1.0</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

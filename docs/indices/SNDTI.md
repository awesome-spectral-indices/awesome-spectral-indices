---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SNDTI"
  text: "Soil-Adjusted Normalized Difference Tillage Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/22797254.2017.1418186"
---

## Formula

```
(1.0 + L) * (S1 - S2) / (S1 + S2 + L)
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">L</code>
<p>Soil adjustment factor.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.6</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.0<span aria-hidden="true">–</span>1.0</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>Increased litter mass</dt>
<dd>0.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Low litter mass</dt>
<dd>1.0</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2025-10-11.

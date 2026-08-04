---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "MBWI"
  text: "Multi-Band Water Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2018.01.018"
---

## Formula

```
(omega * G) - R - N - S1 - S2
```

### Bands

- `G`: Green.
- `R`: Red.
- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">omega</code>
<p>Coefficient that maximizes the difference between water and non-water surfaces.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">2.0</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>For negative index values assigned to water and non-water surfaces</dt>
<dd>1.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>For positive index values assigned to water surfaces and built-up areas (greater values than this also deliver the same result)</dt>
<dd>5.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>For positive index values assigned to water surfaces and negative to non-water surfaces</dt>
<dd>2.0</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-17.

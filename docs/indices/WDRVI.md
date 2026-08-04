---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "WDRVI"
  text: "Wide Dynamic Range Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1078/0176-1617-01176"
---

## Formula

```
(alpha * N - R) / (alpha * N + R)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">alpha</code>
<p>Weighting coefficient.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.1</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.1<span aria-hidden="true">–</span>0.2</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>Aggressive correction, high LAI. Underperforms in sparse vegetation</dt>
<dd>0.05</dd>
</div>
<div class="constant-suggestion-row">
<dt>Conservative correction, high-biomass sensitivity without strongly down-weighting NIR</dt>
<dd>0.2</dd>
</div>
<div class="constant-suggestion-row">
<dt>Equal WDRVI to NDVI</dt>
<dd>1.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Stronger correction, moderate-to-high LAI, vegetation fraction where NDVI saturates</dt>
<dd>0.1</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

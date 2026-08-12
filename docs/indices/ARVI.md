---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "ARVI"
  text: "Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/36.134076"
---

## Formula

```
(N - (R - gamma * (B - R))) / (N + (R - gamma * (B - R)))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">gamma</code>
<p>Weighting coefficient used for reducing atmospheric effects.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.0</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.0<span aria-hidden="true">–</span>2.0</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>Bare soil, very sparse vegetation, or arid and semi-arid areas</dt>
<dd>0.5</dd>
</div>
<div class="constant-suggestion-row">
<dt>Equal ARVI to NDVI</dt>
<dd>0.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Lowest sensitivity for dense forests</dt>
<dd>1.0<span aria-hidden="true">–</span>2.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Model-specific optimum for continental aerosol. alpha ~ 1.3</dt>
<dd>0.9</dd>
</div>
<div class="constant-suggestion-row">
<dt>Model-specific optimum for maritime aerosol. alpha ~ 0.2</dt>
<dd>1.7</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`SARVI`](/indices/SARVI)

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-11.

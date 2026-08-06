---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "EBI"
  text: "Enhanced Bloom Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.isprsjprs.2019.08.006"
---

## Formula

```
(R + G + B)/((G/B) * (R - B + epsilon))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `R`: Red.
- `G`: Green.
- `B`: Blue.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">epsilon</code>
<p>Adjustment constant.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.0</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>For raw RGB values in [0,255]</dt>
<dd>256</dd>
</div>
<div class="constant-suggestion-row">
<dt>For reflectances in [0,1]</dt>
<dd>1.0</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/geoSanjeeb on 2023-07-03.

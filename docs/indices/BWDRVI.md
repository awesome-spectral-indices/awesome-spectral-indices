---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "BWDRVI"
  text: "Blue Wide Dynamic Range Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.2135/cropsci2007.01.0031"
---

## Formula

```
(alpha * N - B) / (alpha * N + B)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `B`: Blue.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">alpha</code>
<p>NIR reflectance scalar.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.01</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>Dense biomass/High yield</dt>
<dd>0.01</dd>
</div>
<div class="constant-suggestion-row">
<dt>Low-to-moderate biomass</dt>
<dd>0.1</dd>
</div>
<div class="constant-suggestion-row">
<dt>Moderate biomass</dt>
<dd>0.05</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2021-09-20.

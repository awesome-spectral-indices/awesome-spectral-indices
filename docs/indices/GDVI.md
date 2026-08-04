---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GDVI"
  text: "Generalized Difference Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs6021211"
---

## Formula

```
((N ** n) - (R ** n)) / ((N ** n) + (R ** n))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">n</code>
<p>Power operation exponent to amplify the dynamic range.</p>
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
<dt>Equal GDVI to NDVI</dt>
<dd>1.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Forest/Maquis (Partly), Irrigated Cropland (Partly), Wood-Lands, Citrus/Orchard, Rainfed Cropland, Olive Plantation, Rangeland, Desert, Bare Land</dt>
<dd>2.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Wood-Lands (Partly), Citrus/Orchard (Partly), Rainfed Cropland (Partly), Olive Plantation, Rangeland, Desert, Bare Land</dt>
<dd>3.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Wood-Lands, Citrus/Orchard, Rainfed Cropland, Olive Plantation, Rangeland, Desert, Bare Land</dt>
<dd>3.0</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-14.

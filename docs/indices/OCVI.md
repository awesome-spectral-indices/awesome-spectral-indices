---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "OCVI"
  text: "Optimized Chlorophyll Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1007/s11119-008-9075-z"
---

## Formula

```
(N / G) * (R / G) ** c
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">c</code>
<p>Correction factor.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.0</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.3<span aria-hidden="true">–</span>1.74</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>Broad-band and erectophile leaf orientation (~ 70°)</dt>
<dd>0.87<span aria-hidden="true">–</span>1.74</dd>
</div>
<div class="constant-suggestion-row">
<dt>Broad-band and intermediate leaf orientation (~ 50°)</dt>
<dd>0.72<span aria-hidden="true">–</span>1.4</dd>
</div>
<div class="constant-suggestion-row">
<dt>Broad-band and planophile leaf orientation (~ 30°)</dt>
<dd>0.64<span aria-hidden="true">–</span>1.31</dd>
</div>
<div class="constant-suggestion-row">
<dt>Broad-band reflectances</dt>
<dd>0.64<span aria-hidden="true">–</span>1.74</dd>
</div>
<div class="constant-suggestion-row">
<dt>Equal OCVI to CVI</dt>
<dd>1.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Narrow-band reflectances</dt>
<dd>0.3<span aria-hidden="true">–</span>0.89</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-13.

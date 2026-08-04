---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SAVI4RE"
  text: "4-band Red Edge Soil Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2022.102793"
---

## Formula

```
2.0 * ((alpha * RE3 + (1 - alpha) * RE2) - (beta * R + (1 - beta) * RE1))/((alpha * RE3 + (1 - alpha) * RE2) + (beta * R + (1 - beta) * RE1 + 1))
```

### Bands

- `RE3`: Red Edge 3.
- `RE2`: Red Edge 2.
- `R`: Red.
- `RE1`: Red Edge 1.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">alpha</code>
<p>Parameter representing the proportion of Red Edge 3 reflectance (Sentinel-2).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.2</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.0<span aria-hidden="true">–</span>1.0</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>April</dt>
<dd>0.2</dd>
</div>
<div class="constant-suggestion-row">
<dt>August</dt>
<dd>0.7</dd>
</div>
</dl>
</div>
</div>
</article>
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">beta</code>
<p>Parameter representing the proportion of Red reflectance (Sentinel-2).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.2</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.0<span aria-hidden="true">–</span>1.0</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>April</dt>
<dd>0.2</dd>
</div>
<div class="constant-suggestion-row">
<dt>August</dt>
<dd>0.7</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`NDVI4RE`](/indices/NDVI4RE)
- [`RVI4RE`](/indices/RVI4RE)
- [`NDTI4RE`](/indices/NDTI4RE)
- [`SNDTI4RE`](/indices/SNDTI4RE)
- [`STI4RE`](/indices/STI4RE)

## Contributor

Index contributed by https://github.com/davemlz on 2025-09-30.

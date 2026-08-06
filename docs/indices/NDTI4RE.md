---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDTI4RE"
  text: "4-band Red Edge Normalized Difference Tillage Index"
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
gamma * (S1 - S2)/(S1 + S2) + (1 - gamma) * (N - RE3)/(N + RE3)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `S2`: Short-wave Infrared (SWIR) 2.
- `N`: Near-Infrared (NIR).
- `RE3`: Red Edge 3.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">gamma</code>
<p>Weighting coefficient for the ratio SWIR1/SWIR2 (Sentinel-2).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.4</strong>
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
<dd>0.4</dd>
</div>
<div class="constant-suggestion-row">
<dt>November</dt>
<dd>0.5</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`NDVI4RE`](/indices/NDVI4RE)
- [`SAVI4RE`](/indices/SAVI4RE)
- [`RVI4RE`](/indices/RVI4RE)
- [`SNDTI4RE`](/indices/SNDTI4RE)
- [`STI4RE`](/indices/STI4RE)

## Contributor

Index contributed by https://github.com/davemlz on 2025-09-30.

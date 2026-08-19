---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "NBUI"
  text: "New Built-Up Index"
  tagline: "Urban"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.researchgate.net/publication/306346676_Urban_Built-up_Area_Extraction_and_Change_Detection_of_Adama_Municipal_Area_using_Time-Series_Landsat_Images"
---

## Formula

```
((S1 - N)/(10.0 * (T + S1) ** 0.5)) - (((N - R) * (1.0 + L))/(N - R + L)) - (G - S1)/(G + S1)
```

### Classification

- Application domain: `Urban`
- Sensing modalities: `Multispectral`, `Thermal`

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `N`: Near-Infrared (NIR).
- `T`: Thermal Infrared.
- `R`: Red.
- `G`: Green.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">L</code>
<p>Canopy background adjustment.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.5</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.0<span aria-hidden="true">–</span>1.0</strong>
</div>
<div class="constant-detail-card constant-suggested-values">
<span class="constant-detail-label">Suggested values</span>
<dl>
<div class="constant-suggestion-row">
<dt>High density vegetation</dt>
<dd>1.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Low density vegetation</dt>
<dd>0.0</dd>
</div>
<div class="constant-suggestion-row">
<dt>Medium density vegetation</dt>
<dd>0.5</dd>
</div>
</dl>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-18.

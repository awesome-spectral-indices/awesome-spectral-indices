---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "FAI"
  text: "Floating Algae Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2009.05.012"
---

## Formula

```
N - (R + (S1 - R)*((lambdaN - lambdaR)/(lambdaS1 - lambdaR)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lambdaN</code>
<p>NIR central wavelength (nm).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default is-empty">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">Not specified</strong>
</div>
</div>
</article>
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lambdaR</code>
<p>Red central wavelength (nm).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default is-empty">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">Not specified</strong>
</div>
</div>
</article>
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lambdaS1</code>
<p>SWIR1 central wavelength (nm).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default is-empty">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">Not specified</strong>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/emanuelcastanho on 2024-05-03.

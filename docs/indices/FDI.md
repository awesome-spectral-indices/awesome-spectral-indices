---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "FDI"
  text: "Floating Debris Index"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1038/s41598-020-62298-z"
---

## Formula

```
N - (RE2 + 10 * (S1 - RE2) * (lambdaN - lambdaR)/(lambdaS1 - lambdaR))
```

### Bands

- `N`: Near-Infrared (NIR).
- `RE2`: Red Edge 2.
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

Index contributed by https://github.com/guillemc23 on 2025-07-18.

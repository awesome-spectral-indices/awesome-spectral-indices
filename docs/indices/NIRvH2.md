---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NIRvH2"
  text: "Hyperspectral Near-Infrared Reflectance of Vegetation"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2021.112723"
---

## Formula

```
N - R - k * (lambdaN - lambdaR)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">k</code>
<p>Slope parameter by soil. Derived by fitting a linear model on refletances against wavelengths in either the red region (675-681 nm) or the NIR region (778-800 nm).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.0</strong>
</div>
</div>
</article>
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
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-17.

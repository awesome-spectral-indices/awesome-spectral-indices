---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "CRSWIR"
  text: "Continuum Removal SWIR"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.onf.fr/onf/+/cec::les-rendez-vous-techniques-de-lonf-no69-70.html"
---

## Formula

```
S1 / (N2 + ((S2 - N2) / (lambdaS2 - lambdaN2)) * (lambdaS1 - lambdaN2))
```

### Bands

- `S1`: Short-wave Infrared (SWIR) 1.
- `N2`: Near-Infrared (NIR) 2.
- `S2`: Short-wave Infrared (SWIR) 2.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lambdaN2</code>
<p>NIR2 central wavelength (nm).</p>
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
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lambdaS2</code>
<p>SWIR2 central wavelength (nm).</p>
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

Index contributed by https://github.com/kenoz on 2025-06-23.

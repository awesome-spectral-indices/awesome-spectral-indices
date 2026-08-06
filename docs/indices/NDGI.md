---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDGI"
  text: "Normalized Difference Greenness Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2019.03.028"
---

## Formula

```
(((lambdaN - lambdaR)/(lambdaN - lambdaG)) * G + (1.0 - ((lambdaN - lambdaR)/(lambdaN - lambdaG))) * N - R)/(((lambdaN - lambdaR)/(lambdaN - lambdaG)) * G + (1.0 - ((lambdaN - lambdaR)/(lambdaN - lambdaG))) * N + R)
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `G`: Green.
- `N`: Near-Infrared (NIR).
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lambdaG</code>
<p>Green central wavelength (nm).</p>
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

### Source Companions

These indices are part of the same scientific source:

- [`DVIplus`](/indices/DVIplus)

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-20.

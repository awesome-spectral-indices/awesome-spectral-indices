---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "kEVI"
  text: "Kernel Enhanced Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1126/sciadv.abc7447"
---

## Formula

```
g * (kernel(N, N) - kernel(N, R)) / (kernel(N, N) + C1 * kernel(N, R) - C2 * kernel(N, B) + kernel(N, L))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`
- Family: `Kernel`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">C1</code>
<p>Coefficient 1 for the aerosol resistance term.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">6.0</strong>
</div>
</div>
</article>
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">C2</code>
<p>Coefficient 2 for the aerosol resistance term.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">7.5</strong>
</div>
</div>
</article>
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">L</code>
<p>Canopy background adjustment.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.0</strong>
</div>
</div>
</article>
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">g</code>
<p>Gain factor.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">2.5</strong>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`kNDVI`](/indices/kNDVI)
- [`kRVI`](/indices/kRVI)
- [`kVARI`](/indices/kVARI)
- [`kIPVI`](/indices/kIPVI)

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-10.

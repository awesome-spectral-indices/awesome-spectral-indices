---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-kernel"

hero:
  name: "kEVI"
  text: "Kernel Enhanced Vegetation Index"
  tagline: "Kernel"
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
g * (kNN - kNR) / (kNN + C1 * kNR - C2 * kNB + kNL)
```

### Bands

- `kNN`: Kernel variable kNN.
- `kNR`: Kernel variable kNR.
- `kNB`: Kernel variable kNB.
- `kNL`: Kernel variable kNL.

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

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-10.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MNLI"
  text: "Modified Non-Linear Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/TGRS.2003.812910"
---

## Formula

```
(1 + L)*((N ** 2) - R)/((N ** 2) + R + L)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

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
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-11.

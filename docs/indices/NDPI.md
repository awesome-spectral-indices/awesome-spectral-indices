---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDPI"
  text: "Normalized Difference Phenology Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2017.04.031"
---

## Formula

```
(N - (alpha * R + (1.0 - alpha) * S1))/(N + (alpha * R + (1.0 - alpha) * S1))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `S1`: Short-wave Infrared (SWIR) 1.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">alpha</code>
<p>Weighting coefficient.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.74</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.0<span aria-hidden="true">–</span>1.0</strong>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2022-01-20.

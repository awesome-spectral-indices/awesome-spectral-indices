---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GARI"
  text: "Green Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(96)00072-7"
---

## Formula

```
(N - (G - lmb * (B - R))) / (N + (G - lmb * (B - R)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `G`: Green.
- `B`: Blue.
- `R`: Red.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">lmb</code>
<p>Parameter that controls the atmospheric correction.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.0</strong>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

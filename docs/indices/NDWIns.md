---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "NDWIns"
  text: "Normalized Difference Water Index with no Snow Cover and Glaciers"
  tagline: "Water"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/w12051339"
---

## Formula

```
(G - a * N)/(G + N)
```

### Bands

- `G`: Green.
- `N`: Near-Infrared (NIR).

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">a</code>
<p>Empirical parameter weighting NIR reflectance.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">2.0</strong>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

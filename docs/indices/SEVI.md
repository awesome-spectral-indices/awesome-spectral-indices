---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SEVI"
  text: "Shadow-Eliminated Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/17538947.2018.1495770"
---

## Formula

```
(N/R) + fdelta * (1.0/R)
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">fdelta</code>
<p>Adjustment factor to avoid under-elimination or over-elimination.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.581</strong>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2022-09-22.

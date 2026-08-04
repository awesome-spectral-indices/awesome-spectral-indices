---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "IAVI"
  text: "New Atmospherically Resistant Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.jipb.net/EN/abstract/abstract23925.shtml"
---

## Formula

```
(N - (R - gamma * (B - R)))/(N + (R - gamma * (B - R)))
```

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.
- `B`: Blue.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">gamma</code>
<p>Correction coefficient for upward atmospheric path radiance reaching the satellite.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.0</strong>
</div>
<div class="constant-detail-card constant-range">
<span class="constant-detail-label">Suggested range</span>
<strong class="constant-detail-value">0.65<span aria-hidden="true">–</span>1.21</strong>
</div>
</div>
</article>
</div>

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

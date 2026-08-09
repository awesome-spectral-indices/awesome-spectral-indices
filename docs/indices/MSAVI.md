---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MSAVI"
  text: "Modified Soil-Adjusted Vegetation Index"
  tagline: "Vegetation"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(94)90134-1"
---

## Formula

```
(1 + (1 - 2 * gamma * ((N - R)/(N + R)) * (N - gamma * R))) * (N - R) / (N + R + (1 - 2 * gamma * ((N - R)/(N + R)) * (N - gamma * R)))
```

### Classification

- Application domain: `Vegetation`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `R`: Red.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">gamma</code>
<p>Primary soil line parameter. gamma = N/R (slope of the soil line, only for soil pixels/measurements).</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">1.06</strong>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`MSAVI2`](/indices/MSAVI2)

## Contributor

Index contributed by https://github.com/davemlz on 2026-08-09.

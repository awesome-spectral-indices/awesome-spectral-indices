---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-snow"

hero:
  name: "NDSInw"
  text: "Normalized Difference Snow Index with no Water"
  tagline: "Snow"
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
(N - S1 - b)/(N + S1)
```

### Classification

- Application domain: `Snow`
- Sensing modalities: `Multispectral`

### Bands

- `N`: Near-Infrared (NIR).
- `S1`: Short-wave Infrared (SWIR) 1.

### Polarizations

No radar polarizations are used in this index.

### Constants

<div class="constant-list">
<article class="constant-panel">
<header class="constant-panel-header">
<code class="constant-symbol">b</code>
<p>Empirical parameter that offsets the index.</p>
</header>
<div class="constant-details">
<div class="constant-detail-card constant-default">
<span class="constant-detail-label">Default value</span>
<strong class="constant-detail-value">0.05</strong>
</div>
</div>
</article>
</div>

### Source Companions

These indices are part of the same scientific source:

- [`NDWIns`](/indices/NDWIns)

## Contributor

Index contributed by https://github.com/davemlz on 2022-04-08.

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "OSAVI"
  text: "Optimized Soil-Adjusted Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #16</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(95)00186-7"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="OSAVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_OSAVI,
  author = {Geneviève Rondeaux and Michael Steven and Frédéric Baret},
  title = {Optimization of soil-adjusted vegetation indices},
  journal = {Remote Sensing of Environment},
  volume = {55},
  number = {2},
  year = {1996},
  doi = {10.1016/0034-4257(95)00186-7},
  url = {https://doi.org/10.1016/0034-4257(95)00186-7}
}
```

```text [APA]
Geneviève Rondeaux, Michael Steven, & Frédéric Baret (1996). Optimization of soil-adjusted vegetation indices. Remote Sensing of Environment, 55(2). https://doi.org/10.1016/0034-4257(95)00186-7
```

:::
</IndexDetails>

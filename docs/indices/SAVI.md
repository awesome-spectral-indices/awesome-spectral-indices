---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SAVI"
  text: "Soil-Adjusted Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #6</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(88)90106-X"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="SAVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_SAVI,
  author = {A.R Huete},
  title = {A soil-adjusted vegetation index (SAVI)},
  journal = {Remote Sensing of Environment},
  volume = {25},
  number = {3},
  year = {1988},
  doi = {10.1016/0034-4257(88)90106-x},
  url = {https://doi.org/10.1016/0034-4257(88)90106-x}
}
```

```text [APA]
A.R Huete (1988). A soil-adjusted vegetation index (SAVI). Remote Sensing of Environment, 25(3). https://doi.org/10.1016/0034-4257(88)90106-x
```

:::
</IndexDetails>

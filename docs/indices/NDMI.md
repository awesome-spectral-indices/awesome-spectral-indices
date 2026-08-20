---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDMI"
  text: "Normalized Difference Moisture Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #79</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(01)00318-2"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDMI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NDMI,
  author = {Emily Hoffhine Wilson and Steven A Sader},
  title = {Detection of forest harvest type using multiple dates of Landsat TM imagery},
  journal = {Remote Sensing of Environment},
  volume = {80},
  number = {3},
  year = {2002},
  doi = {10.1016/s0034-4257(01)00318-2},
  url = {https://doi.org/10.1016/s0034-4257(01)00318-2}
}
```

```text [APA]
Emily Hoffhine Wilson, & Steven A Sader (2002). Detection of forest harvest type using multiple dates of Landsat TM imagery. Remote Sensing of Environment, 80(3). https://doi.org/10.1016/s0034-4257(01)00318-2
```

:::
</IndexDetails>

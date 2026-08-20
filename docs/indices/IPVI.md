---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "IPVI"
  text: "Infrared Percentage Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #106</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(90)90085-Z"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="IPVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_IPVI,
  author = {R CRIPPEN},
  title = {Calculating the vegetation index faster},
  journal = {Remote Sensing of Environment},
  volume = {34},
  number = {1},
  year = {1990},
  doi = {10.1016/0034-4257(90)90085-z},
  url = {https://doi.org/10.1016/0034-4257(90)90085-z}
}
```

```text [APA]
R CRIPPEN (1990). Calculating the vegetation index faster. Remote Sensing of Environment, 34(1). https://doi.org/10.1016/0034-4257(90)90085-z
```

:::
</IndexDetails>

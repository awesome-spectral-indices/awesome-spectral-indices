---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "NBLI"
  text: "Normalized Difference Bare Land Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Soil</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-modality-badge modality-thermal\">Thermal</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #232</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs9030249"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NBLI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NBLI,
  author = {Hui Li and Cuizhen Wang and Cheng Zhong and Aijun Su and Chengren Xiong and Jinge Wang and Junqi Liu},
  title = {Mapping Urban Bare Land Automatically  from Landsat Imagery with a Simple Index},
  journal = {Remote Sensing},
  volume = {9},
  number = {3},
  year = {2017},
  doi = {10.3390/rs9030249},
  url = {https://doi.org/10.3390/rs9030249}
}
```

```text [APA]
Hui Li, Cuizhen Wang, Cheng Zhong, Aijun Su, Chengren Xiong, Jinge Wang, & Junqi Liu (2017). Mapping Urban Bare Land Automatically  from Landsat Imagery with a Simple Index. Remote Sensing, 9(3). https://doi.org/10.3390/rs9030249
```

:::
</IndexDetails>

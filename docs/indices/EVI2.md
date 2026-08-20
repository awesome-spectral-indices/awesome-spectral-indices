---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "EVI2"
  text: "Two-Band Enhanced Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #27</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2008.06.006"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="EVI2">

::: code-group

```bibtex [BibTeX]
@article{ASI_EVI2,
  author = {Z JIANG and A HUETE and K DIDAN and T MIURA},
  title = {Development of a two-band enhanced vegetation index without a blue band},
  journal = {Remote Sensing of Environment},
  volume = {112},
  number = {10},
  year = {2008},
  doi = {10.1016/j.rse.2008.06.006},
  url = {https://doi.org/10.1016/j.rse.2008.06.006}
}
```

```text [APA]
Z JIANG, A HUETE, K DIDAN, & T MIURA (2008). Development of a two-band enhanced vegetation index without a blue band. Remote Sensing of Environment, 112(10). https://doi.org/10.1016/j.rse.2008.06.006
```

:::
</IndexDetails>

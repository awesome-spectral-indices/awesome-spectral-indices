---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "FAI"
  text: "Floating Algae Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Water</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #62</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.rse.2009.05.012"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="FAI">

::: code-group

```bibtex [BibTeX]
@article{ASI_FAI,
  author = {Chuanmin Hu},
  title = {A novel ocean color index to detect floating algae in the global oceans},
  journal = {Remote Sensing of Environment},
  volume = {113},
  number = {10},
  year = {2009},
  doi = {10.1016/j.rse.2009.05.012},
  url = {https://doi.org/10.1016/j.rse.2009.05.012}
}
```

```text [APA]
Chuanmin Hu (2009). A novel ocean color index to detect floating algae in the global oceans. Remote Sensing of Environment, 113(10). https://doi.org/10.1016/j.rse.2009.05.012
```

:::
</IndexDetails>

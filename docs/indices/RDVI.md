---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "RDVI"
  text: "Renormalized Difference Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/0034-4257(94)00114-3"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="RDVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_DVI,
  author = {Jean-Louis Roujean and François-Marie Breon},
  title = {Estimating PAR absorbed by vegetation from bidirectional reflectance measurements},
  journal = {Remote Sensing of Environment},
  volume = {51},
  number = {3},
  year = {1995},
  doi = {10.1016/0034-4257(94)00114-3},
  url = {https://doi.org/10.1016/0034-4257(94)00114-3}
}
```

```text [APA]
Jean-Louis Roujean, & François-Marie Breon (1995). Estimating PAR absorbed by vegetation from bidirectional reflectance measurements. Remote Sensing of Environment, 51(3). https://doi.org/10.1016/0034-4257(94)00114-3
```

:::
</IndexDetails>

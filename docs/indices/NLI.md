---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NLI"
  text: "Non-Linear Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #131</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/02757259409532252"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NLI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NLI,
  author = {Narendra S. Goel and Wenhan Qin},
  title = {Influences of canopy architecture on relationships between various vegetation indices and LAI and Fpar: A computer simulation},
  journal = {Remote Sensing Reviews},
  volume = {10},
  number = {4},
  year = {1994},
  doi = {10.1080/02757259409532252},
  url = {https://doi.org/10.1080/02757259409532252}
}
```

```text [APA]
Narendra S. Goel, & Wenhan Qin (1994). Influences of canopy architecture on relationships between various vegetation indices and LAI and Fpar: A computer simulation. Remote Sensing Reviews, 10(4). https://doi.org/10.1080/02757259409532252
```

:::
</IndexDetails>

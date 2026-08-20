---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "BAIM"
  text: "Burned Area Index adapted to MODIS"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Burn</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #270</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.foreco.2006.08.248"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="BAIM">

::: code-group

```bibtex [BibTeX]
@article{ASI_BAIM,
  author = {M. Pilar Martín and Israel Gómez and Emilio Chuvieco},
  title = {Burnt Area Index (BAIM) for burned area discrimination at regional scale using MODIS data},
  journal = {Forest Ecology and Management},
  volume = {234},
  year = {2006},
  doi = {10.1016/j.foreco.2006.08.248},
  url = {https://doi.org/10.1016/j.foreco.2006.08.248}
}
```

```text [APA]
M. Pilar Martín, Israel Gómez, & Emilio Chuvieco (2006). Burnt Area Index (BAIM) for burned area discrimination at regional scale using MODIS data. Forest Ecology and Management, 234. https://doi.org/10.1016/j.foreco.2006.08.248
```

:::
</IndexDetails>

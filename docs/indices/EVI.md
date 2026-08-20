---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "EVI"
  text: "Enhanced Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(02)00096-2"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="EVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_EVI,
  author = {A Huete and K Didan and T Miura and E.P Rodriguez and X Gao and L.G Ferreira},
  title = {Overview of the radiometric and biophysical performance of the MODIS vegetation indices},
  journal = {Remote Sensing of Environment},
  volume = {83},
  number = {1-2},
  year = {2002},
  doi = {10.1016/s0034-4257(02)00096-2},
  url = {https://doi.org/10.1016/s0034-4257(02)00096-2}
}
```

```text [APA]
A Huete, K Didan, T Miura, E.P Rodriguez, X Gao, & L.G Ferreira (2002). Overview of the radiometric and biophysical performance of the MODIS vegetation indices. Remote Sensing of Environment, 83(1-2). https://doi.org/10.1016/s0034-4257(02)00096-2
```

:::
</IndexDetails>

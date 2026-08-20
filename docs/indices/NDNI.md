---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDNI"
  text: "Normalized Difference Nitrogen Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-hyperspectral\">Hyperspectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(02)00011-1"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDNI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NDLI,
  author = {Lydia Serrano and Josep Peñuelas and Susan L Ustin},
  title = {Remote sensing of nitrogen and lignin in Mediterranean vegetation from AVIRIS data},
  journal = {Remote Sensing of Environment},
  volume = {81},
  number = {2-3},
  year = {2002},
  doi = {10.1016/s0034-4257(02)00011-1},
  url = {https://doi.org/10.1016/s0034-4257(02)00011-1}
}
```

```text [APA]
Lydia Serrano, Josep Peñuelas, & Susan L Ustin (2002). Remote sensing of nitrogen and lignin in Mediterranean vegetation from AVIRIS data. Remote Sensing of Environment, 81(2-3). https://doi.org/10.1016/s0034-4257(02)00011-1
```

:::
</IndexDetails>

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GVMI"
  text: "Global Vegetation Moisture Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(02)00037-8"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="GVMI">

::: code-group

```bibtex [BibTeX]
@article{ASI_GVMI,
  author = {Pietro Ceccato and Nadine Gobron and Stéphane Flasse and Bernard Pinty and Stefano Tarantola},
  title = {Designing a spectral index to estimate vegetation water content from remote sensing data: Part 1},
  journal = {Remote Sensing of Environment},
  volume = {82},
  number = {2-3},
  year = {2002},
  doi = {10.1016/s0034-4257(02)00037-8},
  url = {https://doi.org/10.1016/s0034-4257(02)00037-8}
}
```

```text [APA]
Pietro Ceccato, Nadine Gobron, Stéphane Flasse, Bernard Pinty, & Stefano Tarantola (2002). Designing a spectral index to estimate vegetation water content from remote sensing data: Part 1. Remote Sensing of Environment, 82(2-3). https://doi.org/10.1016/s0034-4257(02)00037-8
```

:::
</IndexDetails>

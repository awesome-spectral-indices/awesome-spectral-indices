---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NMDI"
  text: "Normalized Multi-band Drought Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1029/2007GL031021"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NMDI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NMDI,
  author = {Lingli Wang and John J. Qu},
  title = {NMDI: A normalized multi‐band drought index for monitoring soil and vegetation moisture with satellite remote sensing},
  journal = {Geophysical Research Letters},
  volume = {34},
  number = {20},
  year = {2007},
  doi = {10.1029/2007gl031021},
  url = {https://doi.org/10.1029/2007gl031021}
}
```

```text [APA]
Lingli Wang, & John J. Qu (2007). NMDI: A normalized multi‐band drought index for monitoring soil and vegetation moisture with satellite remote sensing. Geophysical Research Letters, 34(20). https://doi.org/10.1029/2007gl031021
```

:::
</IndexDetails>

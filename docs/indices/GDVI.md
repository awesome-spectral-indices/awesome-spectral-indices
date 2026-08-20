---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GDVI"
  text: "Generalized Difference Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/rs6021211"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="GDVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_GDVI,
  author = {Weicheng Wu},
  title = {The Generalized Difference Vegetation Index (GDVI) for Dryland Characterization},
  journal = {Remote Sensing},
  volume = {6},
  number = {2},
  year = {2014},
  doi = {10.3390/rs6021211},
  url = {https://doi.org/10.3390/rs6021211}
}
```

```text [APA]
Weicheng Wu (2014). The Generalized Difference Vegetation Index (GDVI) for Dryland Characterization. Remote Sensing, 6(2). https://doi.org/10.3390/rs6021211
```

:::
</IndexDetails>

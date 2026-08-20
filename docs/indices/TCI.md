---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TCI"
  text: "Triangular Chlorophyll Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #146</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1109/TGRS.2007.904836"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="TCI">

::: code-group

```bibtex [BibTeX]
@article{ASI_TCI,
  author = {Driss Haboudane and Nicolas Tremblay and John R. Miller and Philippe Vigneault},
  title = {Remote Estimation of Crop Chlorophyll Content Using Spectral Indices Derived From Hyperspectral Data},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume = {46},
  number = {2},
  year = {2008},
  doi = {10.1109/tgrs.2007.904836},
  url = {https://doi.org/10.1109/tgrs.2007.904836}
}
```

```text [APA]
Driss Haboudane, Nicolas Tremblay, John R. Miller, & Philippe Vigneault (2008). Remote Estimation of Crop Chlorophyll Content Using Spectral Indices Derived From Hyperspectral Data. IEEE Transactions on Geoscience and Remote Sensing, 46(2). https://doi.org/10.1109/tgrs.2007.904836
```

:::
</IndexDetails>

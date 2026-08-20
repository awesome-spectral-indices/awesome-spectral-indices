---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MRBVI"
  text: "Modified Red Blue Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/s20185055"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="MRBVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_MRBVI,
  author = {Yahui Guo and Hanxi Wang and Zhaofei Wu and Shuxin Wang and Hongyong Sun and J. Senthilnath and Jingzhe Wang and Christopher Robin Bryant and Yongshuo Fu},
  title = {Modified Red Blue Vegetation Index for Chlorophyll Estimation and Yield Prediction of Maize from Visible Images Captured by UAV},
  journal = {Sensors},
  volume = {20},
  number = {18},
  year = {2020},
  doi = {10.3390/s20185055},
  url = {https://doi.org/10.3390/s20185055}
}
```

```text [APA]
Yahui Guo, Hanxi Wang, Zhaofei Wu, Shuxin Wang, Hongyong Sun, J. Senthilnath, Jingzhe Wang, Christopher Robin Bryant, & Yongshuo Fu (2020). Modified Red Blue Vegetation Index for Chlorophyll Estimation and Yield Prediction of Maize from Visible Images Captured by UAV. Sensors, 20(18). https://doi.org/10.3390/s20185055
```

:::
</IndexDetails>

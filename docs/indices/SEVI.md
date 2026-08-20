---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SEVI"
  text: "Shadow-Eliminated Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/17538947.2018.1495770"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="SEVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_SEVI,
  author = {Hong Jiang and Sen Wang and Xiaojie Cao and Chenghai Yang and Zhaoming Zhang and Xiaoqin Wang},
  title = {A shadow- eliminated vegetation index (SEVI) for removal of self and cast shadow effects on vegetation in rugged terrains},
  journal = {International Journal of Digital Earth},
  volume = {12},
  number = {9},
  year = {2019},
  doi = {10.1080/17538947.2018.1495770},
  url = {https://doi.org/10.1080/17538947.2018.1495770}
}
```

```text [APA]
Hong Jiang, Sen Wang, Xiaojie Cao, Chenghai Yang, Zhaoming Zhang, & Xiaoqin Wang (2019). A shadow- eliminated vegetation index (SEVI) for removal of self and cast shadow effects on vegetation in rugged terrains. International Journal of Digital Earth, 12(9). https://doi.org/10.1080/17538947.2018.1495770
```

:::
</IndexDetails>

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "BaI"
  text: "Bareness Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Soil</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/IGARSS.2005.1525743"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="BaI">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_BaI,
  author = {Haobo Lin and Jindi Wang and Suhong Liu and Yonghua Qu and Huawei Wan},
  title = {Studies on urban areas extraction from landsat TM images},
  booktitle = {Proceedings. 2005 IEEE International Geoscience and Remote Sensing Symposium, 2005. IGARSS '05.},
  volume = {6},
  doi = {10.1109/igarss.2005.1525743},
  url = {https://doi.org/10.1109/igarss.2005.1525743}
}
```

```text [APA]
Haobo Lin, Jindi Wang, Suhong Liu, Yonghua Qu, & Huawei Wan (n.d.). Studies on urban areas extraction from landsat TM images. Proceedings. 2005 IEEE International Geoscience and Remote Sensing Symposium, 2005. IGARSS '05., 6. https://doi.org/10.1109/igarss.2005.1525743
```

:::
</IndexDetails>

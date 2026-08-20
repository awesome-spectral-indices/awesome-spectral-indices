---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-snow"

hero:
  name: "NDSIITM"
  text: "Normalized Difference Snow/Ice Index for Landsat TM"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Snow</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/01431160119766"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDSIITM">

::: code-group

```bibtex [BibTeX]
@article{ASI_NDSIITM,
  author = {Xiangming Xiao and Zhenxi Shen and Xiaoguan Qin},
  title = {Assessing the potential of VEGETATION sensor data for mapping snow and ice cover: A Normalized Difference Snow and Ice Index},
  journal = {International Journal of Remote Sensing},
  volume = {22},
  number = {13},
  year = {2001},
  doi = {10.1080/01431160119766},
  url = {https://doi.org/10.1080/01431160119766}
}
```

```text [APA]
Xiangming Xiao, Zhenxi Shen, & Xiaoguan Qin (2001). Assessing the potential of VEGETATION sensor data for mapping snow and ice cover: A Normalized Difference Snow and Ice Index. International Journal of Remote Sensing, 22(13). https://doi.org/10.1080/01431160119766
```

:::
</IndexDetails>

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "CARI"
  text: "Carotenoid Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-hyperspectral\">Hyperspectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2016.12.005"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="CARI">

::: code-group

```bibtex [BibTeX]
@article{ASI_CARI,
  author = {Xianfeng Zhou and Wenjiang Huang and Weiping Kong and Huichun Ye and Yingying Dong and Raffaele Casa},
  title = {Assessment of leaf carotenoids content with a new carotenoid index: Development and validation on experimental and model data},
  journal = {International Journal of Applied Earth Observation and Geoinformation},
  volume = {57},
  year = {2017},
  doi = {10.1016/j.jag.2016.12.005},
  url = {https://doi.org/10.1016/j.jag.2016.12.005}
}
```

```text [APA]
Xianfeng Zhou, Wenjiang Huang, Weiping Kong, Huichun Ye, Yingying Dong, & Raffaele Casa (2017). Assessment of leaf carotenoids content with a new carotenoid index: Development and validation on experimental and model data. International Journal of Applied Earth Observation and Geoinformation, 57. https://doi.org/10.1016/j.jag.2016.12.005
```

:::
</IndexDetails>

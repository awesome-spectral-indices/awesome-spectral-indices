---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "VIBI"
  text: "Vegetation Index Built-up Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Urban</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1080/01431161.2012.687842"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="VIBI">

::: code-group

```bibtex [BibTeX]
@article{ASI_VIBI,
  author = {Demetris Stathakis and Konstantinos Perakis and Igor Savin},
  title = {Efficient segmentation of urban areas by the VIBI},
  journal = {International Journal of Remote Sensing},
  volume = {33},
  number = {20},
  year = {2012},
  doi = {10.1080/01431161.2012.687842},
  url = {https://doi.org/10.1080/01431161.2012.687842}
}
```

```text [APA]
Demetris Stathakis, Konstantinos Perakis, & Igor Savin (2012). Efficient segmentation of urban areas by the VIBI. International Journal of Remote Sensing, 33(20). https://doi.org/10.1080/01431161.2012.687842
```

:::
</IndexDetails>

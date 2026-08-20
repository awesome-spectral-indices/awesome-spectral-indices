---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "NDBI"
  text: "Normalized Difference Built-Up Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Urban</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1080/01431160304987"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDBI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NDBI,
  author = {Y. Zha and J. Gao and S. Ni},
  title = {Use of normalized difference built-up index in automatically mapping urban areas from TM imagery},
  journal = {International Journal of Remote Sensing},
  volume = {24},
  number = {3},
  year = {2003},
  doi = {10.1080/01431160304987},
  url = {https://doi.org/10.1080/01431160304987}
}
```

```text [APA]
Y. Zha, J. Gao, & S. Ni (2003). Use of normalized difference built-up index in automatically mapping urban areas from TM imagery. International Journal of Remote Sensing, 24(3). https://doi.org/10.1080/01431160304987
```

:::
</IndexDetails>

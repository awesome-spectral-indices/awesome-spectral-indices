---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "QpRVI"
  text: "Quad-Polarized Radar Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-radar\">Radar</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/IGARSS.2001.976856"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="QpRVI">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_QpRVI,
  author = {Yunjin Kim and J. van Zyl},
  title = {Comparison of forest parameter estimation techniques using SAR data},
  booktitle = {IGARSS 2001. Scanning the Present and Resolving the Future. Proceedings. IEEE 2001 International Geoscience and Remote Sensing Symposium (Cat. No.01CH37217)},
  year = {2001},
  doi = {10.1109/igarss.2001.976856},
  url = {https://doi.org/10.1109/igarss.2001.976856}
}
```

```text [APA]
Yunjin Kim, & J. van Zyl (2001). Comparison of forest parameter estimation techniques using SAR data. IGARSS 2001. Scanning the Present and Resolving the Future. Proceedings. IEEE 2001 International Geoscience and Remote Sensing Symposium (Cat. No.01CH37217). https://doi.org/10.1109/igarss.2001.976856
```

:::
</IndexDetails>

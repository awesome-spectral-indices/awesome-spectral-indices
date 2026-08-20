---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TSAVI"
  text: "Transformed Soil-Adjusted Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #203</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/IGARSS.1989.576128"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="TSAVI">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_TSAVI,
  author = {F. Baret and G. Guyot and D.J. Major},
  title = {TSAVI: A Vegetation Index Which Minimizes Soil Brightness Effects On LAI And APAR Estimation},
  booktitle = {12th Canadian Symposium on Remote Sensing Geoscience and Remote Sensing Symposium,},
  volume = {3},
  doi = {10.1109/igarss.1989.576128},
  url = {https://doi.org/10.1109/igarss.1989.576128}
}
```

```text [APA]
F. Baret, G. Guyot, & D.J. Major (n.d.). TSAVI: A Vegetation Index Which Minimizes Soil Brightness Effects On LAI And APAR Estimation. 12th Canadian Symposium on Remote Sensing Geoscience and Remote Sensing Symposium,, 3. https://doi.org/10.1109/igarss.1989.576128
```

:::
</IndexDetails>

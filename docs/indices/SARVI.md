---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SARVI"
  text: "Soil Adjusted and Atmospherically Resistant Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/36.134076"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="SARVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_ARVI,
  author = {Y.J. Kaufman and D. Tanre},
  title = {Atmospherically resistant vegetation index (ARVI) for EOS-MODIS},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume = {30},
  number = {2},
  year = {1992},
  doi = {10.1109/36.134076},
  url = {https://doi.org/10.1109/36.134076}
}
```

```text [APA]
Y.J. Kaufman, & D. Tanre (1992). Atmospherically resistant vegetation index (ARVI) for EOS-MODIS. IEEE Transactions on Geoscience and Remote Sensing, 30(2). https://doi.org/10.1109/36.134076
```

:::
</IndexDetails>

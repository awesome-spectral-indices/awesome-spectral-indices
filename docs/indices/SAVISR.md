---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SAVISR"
  text: "Soil-Adjusted Vegetation Index with Simple Ratio"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/TGRS.2003.812910"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="SAVISR">

::: code-group

```bibtex [BibTeX]
@article{ASI_MNLI,
  author = {Peng Gong and Ruiliang Pu and G.S. Biging and M.R. Larrieu},
  title = {Estimation of forest leaf area index using vegetation indices derived from hyperion hyperspectral data},
  journal = {IEEE Transactions on Geoscience and Remote Sensing},
  volume = {41},
  number = {6},
  year = {2003},
  doi = {10.1109/tgrs.2003.812910},
  url = {https://doi.org/10.1109/tgrs.2003.812910}
}
```

```text [APA]
Peng Gong, Ruiliang Pu, G.S. Biging, & M.R. Larrieu (2003). Estimation of forest leaf area index using vegetation indices derived from hyperion hyperspectral data. IEEE Transactions on Geoscience and Remote Sensing, 41(6). https://doi.org/10.1109/tgrs.2003.812910
```

:::
</IndexDetails>

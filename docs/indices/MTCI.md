---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MTCI"
  text: "MERIS Terrestrial Chlorophyll Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #51</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/0143116042000274015"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="MTCI">

::: code-group

```bibtex [BibTeX]
@article{ASI_MTCI,
  author = {J. Dash and P. J. Curran},
  title = {The MERIS terrestrial chlorophyll index},
  journal = {International Journal of Remote Sensing},
  volume = {25},
  number = {23},
  year = {2004},
  doi = {10.1080/0143116042000274015},
  url = {https://doi.org/10.1080/0143116042000274015}
}
```

```text [APA]
J. Dash, & P. J. Curran (2004). The MERIS terrestrial chlorophyll index. International Journal of Remote Sensing, 25(23). https://doi.org/10.1080/0143116042000274015
```

:::
</IndexDetails>

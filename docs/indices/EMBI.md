---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "EMBI"
  text: "Enhanced Modified Bare Soil Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Soil</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #282</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.jag.2022.102703"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+EMBI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="EMBI">

::: code-group

```bibtex [BibTeX]
@article{ASI_EMBI,
  author = {Yongquan Zhao and Zhe Zhu},
  title = {ASI: An artificial surface Index for Landsat 8 imagery},
  journal = {International Journal of Applied Earth Observation and Geoinformation},
  volume = {107},
  year = {2022},
  doi = {10.1016/j.jag.2022.102703},
  url = {https://doi.org/10.1016/j.jag.2022.102703}
}
```

```text [APA]
Yongquan Zhao, & Zhe Zhu (2022). ASI: An artificial surface Index for Landsat 8 imagery. International Journal of Applied Earth Observation and Geoinformation, 107. https://doi.org/10.1016/j.jag.2022.102703
```

:::
</IndexDetails>

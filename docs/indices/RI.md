---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "RI"
  text: "Redness Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #263</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.documentation.ird.fr/hor/fdi:34390"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+RI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="RI">

::: code-group

```bibtex [BibTeX]
@misc{ASI_RI,
  author = {R. Escadafal and A. Huete},
  title = {Improvement in remote sensing of low vegetation cover in arid regions by correcting vegetation indices for soil "noise"},
  year = {1991},
  url = {https://www.documentation.ird.fr/hor/fdi:34390}
}
```

```text [APA]
R. Escadafal, & A. Huete (1991). Improvement in remote sensing of low vegetation cover in arid regions by correcting vegetation indices for soil "noise". https://www.documentation.ird.fr/hor/fdi:34390
```

:::
</IndexDetails>

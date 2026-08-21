---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TVI"
  text: "Transformed Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-silver\">Citation Rank #2</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://ntrs.nasa.gov/citations/19740022614"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+TVI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="TVI">

::: code-group

```bibtex [BibTeX]
@misc{ASI_NDVI,
  author = {J. Rouse and R. H. Haas and J. A. Schell and D. Deering},
  title = {Monitoring vegetation systems in the great plains with ERTS},
  volume = {1},
  year = {1973},
  url = {https://ntrs.nasa.gov/citations/19740022614}
}
```

```text [APA]
J. Rouse, R. H. Haas, J. A. Schell, & D. Deering (1973). Monitoring vegetation systems in the great plains with ERTS. https://ntrs.nasa.gov/citations/19740022614
```

:::
</IndexDetails>

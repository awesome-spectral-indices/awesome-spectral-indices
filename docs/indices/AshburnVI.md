---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "AshburnVI"
  text: "Ashburn Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #271</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://ntrs.nasa.gov/citations/19800007243"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+AshburnVI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="AshburnVI">

::: code-group

```bibtex [BibTeX]
@misc{ASI_AshburnVI,
  author = {P. Ashburn},
  title = {The vegetative index number and crop identification},
  year = {1979},
  url = {https://ntrs.nasa.gov/citations/19800007243}
}
```

```text [APA]
P. Ashburn (1979). The vegetative index number and crop identification. https://ntrs.nasa.gov/citations/19800007243
```

:::
</IndexDetails>

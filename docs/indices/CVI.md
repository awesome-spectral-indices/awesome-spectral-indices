---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "CVI"
  text: "Chlorophyll Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #247</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1007/s11119-010-9204-3"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+CVI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="CVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_CVI,
  author = {M. Vincini and E. Frazzi},
  title = {Comparing narrow and broad-band vegetation indices to estimate leaf chlorophyll content in planophile crop canopies},
  journal = {Precision Agriculture},
  volume = {12},
  number = {3},
  year = {2011},
  doi = {10.1007/s11119-010-9204-3},
  url = {https://doi.org/10.1007/s11119-010-9204-3}
}
```

```text [APA]
M. Vincini, & E. Frazzi (2011). Comparing narrow and broad-band vegetation indices to estimate leaf chlorophyll content in planophile crop canopies. Precision Agriculture, 12(3). https://doi.org/10.1007/s11119-010-9204-3
```

:::
</IndexDetails>

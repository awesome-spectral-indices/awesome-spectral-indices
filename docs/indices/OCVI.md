---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "OCVI"
  text: "Optimized Chlorophyll Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #154</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1007/s11119-008-9075-z"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="OCVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_OCVI,
  author = {M. Vincini and E. Frazzi and P. D’Alessio},
  title = {A broad-band leaf chlorophyll vegetation index at the canopy scale},
  journal = {Precision Agriculture},
  volume = {9},
  number = {5},
  year = {2008},
  doi = {10.1007/s11119-008-9075-z},
  url = {https://doi.org/10.1007/s11119-008-9075-z}
}
```

```text [APA]
M. Vincini, E. Frazzi, & P. D’Alessio (2008). A broad-band leaf chlorophyll vegetation index at the canopy scale. Precision Agriculture, 9(5). https://doi.org/10.1007/s11119-008-9075-z
```

:::
</IndexDetails>

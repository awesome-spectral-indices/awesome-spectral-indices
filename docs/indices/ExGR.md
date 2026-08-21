---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "ExGR"
  text: "ExG - ExR Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #60</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.compag.2008.03.009"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+ExGR+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="ExGR">

::: code-group

```bibtex [BibTeX]
@article{ASI_ExGR,
  author = {George E. Meyer and João Camargo Neto},
  title = {Verification of color vegetation indices for automated crop imaging applications},
  journal = {Computers and Electronics in Agriculture},
  volume = {63},
  number = {2},
  year = {2008},
  doi = {10.1016/j.compag.2008.03.009},
  url = {https://doi.org/10.1016/j.compag.2008.03.009}
}
```

```text [APA]
George E. Meyer, & João Camargo Neto (2008). Verification of color vegetation indices for automated crop imaging applications. Computers and Electronics in Agriculture, 63(2). https://doi.org/10.1016/j.compag.2008.03.009
```

:::
</IndexDetails>

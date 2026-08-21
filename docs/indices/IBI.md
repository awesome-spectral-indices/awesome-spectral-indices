---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "IBI"
  text: "Index-Based Built-Up Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Urban</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #84</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/01431160802039957"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+IBI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="IBI">

::: code-group

```bibtex [BibTeX]
@article{ASI_IBI,
  author = {H. Xu},
  title = {A new index for delineating built‐up land features in satellite imagery},
  journal = {International Journal of Remote Sensing},
  volume = {29},
  number = {14},
  year = {2008},
  doi = {10.1080/01431160802039957},
  url = {https://doi.org/10.1080/01431160802039957}
}
```

```text [APA]
H. Xu (2008). A new index for delineating built‐up land features in satellite imagery. International Journal of Remote Sensing, 29(14). https://doi.org/10.1080/01431160802039957
```

:::
</IndexDetails>

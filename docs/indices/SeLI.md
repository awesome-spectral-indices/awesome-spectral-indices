---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "SeLI"
  text: "Sentinel-2 LAI Green Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #212</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/s19040904"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+SeLI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="SeLI">

::: code-group

```bibtex [BibTeX]
@article{ASI_SeLI,
  author = {Nieves Pasqualotto and Jesús Delegido and Shari Van Wittenberghe and Michele Rinaldi and José Moreno},
  title = {Multi-Crop Green LAI Estimation with a New Simple Sentinel-2 LAI Index (SeLI)},
  journal = {Sensors},
  volume = {19},
  number = {4},
  year = {2019},
  doi = {10.3390/s19040904},
  url = {https://doi.org/10.3390/s19040904}
}
```

```text [APA]
Nieves Pasqualotto, Jesús Delegido, Shari Van Wittenberghe, Michele Rinaldi, & José Moreno (2019). Multi-Crop Green LAI Estimation with a New Simple Sentinel-2 LAI Index (SeLI). Sensors, 19(4). https://doi.org/10.3390/s19040904
```

:::
</IndexDetails>

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-geology"

hero:
  name: "FII"
  text: "Ferrous Iron Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Geology</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://pubs.usgs.gov/sim/3190/contents/SIM3190_pam.pdf"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+FII+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="FII">

::: code-group

```bibtex [BibTeX]
@techreport{ASI_FII,
  author = {Barnaby W. Rockwell},
  title = {Description and Validation of an Automated Methodology for Mapping Mineralogy, Vegetation, and Hydrothermal Alteration Type from ASTER Satellite Imagery with Examples from the San Juan Mountains, Colorado},
  institution = {U.S. Geological Survey Scientific Investigations Map 3190},
  year = {2012},
  url = {https://pubs.usgs.gov/sim/3190/contents/SIM3190\_pam.pdf}
}
```

```text [APA]
Barnaby W. Rockwell (2012). Description and Validation of an Automated Methodology for Mapping Mineralogy, Vegetation, and Hydrothermal Alteration Type from ASTER Satellite Imagery with Examples from the San Juan Mountains, Colorado. U.S. Geological Survey Scientific Investigations Map 3190. https://pubs.usgs.gov/sim/3190/contents/SIM3190_pam.pdf
```

:::
</IndexDetails>

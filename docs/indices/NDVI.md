---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDVI"
  text: "Normalized Difference Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://ntrs.nasa.gov/citations/19740022614"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDVI">

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

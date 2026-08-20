---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TriVI"
  text: "Triangular Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1016/S0034-4257(00)00197-8"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="TriVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_TriVI,
  author = {N.H Broge and E Leblanc},
  title = {Comparing prediction power and stability of broadband and hyperspectral vegetation indices for estimation of green leaf area index and canopy chlorophyll density},
  journal = {Remote Sensing of Environment},
  volume = {76},
  number = {2},
  year = {2001},
  doi = {10.1016/s0034-4257(00)00197-8},
  url = {https://doi.org/10.1016/s0034-4257(00)00197-8}
}
```

```text [APA]
N.H Broge, & E Leblanc (2001). Comparing prediction power and stability of broadband and hyperspectral vegetation indices for estimation of green leaf area index and canopy chlorophyll density. Remote Sensing of Environment, 76(2). https://doi.org/10.1016/s0034-4257(00)00197-8
```

:::
</IndexDetails>

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDDI"
  text: "Normalized Difference Drought Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1029/2006GL029127"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDDI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NDDI,
  author = {Yingxin Gu and Jesslyn F. Brown and James P. Verdin and Brian Wardlow},
  title = {A five‐year analysis of MODIS NDVI and NDWI for grassland drought assessment over the central Great Plains of the United States},
  journal = {Geophysical Research Letters},
  volume = {34},
  number = {6},
  year = {2007},
  doi = {10.1029/2006gl029127},
  url = {https://doi.org/10.1029/2006gl029127}
}
```

```text [APA]
Yingxin Gu, Jesslyn F. Brown, James P. Verdin, & Brian Wardlow (2007). A five‐year analysis of MODIS NDVI and NDWI for grassland drought assessment over the central Great Plains of the United States. Geophysical Research Letters, 34(6). https://doi.org/10.1029/2006gl029127
```

:::
</IndexDetails>

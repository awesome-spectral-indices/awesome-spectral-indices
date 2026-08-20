---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "CIRE"
  text: "Chlorophyll Index Red Edge"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1078/0176-1617-00887"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="CIRE">

::: code-group

```bibtex [BibTeX]
@article{ASI_CIG,
  author = {Anatoly A. Gitelson and Yuri Gritz † and Mark N. Merzlyak},
  title = {Relationships between leaf chlorophyll content and spectral reflectance and algorithms for non-destructive chlorophyll assessment in higher plant leaves},
  journal = {Journal of Plant Physiology},
  volume = {160},
  number = {3},
  year = {2003},
  doi = {10.1078/0176-1617-00887},
  url = {https://doi.org/10.1078/0176-1617-00887}
}
```

```text [APA]
Anatoly A. Gitelson, Yuri Gritz †, & Mark N. Merzlyak (2003). Relationships between leaf chlorophyll content and spectral reflectance and algorithms for non-destructive chlorophyll assessment in higher plant leaves. Journal of Plant Physiology, 160(3). https://doi.org/10.1078/0176-1617-00887
```

:::
</IndexDetails>

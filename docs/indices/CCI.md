---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "CCI"
  text: "Chlorophyll Carotenoid Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #135</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1073/pnas.1606162113"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="CCI">

::: code-group

```bibtex [BibTeX]
@article{ASI_CCI,
  author = {John A. Gamon and K. Fred Huemmrich and Christopher Y. S. Wong and Ingo Ensminger and Steven Garrity and David Y. Hollinger and Asko Noormets and Josep Peñuelas},
  title = {A remotely sensed pigment index reveals photosynthetic phenology in evergreen conifers},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {113},
  number = {46},
  year = {2016},
  doi = {10.1073/pnas.1606162113},
  url = {https://doi.org/10.1073/pnas.1606162113}
}
```

```text [APA]
John A. Gamon, K. Fred Huemmrich, Christopher Y. S. Wong, Ingo Ensminger, Steven Garrity, David Y. Hollinger, Asko Noormets, & Josep Peñuelas (2016). A remotely sensed pigment index reveals photosynthetic phenology in evergreen conifers. Proceedings of the National Academy of Sciences, 113(46). https://doi.org/10.1073/pnas.1606162113
```

:::
</IndexDetails>

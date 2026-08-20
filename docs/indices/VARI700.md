---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "VARI700"
  text: "Visible Atmospherically Resistant Index (700 nm)"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/S0034-4257(01)00289-9"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="VARI700">

::: code-group

```bibtex [BibTeX]
@article{ASI_VARI,
  author = {Anatoly A. Gitelson and Yoram J. Kaufman and Robert Stark and Don Rundquist},
  title = {Novel algorithms for remote estimation of vegetation fraction},
  journal = {Remote Sensing of Environment},
  volume = {80},
  number = {1},
  year = {2002},
  doi = {10.1016/s0034-4257(01)00289-9},
  url = {https://doi.org/10.1016/s0034-4257(01)00289-9}
}
```

```text [APA]
Anatoly A. Gitelson, Yoram J. Kaufman, Robert Stark, & Don Rundquist (2002). Novel algorithms for remote estimation of vegetation fraction. Remote Sensing of Environment, 80(1). https://doi.org/10.1016/s0034-4257(01)00289-9
```

:::
</IndexDetails>

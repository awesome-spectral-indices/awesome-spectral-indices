---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "S2WI"
  text: "Sentinel-2 Water Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Water</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/w13121647"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="S2WI">

::: code-group

```bibtex [BibTeX]
@article{ASI_S2WI,
  author = {Wei Jiang and Yuan Ni and Zhiguo Pang and Xiaotao Li and Hongrun Ju and Guojin He and Juan Lv and Kun Yang and June Fu and Xiangdong Qin},
  title = {An Effective Water Body Extraction Method with New Water Index for Sentinel-2 Imagery},
  journal = {Water},
  volume = {13},
  number = {12},
  year = {2021},
  doi = {10.3390/w13121647},
  url = {https://doi.org/10.3390/w13121647}
}
```

```text [APA]
Wei Jiang, Yuan Ni, Zhiguo Pang, Xiaotao Li, Hongrun Ju, Guojin He, Juan Lv, Kun Yang, June Fu, & Xiangdong Qin (2021). An Effective Water Body Extraction Method with New Water Index for Sentinel-2 Imagery. Water, 13(12). https://doi.org/10.3390/w13121647
```

:::
</IndexDetails>

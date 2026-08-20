---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "GEMI"
  text: "Global Environment Monitoring Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1007/bf00031911"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="GEMI">

::: code-group

```bibtex [BibTeX]
@article{ASI_GEMI,
  author = {B. Pinty and M. M. Verstraete},
  title = {GEMI: a non-linear index to monitor global vegetation from satellites},
  journal = {Vegetatio},
  volume = {101},
  number = {1},
  year = {1992},
  doi = {10.1007/bf00031911},
  url = {https://doi.org/10.1007/bf00031911}
}
```

```text [APA]
B. Pinty, & M. M. Verstraete (1992). GEMI: a non-linear index to monitor global vegetation from satellites. Vegetatio, 101(1). https://doi.org/10.1007/bf00031911
```

:::
</IndexDetails>

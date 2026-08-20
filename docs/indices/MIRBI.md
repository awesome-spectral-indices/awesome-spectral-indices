---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "MIRBI"
  text: "Mid-Infrared Burn Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Burn</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/01431160110053185"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="MIRBI">

::: code-group

```bibtex [BibTeX]
@article{ASI_MIRBI,
  author = {S. Trigg and S. Flasse},
  title = {An evaluation of different bi-spectral spaces for discriminating burned shrub-savannah},
  journal = {International Journal of Remote Sensing},
  volume = {22},
  number = {13},
  year = {2001},
  doi = {10.1080/01431160110053185},
  url = {https://doi.org/10.1080/01431160110053185}
}
```

```text [APA]
S. Trigg, & S. Flasse (2001). An evaluation of different bi-spectral spaces for discriminating burned shrub-savannah. International Journal of Remote Sensing, 22(13). https://doi.org/10.1080/01431160110053185
```

:::
</IndexDetails>

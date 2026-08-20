---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "NDREI"
  text: "Normalized Difference Red Edge Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/1011-1344(93)06963-4"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDREI">

::: code-group

```bibtex [BibTeX]
@article{ASI_NDREI,
  author = {Anatoly Gitelson and Mark N. Merzlyak},
  title = {Quantitative estimation of chlorophyll-a using reflectance spectra: Experiments with autumn chestnut and maple leaves},
  journal = {Journal of Photochemistry and Photobiology B: Biology},
  volume = {22},
  number = {3},
  year = {1994},
  doi = {10.1016/1011-1344(93)06963-4},
  url = {https://doi.org/10.1016/1011-1344(93)06963-4}
}
```

```text [APA]
Anatoly Gitelson, & Mark N. Merzlyak (1994). Quantitative estimation of chlorophyll-a using reflectance spectra: Experiments with autumn chestnut and maple leaves. Journal of Photochemistry and Photobiology B: Biology, 22(3). https://doi.org/10.1016/1011-1344(93)06963-4
```

:::
</IndexDetails>

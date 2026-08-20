---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "SWM"
  text: "Sentinel Water Mask"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Water</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://eoscience.esa.int/landtraining2017/files/posters/MILCZAREK.pdf"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="SWM">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_SWM,
  author = {Marta Milczarek and Anna Robak and Alicja Gadawska},
  title = {Sentinel Water Mask (SWM) - new index for water detection on Sentinel-2 images},
  booktitle = {7th Advanced Training Course on Land Remote Sensing, Szent István University, Gödöllő, Hungary 4-9 September 2017},
  year = {2017},
  url = {https://eoscience.esa.int/landtraining2017/files/posters/MILCZAREK.pdf}
}
```

```text [APA]
Marta Milczarek, Anna Robak, & Alicja Gadawska (2017). Sentinel Water Mask (SWM) - new index for water detection on Sentinel-2 images. 7th Advanced Training Course on Land Remote Sensing, Szent István University, Gödöllő, Hungary 4-9 September 2017. https://eoscience.esa.int/landtraining2017/files/posters/MILCZAREK.pdf
```

:::
</IndexDetails>

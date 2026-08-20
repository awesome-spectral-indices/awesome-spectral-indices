---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-snow"

hero:
  name: "NDSI"
  text: "Normalized Difference Snow Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Snow</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/IGARSS.1994.399618"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="NDSI">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_NDSI,
  author = {G.A. Riggs and D.K. Hall and V.V. Salomonson},
  title = {A snow index for the Landsat Thematic Mapper and Moderate Resolution Imaging Spectroradiometer},
  booktitle = {Proceedings of IGARSS '94 - 1994 IEEE International Geoscience and Remote Sensing Symposium},
  volume = {4},
  doi = {10.1109/igarss.1994.399618},
  url = {https://doi.org/10.1109/igarss.1994.399618}
}
```

```text [APA]
G.A. Riggs, D.K. Hall, & V.V. Salomonson (n.d.). A snow index for the Landsat Thematic Mapper and Moderate Resolution Imaging Spectroradiometer. Proceedings of IGARSS '94 - 1994 IEEE International Geoscience and Remote Sensing Symposium, 4. https://doi.org/10.1109/igarss.1994.399618
```

:::
</IndexDetails>

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "WRI"
  text: "Water Ratio Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Water</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1109/GEOINFORMATICS.2010.5567762"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="WRI">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_WRI,
  author = {Li Shen and Changchun Li},
  title = {Water body extraction from Landsat ETM\&amp;\#x002B; imagery using adaboost algorithm},
  booktitle = {2010 18th International Conference on Geoinformatics},
  year = {2010},
  doi = {10.1109/geoinformatics.2010.5567762},
  url = {https://doi.org/10.1109/geoinformatics.2010.5567762}
}
```

```text [APA]
Li Shen, & Changchun Li (2010). Water body extraction from Landsat ETM&amp;#x002B; imagery using adaboost algorithm. 2010 18th International Conference on Geoinformatics. https://doi.org/10.1109/geoinformatics.2010.5567762
```

:::
</IndexDetails>

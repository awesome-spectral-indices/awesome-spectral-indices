---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "ExR"
  text: "Excess Red Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1117/12.336896"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="ExR">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_ExR,
  author = {George E. Meyer and Timothy W. Hindman and Koppolu Laksmi},
  title = {\&lt;title\&gt;Machine vision detection parameters for plant species identification\&lt;/title\&gt;},
  booktitle = {SPIE Proceedings},
  volume = {3543},
  year = {1999},
  doi = {10.1117/12.336896},
  url = {https://doi.org/10.1117/12.336896}
}
```

```text [APA]
George E. Meyer, Timothy W. Hindman, & Koppolu Laksmi (1999). &lt;title&gt;Machine vision detection parameters for plant species identification&lt;/title&gt;. SPIE Proceedings, 3543. https://doi.org/10.1117/12.336896
```

:::
</IndexDetails>

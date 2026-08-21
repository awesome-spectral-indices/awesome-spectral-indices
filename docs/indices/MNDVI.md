---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "MNDVI"
  text: "Modified Normalized Difference Vegetation Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #210</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1080/014311697216810"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+MNDVI+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="MNDVI">

::: code-group

```bibtex [BibTeX]
@article{ASI_MNDVI,
  author = {C. Jurgens},
  title = {The modified normalized difference vegetation index (mNDVI) a new index to determine frost damages in agriculture based on Landsat TM data},
  journal = {International Journal of Remote Sensing},
  volume = {18},
  number = {17},
  year = {1997},
  doi = {10.1080/014311697216810},
  url = {https://doi.org/10.1080/014311697216810}
}
```

```text [APA]
C. Jurgens (1997). The modified normalized difference vegetation index (mNDVI) a new index to determine frost damages in agriculture based on Landsat TM data. International Journal of Remote Sensing, 18(17). https://doi.org/10.1080/014311697216810
```

:::
</IndexDetails>

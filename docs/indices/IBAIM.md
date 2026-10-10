---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "IBAIM"
  text: "Improved Burned Area Index adapted to MODIS"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Burn</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span><span class=\"hero-citation-badge citation-rank-standard\">Citation Rank #310</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://digital.csic.es/bitstream/10261/157427/1/6th_EARsel_Workshop.pdf"
    - theme: alt
      text: Report error
      link: "https://github.com/awesome-spectral-indices/awesome-spectral-indices/issues/new?template=report-error.md&title=INDEX+ERROR%3A+IBAIM+%E2%80%94+"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="IBAIM">

::: code-group

```bibtex [BibTeX]
@misc{ASI_IBAIM,
  author = {Israel Gómez Nieto and M. P. Martín},
  title = {Improving the performance of the BAIM index for burnt area mapping using MODIS data},
  year = {2007},
  url = {https://digital.csic.es/bitstream/10261/157427/1/6th\_EARsel\_Workshop.pdf}
}
```

```text [APA]
Israel Gómez Nieto, & M. P. Martín (2007). Improving the performance of the BAIM index for burnt area mapping using MODIS data. https://digital.csic.es/bitstream/10261/157427/1/6th_EARsel_Workshop.pdf
```

:::
</IndexDetails>

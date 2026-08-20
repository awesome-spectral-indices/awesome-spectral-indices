---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "BAIS2"
  text: "Burned Area Index for Sentinel 2"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Burn</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/ecrs-2-05177"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="BAIS2">

::: code-group

```bibtex [BibTeX]
@inproceedings{ASI_BAIS2,
  author = {Federico Filipponi},
  title = {BAIS2: Burned Area Index for Sentinel-2},
  booktitle = {The 2nd International Electronic Conference on Remote Sensing},
  year = {2018},
  doi = {10.3390/ecrs-2-05177},
  url = {https://doi.org/10.3390/ecrs-2-05177}
}
```

```text [APA]
Federico Filipponi (2018). BAIS2: Burned Area Index for Sentinel-2. The 2nd International Electronic Conference on Remote Sensing. https://doi.org/10.3390/ecrs-2-05177
```

:::
</IndexDetails>

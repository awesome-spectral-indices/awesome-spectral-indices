---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "TGI"
  text: "Triangular Greenness Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "http://dx.doi.org/10.1016/j.jag.2012.07.020"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="TGI">

::: code-group

```bibtex [BibTeX]
@article{ASI_TGI,
  author = {E. Raymond Hunt and Paul C. Doraiswamy and James E. McMurtrey and Craig S.T. Daughtry and Eileen M. Perry and Bakhyt Akhmedov},
  title = {A visible band index for remote sensing leaf chlorophyll content at the canopy scale},
  journal = {International Journal of Applied Earth Observation and Geoinformation},
  volume = {21},
  year = {2013},
  doi = {10.1016/j.jag.2012.07.020},
  url = {https://doi.org/10.1016/j.jag.2012.07.020}
}
```

```text [APA]
E. Raymond Hunt, Paul C. Doraiswamy, James E. McMurtrey, Craig S.T. Daughtry, Eileen M. Perry, & Bakhyt Akhmedov (2013). A visible band index for remote sensing leaf chlorophyll content at the canopy scale. International Journal of Applied Earth Observation and Geoinformation, 21. https://doi.org/10.1016/j.jag.2012.07.020
```

:::
</IndexDetails>

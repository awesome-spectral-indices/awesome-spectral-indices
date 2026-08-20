---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-water"

hero:
  name: "OSI"
  text: "Oil Spill Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Water</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1016/j.mex.2021.101327"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="OSI">

::: code-group

```bibtex [BibTeX]
@article{ASI_OSI,
  author = {Sankaran Rajendran and Ponnumony Vethamony and Fadhil N. Sadooni and Hamad Al-Saad Al-Kuwari and Jassim A. Al-Khayat and Himanshu Govil and Sobhi Nasir},
  title = {Sentinel-2 image transformation methods for mapping oil spill – A case study with Wakashio oil spill in the Indian Ocean, off Mauritius},
  journal = {MethodsX},
  volume = {8},
  year = {2021},
  doi = {10.1016/j.mex.2021.101327},
  url = {https://doi.org/10.1016/j.mex.2021.101327}
}
```

```text [APA]
Sankaran Rajendran, Ponnumony Vethamony, Fadhil N. Sadooni, Hamad Al-Saad Al-Kuwari, Jassim A. Al-Khayat, Himanshu Govil, & Sobhi Nasir (2021). Sentinel-2 image transformation methods for mapping oil spill – A case study with Wakashio oil spill in the Indian Ocean, off Mauritius. MethodsX, 8. https://doi.org/10.1016/j.mex.2021.101327
```

:::
</IndexDetails>

---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-soil"

hero:
  name: "DBSI"
  text: "Dry Bareness Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Soil</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.3390/land7030081"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="DBSI">

::: code-group

```bibtex [BibTeX]
@article{ASI_DBI,
  author = {Azad Rasul and Heiko Balzter and Gaylan R. Faqe Ibrahim and Hasan M. Hameed and James Wheeler and Bashir Adamu and Sa’ad Ibrahim and Peshawa M. Najmaddin},
  title = {Applying Built-Up and Bare-Soil Indices from Landsat 8 to Cities in Dry Climates},
  journal = {Land},
  volume = {7},
  number = {3},
  year = {2018},
  doi = {10.3390/land7030081},
  url = {https://doi.org/10.3390/land7030081}
}
```

```text [APA]
Azad Rasul, Heiko Balzter, Gaylan R. Faqe Ibrahim, Hasan M. Hameed, James Wheeler, Bashir Adamu, Sa’ad Ibrahim, & Peshawa M. Najmaddin (2018). Applying Built-Up and Bare-Soil Indices from Landsat 8 to Cities in Dry Climates. Land, 7(3). https://doi.org/10.3390/land7030081
```

:::
</IndexDetails>

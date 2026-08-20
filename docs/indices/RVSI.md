---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-vegetation"

hero:
  name: "RVSI"
  text: "Red-edge Vegetation Stress Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Vegetation</span><span class=\"hero-modality-badge modality-hyperspectral\">Hyperspectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://popo.jpl.nasa.gov/pub/docs/workshops/98_docs/37.pdf"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="RVSI">

</IndexDetails>

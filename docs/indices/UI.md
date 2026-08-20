---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-urban"

hero:
  name: "UI"
  text: "Urban Index"
  tagline: "<span class=\"hero-classification-badges\"><span class=\"hero-domain-badge\">Urban</span><span class=\"hero-modality-badge modality-multispectral\">Multispectral</span></span>"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://www.isprs.org/proceedings/XXXI/congress/part7/321_XXXI-part7.pdf"
---

<script setup>
import IndexDetails from '../.vitepress/theme/components/IndexDetails.vue'
</script>

<IndexDetails index-key="UI">

</IndexDetails>

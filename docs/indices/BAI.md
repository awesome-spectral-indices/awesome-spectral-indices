---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-burn"

hero:
  name: "BAI"
  text: "Burned Area Index"
  tagline: "Burn"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://digital.csic.es/bitstream/10261/6426/1/Martin_Isabel_Serie_Geografica.pdf"
---

## Formula

```
1.0 / ((0.1 - R) ** 2.0 + (0.06 - N) ** 2.0)
```

### Bands

- `R`: Red.
- `N`: Near-Infrared (NIR).

### Constants

No constants are used in this index.

## Contributor

Index contributed by https://github.com/davemlz on 2021-04-07.

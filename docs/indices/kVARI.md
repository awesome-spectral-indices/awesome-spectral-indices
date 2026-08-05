---
# https://vitepress.dev/reference/default-theme-home-page
layout: home
pageClass: "index-page domain-kernel"

hero:
  name: "kVARI"
  text: "Kernel Visible Atmospherically Resistant Index"
  tagline: "Kernel"
  actions:
    - theme: brand
      text: 🡰 Back to Catalogue Search
      link: /indices/index
    - theme: alt
      text: View source 🡕
      link: "https://doi.org/10.1126/sciadv.abc7447"
---

## Formula

```
(kernel(G, G) - kernel(G, R)) / (kernel(G, G) + kernel(G, R) - kernel(G, B))
```

### Bands

- `G`: Green.
- `R`: Red.
- `B`: Blue.

### Constants

No constants are used in this index.

### Source Companions

These indices are part of the same scientific source:

- [`kEVI`](/indices/kEVI)
- [`kNDVI`](/indices/kNDVI)
- [`kRVI`](/indices/kRVI)
- [`kIPVI`](/indices/kIPVI)

## Contributor

Index contributed by https://github.com/davemlz on 2021-05-10.

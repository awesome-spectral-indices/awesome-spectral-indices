import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Awesome Spectral Indices",
  description: "Awesome Spectral Indices",
  base: '/awesome-spectral-indices/',
  ignoreDeadLinks: [
    /AI%20POLICY/,
    /src\/utils\.py/,
    /src\/indices\.py/
  ],
  srcExclude: [
    'indices/BAI.md',
    'indices/BaI.md',
    'indices/MSR705.md',
    'indices/mSR705.md'
  ],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Catalogue Search', link: '/indices/index' },
      { text: 'Contributing', link: '/CONTRIBUTING' },
      { text: 'Changelog', link: '/CHANGELOG' },
      { text: 'v1 Explained', link: '/v1' },
      { text: 'How to cite', link: '/citation' },
      {
        text: 'APIs',
        items: [
          { text: 'Python', link: 'https://github.com/awesome-spectral-indices/spyndex' },
          { text: 'Earth Engine', link: 'https://github.com/awesome-spectral-indices/spectral' },
          { text: 'Julia', link: 'https://github.com/awesome-spectral-indices/SpectralIndices.jl' }
        ]
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/awesome-spectral-indices/awesome-spectral-indices' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2026-present David Montero Loaiza'
    },
    search: {
      provider: 'local'
    }

  },
  markdown: {
    math: true
  }
})

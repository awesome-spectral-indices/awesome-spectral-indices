import { defineConfig } from 'vitepress'

const base = '/awesome-spectral-indices/'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Awesome Spectral Indices",
  description: "Awesome Spectral Indices",
  base,
  head: [
    ['link', {
      rel: 'icon',
      type: 'image/png',
      media: '(prefers-color-scheme: light)',
      href: `${base}icon.png`
    }],
    ['link', {
      rel: 'icon',
      type: 'image/png',
      media: '(prefers-color-scheme: dark)',
      href: `${base}icon-dark.png`
    }]
  ],
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
    logo: {
      light: '/icon.png',
      dark: '/icon-dark.png',
      alt: 'Awesome Spectral Indices'
    },
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Search Indices', link: '/indices/index' },
      { text: 'Contributing', link: '/CONTRIBUTING' },
      { text: 'v1 Explained', link: '/v1' },      
      {
        text: 'APIs',
        items: [
          { text: 'Python', link: 'https://github.com/awesome-spectral-indices/spyndex' },
          { text: 'Earth Engine', link: 'https://github.com/awesome-spectral-indices/spectral' },
          { text: 'Julia', link: 'https://github.com/awesome-spectral-indices/SpectralIndices.jl' }
        ]
      },
      { text: 'Changelog', link: '/CHANGELOG' },
      {
        text: 'More',
        items: [
          { text: 'How to cite', link: '/citation' },
          { text: 'People', link: '/people' }
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

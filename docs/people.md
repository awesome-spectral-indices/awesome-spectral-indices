---
layout: page
---

<script setup>
import {
  VPTeamPage,
  VPTeamPageTitle,
  VPTeamMembers,
  VPTeamPageSection
} from 'vitepress/theme'
import indexContributors from './.vitepress/data/index-contributors.json'

const maintainer = [{
    avatar: 'https://www.github.com/davemlz.png',
    name: 'David Montero Loaiza',
    title: 'Creator and Maintainer',
    links: [
      { icon: 'github', link: 'https://github.com/davemlz' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/david-montero-loaiza/' }
    ]
  },
]
const schemaValidationDevelopers = [{
    avatar: 'https://www.github.com/davemlz.png',
    name: 'David Montero Loaiza',
    title: 'Schema, Data Model, and Validation Developer',
    links: [
      { icon: 'github', link: 'https://github.com/davemlz' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/david-montero-loaiza/' }
    ]
  },
  {
    avatar: 'https://www.github.com/csaybar.png',
    name: 'César Aybar',
    title: 'Original Pydantic Data Model Developer',
    desc: 'Developed the original Pydantic data model used by the v0 catalogue.',
    links: [
      { icon: 'github', link: 'https://github.com/csaybar' }
    ]
  },
]
const apiDevelopers = [{
    avatar: 'https://www.github.com/davemlz.png',
    name: 'David Montero Loaiza',
    title: 'Python and Google Earth Engine APIs: spyndex, spectral',
    links: [
      { icon: 'github', link: 'https://github.com/davemlz' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/david-montero-loaiza/' }
    ]
  },
  {
    avatar: 'https://www.github.com/MartinuzziFrancesco.png',
    name: 'Francesco Martinuzzi',
    title: 'Julia API: SpectralIndices.jl',
    links: [
      { icon: 'github', link: 'https://github.com/MartinuzziFrancesco' },
    ]
  },
]
const designer = [{
    avatar: 'https://media.licdn.com/dms/image/v2/D4E03AQGgoj42ydBmVw/profile-displayphoto-shrink_800_800/B4EZbMFuIGHcAg-/0/1747180774373?e=1787184000&v=beta&t=g_s39jqaS5KnZqfEWNdme8A0GJO3AOevm74URE0Tnrw',
    name: 'Juliana Quiñones Osorio',
    title: 'Logo Designer',
    links: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/juliana-quinones/?locale=en-US' }
    ]
  },
]
</script>

<VPTeamPage>
  <VPTeamPageTitle>
    <template #title>Team & Contributors</template>
    <template #lead>Meet the people who maintain the catalogue, develop its schema and APIs, contribute spectral indices, and shape its visual identity.</template>
  </VPTeamPageTitle>
  <VPTeamPageSection>
    <template #title>Maintainer</template>
    <template #lead>Project stewardship, catalogue curation, releases, and community coordination.</template>
    <template #members>
      <VPTeamMembers size="small" :members="maintainer" />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>Schema and Validation Contributors</template>
    <template #lead>Development and maintenance of the catalogue schema, data models, and validation.</template>
    <template #members>
      <VPTeamMembers size="small" :members="schemaValidationDevelopers" />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>API Developers</template>
    <template #lead>Development of the libraries that make the catalogue available in Python, Google Earth Engine, and Julia.</template>
    <template #members>
      <VPTeamMembers size="small" :members="apiDevelopers" />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>Index Contributors</template>
    <template #lead>Community members who have contributed one or more spectral indices to the catalogue.</template>
    <template #members>
      <VPTeamMembers size="small" :members="indexContributors" />
    </template>
  </VPTeamPageSection>
  <VPTeamPageSection>
    <template #title>Graphic Designer</template>
    <template #lead>Logo design for Awesome Spectral Indices.</template>
    <template #members>
      <VPTeamMembers size="small" :members="designer" />
    </template>
  </VPTeamPageSection>
</VPTeamPage>

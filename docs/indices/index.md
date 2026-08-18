---
outline: deep
---

<script setup>
import { computed, reactive, ref } from 'vue'
import { withBase } from 'vitepress'
import catalogue from '../../output/v1/spectral-indices-dict.json'

const domainOrder = [
  'vegetation',
  'water',
  'burn',
  'snow',
  'urban',
  'soil',
  'geology',
  'clouds'
]

const domainLabels = {
  vegetation: 'Vegetation',
  water: 'Water',
  burn: 'Burn',
  snow: 'Snow',
  urban: 'Urban',
  soil: 'Soil',
  geology: 'Geology',
  clouds: 'Clouds'
}

const modalityOrder = ['multispectral', 'hyperspectral', 'thermal', 'radar']
const modalityLabels = {
  multispectral: 'Multispectral',
  hyperspectral: 'Hyperspectral',
  thermal: 'Thermal',
  radar: 'Radar'
}

const familyLabels = {
  kernel: 'Kernel',
  tasseled_cap: 'Tasseled Cap',
  radar: 'Radar'
}

const routeOverrides = {
  BAI: 'BAI-burn',
  BaI: 'BaI-soil',
  MSR705: 'MSR705-ratio',
  mSR705: 'mSR705-modified'
}

const indices = Object.entries(catalogue.SpectralIndices)
  .map(([key, index]) => ({ key, ...index }))
  .sort((left, right) => left.key.localeCompare(right.key))

const query = ref('')
const advancedOpen = ref(false)
const advanced = reactive({
  acronym: '',
  name: '',
  applicationDomain: '',
  sensingModalities: [],
  families: [],
  formula: '',
  contributor: '',
  sourceLink: '',
  sourceLinkStatus: '',
  sourceLinkType: '',
  sourceType: '',
  dateOfAddition: '',
  bands: [],
  polarizations: [],
  constants: [],
  externalVariables: []
})

const normalize = (value) => String(value ?? '').toLocaleLowerCase()
const includesText = (value, filter) =>
  !filter || normalize(value).includes(normalize(filter).trim())

const allBands = [...new Set(indices.flatMap((index) => index.bands))]
  .sort((left, right) => left.localeCompare(right))

const hyperspectralBandPattern = /^R([1-9][0-9]*)(?:_([1-9][0-9]*))?$/
const hyperspectralBandBounds = (band) => {
  const match = hyperspectralBandPattern.exec(band)
  if (!match) return null
  const lower = Number(match[1])
  const upper = Number(match[2] ?? match[1])
  const isRange = match[2] !== undefined
  if (lower < 300 || upper > 2500 || (isRange && lower >= upper)) return null
  return [lower, upper]
}
const isHyperspectralBand = (band) => {
  return hyperspectralBandBounds(band) !== null
}
const thermalBands = new Set(['T', 'T1', 'T2'])
const allMultispectralBands = allBands.filter(
  (band) => !isHyperspectralBand(band) && !thermalBands.has(band)
)
const allHyperspectralBands = allBands
  .filter(isHyperspectralBand)
  .sort((left, right) => {
    const leftBounds = hyperspectralBandBounds(left)
    const rightBounds = hyperspectralBandBounds(right)
    return leftBounds[0] - rightBounds[0] || leftBounds[1] - rightBounds[1]
  })
const allThermalBands = allBands.filter((band) => thermalBands.has(band))

const allPolarizations = [
  ...new Set(indices.flatMap((index) => index.polarizations))
].sort((left, right) => left.localeCompare(right))

const allSensingModalities = modalityOrder.filter((modality) =>
  indices.some((index) =>
    index.classification.sensing_modalities.includes(modality)
  )
)

const allFamilies = [
  ...new Set(indices.flatMap((index) => index.classification.family ?? []))
].sort((left, right) => left.localeCompare(right))

const allConstants = [
  ...new Set(indices.flatMap((index) => Object.keys(index.constants)))
].sort((left, right) => left.localeCompare(right))

const allExternalVariables = [
  ...new Set(indices.flatMap((index) => Object.keys(index.external_variables)))
].sort((left, right) => left.localeCompare(right))

const filteredIndices = computed(() => {
  const basicQuery = normalize(query.value).trim()

  return indices.filter((index) => {
    const basicFields = [
      index.key,
      index.acronym,
      index.name,
      index.classification.application_domain,
      ...index.classification.sensing_modalities,
      ...(index.classification.family ?? [])
    ]

    if (
      basicQuery &&
      !basicFields.some((value) => normalize(value).includes(basicQuery))
    ) {
      return false
    }

    if (!includesText(index.acronym, advanced.acronym)) return false
    if (!includesText(index.name, advanced.name)) return false
    if (
      advanced.applicationDomain &&
      index.classification.application_domain !== advanced.applicationDomain
    ) {
      return false
    }
    if (
      !advanced.sensingModalities.every((modality) =>
        index.classification.sensing_modalities.includes(modality)
      )
    ) {
      return false
    }
    if (
      !advanced.families.every((family) =>
        index.classification.family?.includes(family)
      )
    ) {
      return false
    }
    if (!includesText(index.formula, advanced.formula)) return false
    if (!includesText(index.contributor, advanced.contributor)) return false
    if (!includesText(index.source.source_link, advanced.sourceLink)) return false
    if (
      advanced.sourceLinkStatus &&
      index.source.source_link_status !== advanced.sourceLinkStatus
    ) {
      return false
    }
    if (
      advanced.sourceLinkType &&
      index.source.source_link_type !== advanced.sourceLinkType
    ) {
      return false
    }
    if (
      advanced.sourceType &&
      index.source.source_metadata?.type !== advanced.sourceType
    ) {
      return false
    }
    if (!includesText(index.date_of_addition, advanced.dateOfAddition)) {
      return false
    }
    if (!advanced.bands.every((band) => index.bands.includes(band))) {
      return false
    }
    if (
      !advanced.polarizations.every((polarization) =>
        index.polarizations.includes(polarization)
      )
    ) {
      return false
    }
    if (!advanced.constants.every((constant) => constant in index.constants)) {
      return false
    }
    if (
      !advanced.externalVariables.every(
        (externalVariable) => externalVariable in index.external_variables
      )
    ) {
      return false
    }

    return true
  })
})

const modalityProfileKey = (modalities) => modalities.join('+')
const modalityProfileLabel = (modalities) =>
  modalities.map((modality) => modalityLabels[modality]).join(' + ')
const modalityProfileRank = (modalities) =>
  modalityOrder.indexOf(modalities[0]) * 10 + modalities.length

const groupedIndices = computed(() => {
  const profiles = new Map()

  for (const index of filteredIndices.value) {
    const modalities = index.classification.sensing_modalities
    const key = modalityProfileKey(modalities)
    if (!profiles.has(key)) profiles.set(key, { key, modalities, indices: [] })
    profiles.get(key).indices.push(index)
  }

  return [...profiles.values()]
    .sort(
      (left, right) =>
        modalityProfileRank(left.modalities) -
          modalityProfileRank(right.modalities) ||
        left.key.localeCompare(right.key)
    )
    .map((profile) => ({
      ...profile,
      label: modalityProfileLabel(profile.modalities),
      domains: domainOrder
        .map((domain) => ({
          domain,
          indices: profile.indices.filter(
            (index) => index.classification.application_domain === domain
          )
        }))
        .filter((group) => group.indices.length)
    }))
})

function clearFilters() {
  query.value = ''
  advanced.acronym = ''
  advanced.name = ''
  advanced.applicationDomain = ''
  advanced.sensingModalities = []
  advanced.families = []
  advanced.formula = ''
  advanced.contributor = ''
  advanced.sourceLink = ''
  advanced.sourceLinkStatus = ''
  advanced.sourceLinkType = ''
  advanced.sourceType = ''
  advanced.dateOfAddition = ''
  advanced.bands = []
  advanced.polarizations = []
  advanced.constants = []
  advanced.externalVariables = []
}

function indexLink(key) {
  const route = routeOverrides[key] ?? key
  return withBase(`/indices/${encodeURIComponent(route)}`)
}
</script>

# Catalogue Search

Search all Awesome Spectral Indices by name, classification, or application
domain. Open advanced search to filter individual metadata fields or require
specific formula variables.

<div class="catalogue-tools">
  <div class="primary-search">
    <label class="visually-hidden" for="catalogue-query">
      Search spectral indices
    </label>
    <input
      id="catalogue-query"
      v-model="query"
      type="search"
      placeholder="Search acronym, name, application, modality, or family…"
      autocomplete="off"
    >
    <button
      class="advanced-button"
      type="button"
      :aria-expanded="advancedOpen"
      aria-controls="advanced-search"
      @click="advancedOpen = !advancedOpen"
    >
      {{ advancedOpen ? 'Hide advanced search' : 'Advanced Search' }}
    </button>
  </div>

  <div
    v-if="advancedOpen"
    id="advanced-search"
    class="advanced-search"
  >
    <div class="field-grid">
      <label>
        Acronym
        <input v-model="advanced.acronym" type="search" placeholder="e.g. NDVI">
      </label>
      <label>
        Name
        <input v-model="advanced.name" type="search" placeholder="e.g. vegetation">
      </label>
      <label>
        Application domain
        <select v-model="advanced.applicationDomain">
          <option value="">Any domain</option>
          <option v-for="domain in domainOrder" :key="domain" :value="domain">
            {{ domainLabels[domain] }}
          </option>
        </select>
      </label>
      <label>
        Formula contains
        <input v-model="advanced.formula" type="search" placeholder="e.g. N - R">
      </label>
      <label>
        Contributor
        <input v-model="advanced.contributor" type="search" placeholder="GitHub user or email">
      </label>
      <label>
        Source link
        <input v-model="advanced.sourceLink" type="search" placeholder="DOI or URL">
      </label>
      <label>
        Source link status
        <select v-model="advanced.sourceLinkStatus">
          <option value="">Any status</option>
          <option value="operational">Operational</option>
          <option value="down">Down</option>
        </select>
      </label>
      <label>
        Source link type
        <select v-model="advanced.sourceLinkType">
          <option value="">Any link type</option>
          <option value="doi">DOI</option>
          <option value="other">Other</option>
        </select>
      </label>
      <label>
        Source type
        <select v-model="advanced.sourceType">
          <option value="">Any source type</option>
          <option value="article">Article</option>
          <option value="book">Book</option>
          <option value="book_chapter">Book chapter</option>
          <option value="conference_paper">Conference paper</option>
          <option value="poster">Poster</option>
          <option value="report">Report</option>
          <option value="preprint">Preprint</option>
        </select>
      </label>
      <label>
        Date added
        <input v-model="advanced.dateOfAddition" type="search" placeholder="YYYY-MM-DD">
      </label>
    </div>
    <fieldset class="band-filter">
      <legend>Includes all selected sensing modalities</legend>
      <div class="band-options">
        <label
          v-for="modality in allSensingModalities"
          :key="modality"
          class="band-option"
          :class="{ selected: advanced.sensingModalities.includes(modality) }"
        >
          <input
            v-model="advanced.sensingModalities"
            type="checkbox"
            :value="modality"
          >
          <span>{{ modalityLabels[modality] }}</span>
        </label>
      </div>
    </fieldset>
    <fieldset v-if="allFamilies.length" class="band-filter">
      <legend>Includes all selected families</legend>
      <div class="band-options">
        <label
          v-for="family in allFamilies"
          :key="family"
          class="band-option"
          :class="{ selected: advanced.families.includes(family) }"
        >
          <input v-model="advanced.families" type="checkbox" :value="family">
          <span>{{ familyLabels[family] }}</span>
        </label>
      </div>
    </fieldset>
    <fieldset v-if="allMultispectralBands.length" class="band-filter">
      <legend>Includes all selected multispectral bands</legend>
      <div class="band-options">
        <label
          v-for="band in allMultispectralBands"
          :key="band"
          class="band-option"
          :class="{ selected: advanced.bands.includes(band) }"
        >
          <input v-model="advanced.bands" type="checkbox" :value="band">
          <code>{{ band }}</code>
        </label>
      </div>
    </fieldset>
    <fieldset v-if="allHyperspectralBands.length" class="band-filter">
      <legend>Includes all selected hyperspectral wavelengths or ranges</legend>
      <div class="band-options">
        <label
          v-for="band in allHyperspectralBands"
          :key="band"
          class="band-option"
          :class="{ selected: advanced.bands.includes(band) }"
        >
          <input v-model="advanced.bands" type="checkbox" :value="band">
          <code>{{ band }}</code>
        </label>
      </div>
    </fieldset>
    <fieldset v-if="allThermalBands.length" class="band-filter">
      <legend>Includes all selected thermal bands</legend>
      <div class="band-options">
        <label
          v-for="band in allThermalBands"
          :key="band"
          class="band-option"
          :class="{ selected: advanced.bands.includes(band) }"
        >
          <input v-model="advanced.bands" type="checkbox" :value="band">
          <code>{{ band }}</code>
        </label>
      </div>
    </fieldset>
    <fieldset v-if="allPolarizations.length" class="band-filter">
      <legend>Includes all selected radar polarizations</legend>
      <div class="band-options">
        <label
          v-for="polarization in allPolarizations"
          :key="polarization"
          class="band-option"
          :class="{ selected: advanced.polarizations.includes(polarization) }"
        >
          <input
            v-model="advanced.polarizations"
            type="checkbox"
            :value="polarization"
          >
          <code>{{ polarization }}</code>
        </label>
      </div>
    </fieldset>
    <fieldset class="band-filter">
      <legend>Includes all selected constants</legend>
      <div class="band-options">
        <label
          v-for="constant in allConstants"
          :key="constant"
          class="band-option"
          :class="{ selected: advanced.constants.includes(constant) }"
        >
          <input v-model="advanced.constants" type="checkbox" :value="constant">
          <code>{{ constant }}</code>
        </label>
      </div>
    </fieldset>
    <fieldset class="band-filter">
      <legend>Includes all selected external variables</legend>
      <div class="band-options">
        <label
          v-for="externalVariable in allExternalVariables"
          :key="externalVariable"
          class="band-option"
          :class="{ selected: advanced.externalVariables.includes(externalVariable) }"
        >
          <input
            v-model="advanced.externalVariables"
            type="checkbox"
            :value="externalVariable"
          >
          <code>{{ externalVariable }}</code>
        </label>
      </div>
    </fieldset>
    <button class="clear-button" type="button" @click="clearFilters">
      Clear all filters
    </button>
  </div>
</div>

<p class="result-count" aria-live="polite">
  {{ filteredIndices.length }} of {{ indices.length }} indices found
</p>

<div v-if="groupedIndices.length" class="modality-groups">
  <section
    v-for="modalityGroup in groupedIndices"
    :key="modalityGroup.key"
    class="modality-group"
  >
    <h2 :id="`modality-${modalityGroup.key}`">
      {{ modalityGroup.label }}
      <span>{{ modalityGroup.indices.length }}</span>
    </h2>
    <div class="domain-groups">
      <section
        v-for="domainGroup in modalityGroup.domains"
        :key="`${modalityGroup.key}-${domainGroup.domain}`"
        class="domain-group"
      >
        <h3 :id="`${modalityGroup.key}-${domainGroup.domain}`">
          {{ domainLabels[domainGroup.domain] }}
          <span>{{ domainGroup.indices.length }}</span>
        </h3>
        <div class="index-grid">
          <article
            v-for="index in domainGroup.indices"
            :key="index.key"
            class="index-card"
          >
            <h4>
              <a :href="indexLink(index.key)">{{ index.acronym }}</a>
            </h4>
            <p>{{ index.name }}</p>
            <div class="index-bands">
              <code v-for="band in index.bands" :key="band">{{ band }}</code>
              <code
                v-for="polarization in index.polarizations"
                :key="polarization"
              >
                {{ polarization }}
              </code>
            </div>
          </article>
        </div>
      </section>
    </div>
  </section>
</div>

<div v-else class="empty-state">
  <h2>No indices found</h2>
  <p>Try removing a band or broadening one of the search fields.</p>
  <button class="clear-button" type="button" @click="clearFilters">
    Clear all filters
  </button>
</div>

<style scoped>
.catalogue-tools,
.result-count,
.modality-groups,
.empty-state {
  --catalogue-glass-border: color-mix(
    in srgb,
    var(--asi-accent) 24%,
    var(--vp-c-divider)
  );
  --catalogue-glass-surface: color-mix(
    in srgb,
    var(--vp-c-bg-soft) 74%,
    transparent
  );
}

.catalogue-tools {
  margin: 1.5rem 0 1rem;
}

.primary-search {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 0.75rem;
}

.primary-search input,
.advanced-search input,
.advanced-search select {
  width: 100%;
  min-height: 2.75rem;
  border: 1px solid var(--catalogue-glass-border);
  border-radius: 14px;
  background: color-mix(in srgb, var(--vp-c-bg) 82%, transparent);
  box-shadow: inset 0 1px 0 rgb(255 255 255 / 18%);
  color: var(--vp-c-text-1);
  padding: 0.65rem 0.8rem;
  font: inherit;
}

.primary-search input {
  border-radius: 999px;
  padding-inline: 1.1rem;
}

.primary-search input:focus,
.advanced-search input:focus,
.advanced-search select:focus {
  border-color: var(--vp-c-brand-1);
  outline: 3px solid color-mix(in srgb, var(--vp-c-brand-1) 18%, transparent);
}

.advanced-button,
.clear-button {
  min-height: 2.75rem;
  border: 1px solid var(--vp-button-brand-border);
  border-radius: 12px;
  background: var(--vp-button-brand-bg);
  color: var(--vp-button-brand-text);
  padding: 0.65rem 1rem;
  font-weight: 600;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  transition:
    border-color 0.2s ease,
    background-color 0.2s ease,
    box-shadow 0.2s ease;
}

.advanced-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-color: color-mix(
    in srgb,
    var(--asi-accent-bright) 62%,
    var(--vp-c-brand-1)
  );
  border-radius: 999px;
  background:
    linear-gradient(
      135deg,
      rgb(255 255 255 / 28%),
      transparent 36%,
      color-mix(in srgb, var(--asi-accent-bright) 18%, transparent)
    ),
    color-mix(in srgb, var(--vp-button-brand-bg) 84%, transparent);
  box-shadow:
    0 0 18px color-mix(in srgb, var(--asi-accent) 24%, transparent),
    inset 0 1px 0 rgb(255 255 255 / 34%),
    inset 0 -1px 0 rgb(0 0 0 / 8%);
  padding-inline: 1.25rem;
  white-space: nowrap;
  backdrop-filter: blur(14px) saturate(145%);
  -webkit-backdrop-filter: blur(14px) saturate(145%);
}

.advanced-button::after,
.clear-button::after {
  position: absolute;
  top: -70%;
  left: -45%;
  width: 28%;
  height: 240%;
  background: linear-gradient(
    to right,
    transparent,
    rgb(255 255 255 / 58%),
    transparent
  );
  content: "";
  pointer-events: none;
  transform: skewX(-20deg);
}

.advanced-button:hover,
.clear-button:hover {
  border-color: var(--vp-button-brand-hover-border);
  background: var(--vp-button-brand-hover-bg);
  color: var(--vp-button-brand-hover-text);
  box-shadow: 0 0 26px color-mix(
    in srgb,
    var(--asi-accent) 42%,
    transparent
  );
}

.advanced-button:hover {
  background:
    linear-gradient(
      135deg,
      rgb(255 255 255 / 34%),
      transparent 38%,
      color-mix(in srgb, var(--asi-accent-bright) 24%, transparent)
    ),
    color-mix(in srgb, var(--vp-button-brand-hover-bg) 88%, transparent);
  box-shadow:
    0 0 32px color-mix(in srgb, var(--asi-accent-bright) 48%, transparent),
    inset 0 1px 0 rgb(255 255 255 / 42%);
}

.advanced-button:hover::after,
.clear-button:hover::after {
  left: 125%;
}

.advanced-search {
  margin-top: 0.85rem;
  border: 1px solid var(--catalogue-glass-border);
  border-radius: 20px;
  background:
    linear-gradient(
      135deg,
      color-mix(in srgb, var(--asi-accent) 10%, transparent),
      transparent 52%
    ),
    var(--catalogue-glass-surface);
  box-shadow:
    0 16px 36px rgb(26 55 32 / 9%),
    inset 0 1px 0 rgb(255 255 255 / 24%);
  padding: 1.2rem;
}

.field-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.9rem;
}

.field-grid label {
  display: grid;
  gap: 0.35rem;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  font-weight: 600;
}

.band-filter {
  margin: 1rem 0;
  border: 0;
  padding: 0;
}

.band-filter legend {
  margin-bottom: 0.6rem;
  color: var(--vp-c-text-2);
  font-size: 0.9rem;
  font-weight: 600;
}

.band-options {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.band-option {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  border: 1px solid var(--catalogue-glass-border);
  border-radius: 999px;
  background: color-mix(in srgb, var(--vp-c-bg) 78%, transparent);
  padding: 0.3rem 0.6rem;
  cursor: pointer;
  transition:
    border-color 0.2s ease,
    background-color 0.2s ease;
}

.band-option.selected {
  border-color: var(--vp-c-brand-1);
  background: color-mix(
    in srgb,
    var(--vp-c-brand-soft) 78%,
    var(--vp-c-bg)
  );
}

.band-option input {
  width: auto;
  min-height: auto;
  margin: 0;
}

.result-count {
  margin: 1rem 0 0;
  color: var(--vp-c-text-2);
}

.modality-group {
  margin-top: 2.5rem;
}

.modality-group > h2,
.domain-group h3 {
  display: flex;
  align-items: baseline;
  gap: 0.55rem;
  border-top: 0;
  padding-top: 0;
}

.modality-group > h2 {
  margin-bottom: 0.5rem;
  color: var(--vp-c-brand-1);
}

.domain-groups {
  margin-left: 1rem;
}

.domain-group {
  margin-top: 1.5rem;
}

.domain-group h3 {
  margin-bottom: 0.8rem;
  color: var(--vp-c-text-1);
  font-size: 1.15rem;
}

.modality-group > h2 span,
.domain-group h3 span {
  color: var(--vp-c-text-3);
  font-size: 0.85rem;
  font-weight: 500;
}

.index-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.8rem;
}

.index-card {
  border: 1px solid color-mix(
    in srgb,
    var(--asi-accent) 16%,
    var(--vp-c-divider)
  );
  border-radius: 16px;
  background:
    linear-gradient(
      135deg,
      color-mix(in srgb, var(--asi-accent) 6%, transparent),
      transparent 62%
    ),
    color-mix(in srgb, var(--vp-c-bg) 76%, transparent);
  box-shadow:
    0 8px 22px rgb(26 55 32 / 5%),
    inset 0 1px 0 rgb(255 255 255 / 18%);
  padding: 1rem;
  transition:
    border-color 0.2s ease,
    box-shadow 0.2s ease,
    transform 0.2s ease;
}

.index-card:hover {
  border-color: color-mix(
    in srgb,
    var(--asi-accent) 62%,
    var(--vp-c-divider)
  );
  box-shadow:
    0 12px 28px rgb(26 55 32 / 11%),
    inset 0 1px 0 rgb(255 255 255 / 24%);
  transform: translateY(-2px);
}

.index-card h4 {
  margin: 0;
  border: 0;
  padding: 0;
  font-size: 1rem;
}

.index-card h4 a {
  color: var(--vp-c-brand-1);
}

.index-card p {
  margin: 0.35rem 0 0.75rem;
  color: var(--vp-c-text-2);
}

.index-bands {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
}

.index-bands code {
  border: 1px solid color-mix(
    in srgb,
    var(--asi-accent) 16%,
    transparent
  );
  border-radius: 5px;
  background: color-mix(in srgb, var(--vp-c-brand-soft) 54%, var(--vp-c-bg));
  color: var(--vp-c-brand-1);
  padding: 0.15rem 0.35rem;
}

.empty-state {
  margin-top: 1.5rem;
  border: 1px dashed var(--catalogue-glass-border);
  border-radius: 20px;
  background:
    linear-gradient(
      135deg,
      color-mix(in srgb, var(--asi-accent) 8%, transparent),
      transparent
    ),
    var(--catalogue-glass-surface);
  box-shadow: 0 16px 36px rgb(26 55 32 / 8%);
  padding: 2rem;
  text-align: center;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}

.empty-state h2 {
  margin-top: 0;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  clip-path: inset(50%);
}

@media (max-width: 700px) {
  .primary-search,
  .field-grid,
  .index-grid {
    grid-template-columns: 1fr;
  }

  .domain-group {
    margin-top: 1.6rem;
  }

  .domain-groups {
    margin-left: 0;
  }
}

@media (prefers-reduced-motion: no-preference) {
  .advanced-button::after,
  .clear-button::after {
    transition: left 0.55s ease;
  }
}
</style>

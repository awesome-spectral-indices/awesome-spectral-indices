<script setup>
import { ref } from 'vue'
import { withBase } from 'vitepress'
import catalogue from '../../../../output/v1/spectral-indices-dict.json'
import bandMetadata from '../../../../output/v1/bands.json'

const props = defineProps({
  indexKey: {
    type: String,
    required: true
  }
})

const routeOverrides = {
  BAI: 'BAI-burn',
  BaI: 'BaI-soil',
  MSR705: 'MSR705-ratio',
  mSR705: 'mSR705-modified'
}

const polarizationDescriptions = {
  HH: 'Horizontal transmit, horizontal receive radar polarization',
  HV: 'Horizontal transmit, vertical receive radar polarization',
  VH: 'Vertical transmit, horizontal receive radar polarization',
  VV: 'Vertical transmit, vertical receive radar polarization'
}

const reductionScopeDescriptions = {
  aoi: 'Area of interest (AOI)',
  scene: 'Complete input scene'
}

const tabs = [
  { key: 'formula', label: 'Formula' },
  { key: 'citation', label: 'Cite this Index' },
  { key: 'contribution', label: 'Contribution Details' }
]

const activeTab = ref('formula')

const index = catalogue.SpectralIndices[props.indexKey]
if (!index) throw new Error(`Unknown spectral-index key: ${props.indexKey}`)

const metadata = index.source?.source_metadata ?? {}
const apaCitation = metadata.how_to_cite?.apa ?? null
const publicationYear = metadata.year ?? null
const applicationDomain = index.classification.application_domain.replaceAll('_', ' ')
const sensingModalityText = formatList(
  index.classification.sensing_modalities.map((value) => value.replaceAll('_', ' '))
)
const bands = index.bands.map((name) => ({
  name,
  description: describeBand(name)
}))
const polarizations = index.polarizations.map((name) => ({
  name,
  description: polarizationDescriptions[name] ?? name
}))
const constants = Object.entries(index.constants)
const externalVariables = Object.entries(index.external_variables)
const reductions = Object.entries(index.reductions)
const families = index.classification.family ?? []
const sourceCompanions = index.source.source_companions ?? []
const contributor = contributorDetails(index.contributor)

function formatList(values) {
  if (values.length < 2) return values[0] ?? ''
  if (values.length === 2) return values.join(' and ')
  return `${values.slice(0, -1).join(', ')}, and ${values.at(-1)}`
}

function titleCase(value) {
  return value
    .replaceAll('_', ' ')
    .replace(/\b\w/g, (character) => character.toUpperCase())
}

function sentence(value) {
  const text = String(value).trim()
  return /[.!?]$/.test(text) ? text : `${text}.`
}

function describeBand(name) {
  if (bandMetadata[name]) return bandMetadata[name].long_name

  const range = name.match(/^R([1-9][0-9]*)_([1-9][0-9]*)$/)
  if (range) {
    return `Reflectance at one selected wavelength from ${range[1]} to ${range[2]} nm, inclusive`
  }

  const wavelength = name.match(/^R([1-9][0-9]*)$/)
  if (wavelength) return `Reflectance at ${wavelength[1]} nm`
  return name
}

function displayValue(value) {
  if (Array.isArray(value)) return `${value[0]}–${value[1]}`
  return String(value)
}

function companionLink(key) {
  return withBase(`/indices/${encodeURIComponent(routeOverrides[key] ?? key)}`)
}

function contributorDetails(value) {
  if (value.includes('@') && !value.startsWith('http')) {
    return { href: `mailto:${value}`, label: value }
  }

  try {
    const url = new URL(value)
    if (url.hostname === 'github.com' || url.hostname === 'www.github.com') {
      const username = url.pathname.split('/').filter(Boolean)[0]
      if (username) return { href: value, label: `@${username}` }
    }
  } catch {
    // Validation already guarantees a GitHub profile or email address.
  }

  return { href: value, label: value }
}
</script>

<template>
  <div class="index-details-shell">
    <section class="index-summary" aria-labelledby="index-summary-heading">
      <h2 id="index-summary-heading">Summary</h2>
      <p class="index-summary-text">
        The <strong>{{ index.name }} ({{ index.acronym }})</strong> is a
        <strong>{{ applicationDomain }}</strong> spectral index intended for
        <strong>{{ sensingModalityText }}</strong> sensing.
        <template v-if="publicationYear">
          It was introduced in <strong>{{ publicationYear }}</strong>;
          <template v-if="apaCitation">
            its source is cited as
            <a
              :href="index.source.source_link"
              target="_blank"
              rel="noopener noreferrer"
              class="index-summary-source"
            >{{ apaCitation }} <span aria-hidden="true">🡕</span></a>.
          </template>
          <template v-else>
            consult its
            <a
              :href="index.source.source_link"
              target="_blank"
              rel="noopener noreferrer"
              class="index-summary-source"
            >original source <span aria-hidden="true">🡕</span></a>.
          </template>
        </template>
        <template v-else>
          <template v-if="apaCitation">Its source is cited as</template>
          <template v-else>Consult its</template>
          {{ ' ' }}
          <a
            :href="index.source.source_link"
            target="_blank"
              rel="noopener noreferrer"
              class="index-summary-source"
          ><template v-if="apaCitation">{{ apaCitation }}</template><template v-else>original source</template> <span aria-hidden="true">🡕</span></a>.
        </template>
      </p>

      <template v-if="sourceCompanions.length">
        <h3>Other indices from the same source</h3>
        <p class="index-tab-intro">
          These catalogue entries share this index's scientific source and
          citation.
        </p>
        <div class="source-companion-list">
          <a
            v-for="key in sourceCompanions"
            :key="key"
            :href="companionLink(key)"
            class="source-companion-link"
          >
            {{ key }}
          </a>
        </div>
      </template>
    </section>

    <nav
      class="index-details-tabs"
      role="tablist"
      aria-label="Spectral index information"
    >
      <button
        v-for="tab in tabs"
        :id="`index-tab-${tab.key}`"
        :key="tab.key"
        type="button"
        role="tab"
        :aria-controls="`index-panel-${tab.key}`"
        :aria-selected="activeTab === tab.key"
        @click="activeTab = tab.key"
      >
        {{ tab.label }}
      </button>
    </nav>

    <section
      v-show="activeTab === 'formula'"
      id="index-panel-formula"
      class="index-tab-panel"
      role="tabpanel"
      aria-labelledby="index-tab-formula"
    >
      <h2>Formula</h2>

      <div class="language-text index-formula-code">
        <pre><code>{{ index.formula }}</code></pre>
      </div>

      <div v-if="families.length" class="index-family-row">
        <span class="index-detail-label">Index family</span>
        <span
          v-for="family in families"
          :key="family"
          class="index-family-badge"
        >
          {{ titleCase(family) }}
        </span>
      </div>

      <h3>Bands</h3>
      <div class="index-variable-list">
        <article
          v-for="band in bands"
          :key="band.name"
          class="index-variable-panel"
        >
          <header class="index-variable-header">
            <code class="index-variable-symbol">{{ band.name }}</code>
            <p>{{ sentence(band.description) }}</p>
          </header>
        </article>
        <article v-if="!bands.length" class="index-variable-panel is-empty">
          No spectral, thermal, or hyperspectral bands are used in this index.
        </article>
      </div>

      <h3>Polarizations</h3>
      <div class="index-variable-list">
        <article
          v-for="polarization in polarizations"
          :key="polarization.name"
          class="index-variable-panel"
        >
          <header class="index-variable-header">
            <code class="index-variable-symbol">{{ polarization.name }}</code>
            <p>{{ sentence(polarization.description) }}</p>
          </header>
        </article>
        <article
          v-if="!polarizations.length"
          class="index-variable-panel is-empty"
        >
          No radar polarizations are used in this index.
        </article>
      </div>

      <h3>Constants</h3>
      <div class="constant-list">
        <article
          v-for="[name, definition] in constants"
          :key="name"
          class="constant-panel"
        >
          <header class="constant-panel-header">
            <code class="constant-symbol">{{ name }}</code>
            <p>{{ sentence(definition.description) }}</p>
          </header>
          <div class="constant-details">
            <div
              class="constant-detail-card constant-default"
              :class="{ 'is-empty': definition.default_value == null }"
            >
              <span class="constant-detail-label">Default value</span>
              <strong class="constant-detail-value">
                {{ definition.default_value ?? 'Not specified' }}
              </strong>
            </div>
            <div
              v-if="definition.suggested_range"
              class="constant-detail-card constant-range"
            >
              <span class="constant-detail-label">Suggested range</span>
              <strong class="constant-detail-value">
                {{ displayValue(definition.suggested_range) }}
              </strong>
            </div>
            <div
              v-if="definition.suggested_values"
              class="constant-detail-card constant-suggested-values"
            >
              <span class="constant-detail-label">Suggested values</span>
              <dl>
                <div
                  v-for="(value, condition) in definition.suggested_values"
                  :key="condition"
                  class="constant-suggestion-row"
                >
                  <dt>{{ condition }}</dt>
                  <dd>{{ displayValue(value) }}</dd>
                </div>
              </dl>
            </div>
          </div>
        </article>
        <article v-if="!constants.length" class="index-variable-panel is-empty">
          No constants are used in this index.
        </article>
      </div>

      <template v-if="externalVariables.length">
        <h3>External Variables</h3>
        <div class="index-variable-list">
          <article
            v-for="[name, definition] in externalVariables"
            :key="name"
            class="index-variable-panel"
          >
            <header class="index-variable-header">
              <code class="index-variable-symbol">{{ name }}</code>
              <p>{{ sentence(definition.description) }}</p>
            </header>
          </article>
        </div>
      </template>

      <h3>Reductions</h3>
      <div class="index-variable-list">
        <article
          v-for="[dimension, definition] in reductions"
          :key="dimension"
          class="index-variable-panel"
        >
          <header class="index-variable-header">
            <code class="index-variable-symbol">{{ dimension }}</code>
            <p>Context shared by the formula's spatial reduction functions.</p>
          </header>
          <div class="constant-details">
            <div class="constant-detail-card">
              <span class="constant-detail-label">Scope</span>
              <strong class="constant-detail-value">
                {{ reductionScopeDescriptions[definition.scope] ?? definition.scope }}
              </strong>
            </div>
          </div>
        </article>
        <article v-if="!reductions.length" class="index-variable-panel is-empty">
          No contextual reductions are used in this index.
        </article>
      </div>
    </section>

    <section
      v-show="activeTab === 'citation'"
      id="index-panel-citation"
      class="index-tab-panel"
      role="tabpanel"
      aria-labelledby="index-tab-citation"
    >
      <h2>Cite this Index</h2>
      <p v-if="$slots.default" class="index-tab-intro">
        Use either format below to cite the scientific source associated with
        this index.
      </p>

      <div v-if="$slots.default" class="index-citation-slot">
        <slot />
      </div>

      <article v-else class="index-variable-panel is-empty citation-empty">
        Citation formats are not yet available for this index's source.
      </article>

      <template v-if="sourceCompanions.length">
        <h3>Indices from the same source</h3>
        <p class="index-tab-intro">
          These catalogue entries share this index's scientific source and
          citation.
        </p>
        <div class="source-companion-list">
          <a
            v-for="key in sourceCompanions"
            :key="key"
            :href="companionLink(key)"
            class="source-companion-link"
          >
            {{ key }}
          </a>
        </div>
      </template>
    </section>

    <section
      v-show="activeTab === 'contribution'"
      id="index-panel-contribution"
      class="index-tab-panel"
      role="tabpanel"
      aria-labelledby="index-tab-contribution"
    >
      <h2>Contribution Details</h2>
      <div class="contribution-detail-grid">
        <article class="contribution-detail-card">
          <span class="index-detail-label">Contributor</span>
          <a :href="contributor.href">{{ contributor.label }}</a>
        </article>
        <article class="contribution-detail-card">
          <span class="index-detail-label">Date contributed</span>
          <time :datetime="index.date_of_addition">
            {{ index.date_of_addition }}
          </time>
        </article>
      </div>
    </section>
  </div>
</template>

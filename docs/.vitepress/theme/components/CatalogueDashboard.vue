<script setup>
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import catalogue from '../../../../output/v1/spectral-indices-dict.json'

const domainDefinitions = [
  ['vegetation', 'Vegetation', 'linear-gradient(90deg, #386641, #6a994e 58%, #a7c957)'],
  ['water', 'Water', 'linear-gradient(90deg, #005f73, #0a9396 58%, #79cdcf)'],
  ['burn', 'Burn', 'linear-gradient(90deg, #d00000, #f48c06 62%, #ffba08)'],
  ['snow', 'Snow', 'linear-gradient(90deg, #495057, #6c757d 58%, #b1b6bb)'],
  ['urban', 'Urban', 'linear-gradient(90deg, #003566, #d3b000 70%, #ffd60a)'],
  ['soil', 'Soil', 'linear-gradient(90deg, #99582a, #bb9457 58%, #ffe6a7)'],
  ['geology', 'Geology', 'linear-gradient(90deg, #8a4f22, #c6874c 58%, #f4d5a6)'],
  ['clouds', 'Clouds', 'linear-gradient(90deg, #0077b6, #60e1f7 58%, #abf1ff)']
].map(([key, label, gradient]) => ({ key, label, gradient }))

const domainDefinitionByKey = Object.fromEntries(
  domainDefinitions.map((domain) => [domain.key, domain])
)

const modalityDefinitions = [
  ['multispectral', 'Multispectral', 'linear-gradient(90deg, #166534, #4d9b65 58%, #a7c957)'],
  ['hyperspectral', 'Hyperspectral', 'linear-gradient(90deg, #5b21b6, #db2777 52%, #0891b2)'],
  ['thermal', 'Thermal', 'linear-gradient(90deg, #b91c1c, #f97316 58%, #fbbf24)'],
  ['radar', 'Radar', 'linear-gradient(90deg, #374151, #6b7280 58%, #d1d5db)']
].map(([key, label, gradient]) => ({ key, label, gradient }))

const typeDefinitions = {
  article: ['Article', 'linear-gradient(90deg, #164e63, #0891b2 58%, #67e8f9)'],
  book: ['Book', 'linear-gradient(90deg, #713f12, #ca8a04 58%, #fde047)'],
  book_chapter: ['Book chapter', 'linear-gradient(90deg, #78350f, #d97706 58%, #fbbf24)'],
  conference_paper: ['Conference paper', 'linear-gradient(90deg, #4c1d95, #7c3aed 58%, #c4b5fd)'],
  poster: ['Poster', 'linear-gradient(90deg, #831843, #db2777 58%, #f9a8d4)'],
  report: ['Report', 'linear-gradient(90deg, #334155, #64748b 58%, #cbd5e1)'],
  preprint: ['Preprint', 'linear-gradient(90deg, #9a3412, #ea580c 58%, #fdba74)']
}

const routeOverrides = {
  BAI: 'BAI-burn',
  BaI: 'BaI-soil',
  MSR705: 'MSR705-ratio',
  mSR705: 'mSR705-modified'
}

const tabs = [
  { key: 'counts', label: 'Number of indices' },
  { key: 'publications', label: 'Publications' },
  { key: 'citations', label: 'Citations' }
]

const indices = Object.entries(catalogue.SpectralIndices)
  .map(([key, index]) => ({ key, ...index }))
  .sort((left, right) => left.key.localeCompare(right.key))
const totalIndices = indices.length
const activeTab = ref('counts')
const selection = ref(null)

function metadata(index) {
  return index.source?.source_metadata ?? {}
}

function countDefinitions(definitions, predicate) {
  return definitions
    .map((definition) => ({
      ...definition,
      count: indices.filter((index) => predicate(index, definition.key)).length
    }))
    .sort((left, right) => right.count - left.count || left.label.localeCompare(right.label))
}

function countedMetadata(field) {
  const counts = new Map()
  for (const index of indices) {
    const value = metadata(index)[field]
    if (value !== null && value !== undefined && String(value).trim()) {
      const key = typeof value === 'string' ? value.trim() : value
      counts.set(key, (counts.get(key) ?? 0) + 1)
    }
  }
  return counts
}

const domainBars = countDefinitions(
  domainDefinitions,
  (index, key) => index.classification.application_domain === key
)
const modalityBars = countDefinitions(
  modalityDefinitions,
  (index, key) => index.classification.sensing_modalities.includes(key)
)

const yearBars = [...countedMetadata('year').entries()]
  .map(([key, count]) => ({
    key,
    label: String(key),
    count,
    gradient: 'linear-gradient(90deg, #334155, #64748b 58%, #cbd5e1)'
  }))
  .sort((left, right) => left.key - right.key)

const journalBars = [...countedMetadata('journal').entries()]
  .map(([key, count]) => ({
    key,
    label: key,
    count,
    gradient: 'linear-gradient(90deg, #075985, #0284c7 58%, #7dd3fc)'
  }))
  .sort((left, right) => right.count - left.count || left.label.localeCompare(right.label))

const sourceTypeBars = [...countedMetadata('type').entries()]
  .map(([key, count]) => ({
    key,
    label: typeDefinitions[key]?.[0] ?? key.replaceAll('_', ' '),
    count,
    gradient:
      typeDefinitions[key]?.[1] ??
      'linear-gradient(90deg, #334155, #64748b 58%, #cbd5e1)'
  }))
  .sort((left, right) => right.count - left.count || left.label.localeCompare(right.label))

const citationBars = indices
  .filter((index) => Number.isInteger(metadata(index).citations?.citation_count))
  .map((index) => ({
    key: index.key,
    label: index.key,
    name: index.name,
    domain: index.classification.application_domain,
    count: metadata(index).citations.citation_count,
    gradient:
      domainDefinitionByKey[index.classification.application_domain]?.gradient ??
      'linear-gradient(90deg, #334155, #64748b 58%, #cbd5e1)'
  }))
  .sort((left, right) => right.count - left.count || left.label.localeCompare(right.label))

function maximum(bars) {
  return Math.max(...bars.map((item) => item.count), 0)
}

const citationDomainCharts = domainDefinitions
  .map((domain) => {
    const bars = citationBars.filter((item) => item.domain === domain.key)
    return {
      key: `citation-${domain.key}`,
      selectionKind: 'citation',
      kicker: domain.label,
      title: `${domain.label} indices by citation count`,
      badge: `${bars.length} with data`,
      bars,
      maximum: maximum(bars),
      scroll: true,
      logarithmic: true,
      chartClass: 'domain-citation-chart',
      rowClass: 'citation-row'
    }
  })

const datedIndices = yearBars.reduce((total, item) => total + item.count, 0)
const journalledIndices = journalBars.reduce((total, item) => total + item.count, 0)
const typedIndices = sourceTypeBars.reduce((total, item) => total + item.count, 0)

const charts = {
  counts: [
    {
      key: 'domain',
      kicker: 'Applications',
      title: 'Indices by application domain',
      badge: `${totalIndices} total`,
      bars: domainBars,
      maximum: maximum(domainBars)
    },
    {
      key: 'modality',
      kicker: 'Measurements',
      title: 'Indices by sensing modality',
      badge: 'May overlap',
      note: 'An index is counted in every modality required by its formula.',
      bars: modalityBars,
      maximum: maximum(modalityBars)
    }
  ],
  publications: [
    {
      key: 'year',
      kicker: 'Timeline',
      title: 'Indices by publication year',
      badge: `${datedIndices} dated`,
      note: `${totalIndices - datedIndices} indices have no publication year available.`,
      bars: yearBars,
      maximum: maximum(yearBars),
      scroll: true
    },
    {
      key: 'journal',
      kicker: 'Venues',
      title: 'Indices by journal or proceedings',
      badge: `${journalBars.length} venues`,
      note: `Ranked by catalogue indices. ${totalIndices - journalledIndices} indices have no journal or proceedings metadata available.`,
      bars: journalBars,
      maximum: maximum(journalBars),
      scroll: true
    },
    {
      key: 'type',
      kicker: 'Format',
      title: 'Indices by publication type',
      badge: `${typedIndices} classified`,
      note: `${totalIndices - typedIndices} indices have no publication type available.`,
      bars: sourceTypeBars,
      maximum: maximum(sourceTypeBars),
      wide: true
    }
  ],
  citations: [
    {
      key: 'citation-all',
      selectionKind: 'citation',
      kicker: 'All application domains',
      title: 'All indices by citation count',
      badge: `${citationBars.length} with data`,
      note: `Ranked from most to least cited using the latest retrieved count. Bar lengths use a logarithmic scale; exact counts are shown at right. ${totalIndices - citationBars.length} indices have no citation data.`,
      bars: citationBars,
      maximum: maximum(citationBars),
      scroll: true,
      wide: true,
      logarithmic: true,
      chartClass: 'citation-chart',
      rowClass: 'citation-row'
    },
    ...citationDomainCharts
  ]
}

const visibleCharts = computed(() => charts[activeTab.value])

const selectionKindLabels = {
  domain: 'Application domain',
  modality: 'Sensing modality',
  year: 'Publication year',
  journal: 'Journal or proceedings',
  type: 'Publication type',
  citation: 'Citation ranking'
}

const selectedIndices = computed(() => {
  if (!selection.value) return []
  const { kind, key } = selection.value
  if (kind === 'domain') {
    return indices.filter((index) => index.classification.application_domain === key)
  }
  if (kind === 'modality') {
    return indices.filter((index) => index.classification.sensing_modalities.includes(key))
  }
  if (kind === 'year') return indices.filter((index) => metadata(index).year === key)
  if (kind === 'journal') {
    return indices.filter((index) => metadata(index).journal?.trim() === key)
  }
  if (kind === 'type') return indices.filter((index) => metadata(index).type === key)
  if (kind === 'citation') return indices.filter((index) => index.key === key)
  return []
})

function setActiveTab(tab) {
  activeTab.value = tab
  selection.value = null
}

function handleTabKeydown(event) {
  const current = tabs.findIndex((tab) => tab.key === activeTab.value)
  let next = current
  if (event.key === 'ArrowRight') next = (current + 1) % tabs.length
  else if (event.key === 'ArrowLeft') next = (current - 1 + tabs.length) % tabs.length
  else if (event.key === 'Home') next = 0
  else if (event.key === 'End') next = tabs.length - 1
  else return

  event.preventDefault()
  setActiveTab(tabs[next].key)
  event.currentTarget.parentElement
    ?.querySelector(`#dashboard-tab-${tabs[next].key}`)
    ?.focus()
}

function percentageLabel(count) {
  const value = totalIndices ? (count / totalIndices) * 100 : 0
  if (value === 0 || value === 100) return `${value.toFixed(0)}%`
  return `${value.toFixed(1)}%`
}

function barWidth(chart, count) {
  if (!chart.maximum) return '0%'
  const ratio = chart.logarithmic
    ? Math.log1p(count) / Math.log1p(chart.maximum)
    : count / chart.maximum
  return `${ratio * 100}%`
}

function barLabel(chart, item) {
  if (chartKind(chart) === 'citation') {
    return `${item.label}, ${item.name}: ${item.count.toLocaleString()} citations`
  }
  return `${item.label}: ${item.count} of ${totalIndices} indices (${percentageLabel(item.count)})`
}

function isSelected(kind, key) {
  return selection.value?.kind === kind && selection.value?.key === key
}

function chartKind(chart) {
  return chart.selectionKind ?? chart.key
}

function selectBar(kind, item) {
  selection.value = isSelected(kind, item.key)
    ? null
    : { kind, key: item.key, label: item.label, count: item.count }
}

function indexLink(key) {
  return withBase(`/indices/${encodeURIComponent(routeOverrides[key] ?? key)}`)
}
</script>

<template>
  <div class="catalogue-dashboard">
    <header class="dashboard-header">
      <p class="dashboard-eyebrow">V1 catalogue overview</p>
      <h1>Catalogue Dashboard</h1>
      <p>
        Explore the catalogue's composition, publication history, and citation
        reach. Select a bar to inspect the indices behind it.
      </p>
    </header>

    <nav class="dashboard-tabs" role="tablist" aria-label="Dashboard sections">
      <button
        v-for="tab in tabs"
        :id="`dashboard-tab-${tab.key}`"
        :key="tab.key"
        type="button"
        role="tab"
        :aria-selected="activeTab === tab.key"
        :aria-controls="`dashboard-panel-${tab.key}`"
        :tabindex="activeTab === tab.key ? 0 : -1"
        @click="setActiveTab(tab.key)"
        @keydown="handleTabKeydown"
      >
        {{ tab.label }}
      </button>
    </nav>

    <section
      :id="`dashboard-panel-${activeTab}`"
      class="tab-panel"
      role="tabpanel"
      :aria-labelledby="`dashboard-tab-${activeTab}`"
    >
      <div
        class="dashboard-grid"
        :class="{ 'publication-grid': activeTab === 'publications' }"
      >
        <figure
          v-for="chart in visibleCharts"
          :key="chart.key"
          class="chart-card"
          :class="{ 'wide-card': chart.wide }"
          :aria-labelledby="`${chart.key}-chart-title`"
        >
          <figcaption>
            <div>
              <p class="chart-kicker">{{ chart.kicker }}</p>
              <h2 :id="`${chart.key}-chart-title`">{{ chart.title }}</h2>
            </div>
            <span class="chart-total">{{ chart.badge }}</span>
          </figcaption>

          <p v-if="chart.note" class="chart-note">{{ chart.note }}</p>

          <p v-if="!chart.bars.length" class="empty-chart">
            No citation data are currently available for this application domain.
          </p>

          <div
            v-else
            class="bar-chart"
            :class="[
              `${chart.key}-chart`,
              chart.chartClass,
              { 'scroll-chart': chart.scroll }
            ]"
          >
            <button
              v-for="item in chart.bars"
              :key="item.key"
              type="button"
              class="bar-row"
              :class="[
                `${chart.key}-row`,
                chart.rowClass,
                { selected: isSelected(chartKind(chart), item.key) }
              ]"
              :aria-label="barLabel(chart, item)"
              :aria-pressed="isSelected(chartKind(chart), item.key)"
              aria-controls="dashboard-selection"
              :title="barLabel(chart, item)"
              @click="selectBar(chartKind(chart), item)"
            >
              <span class="bar-label" :title="item.label">{{ item.label }}</span>
              <span class="bar-track" aria-hidden="true">
                <span
                  class="bar-fill"
                  :style="{
                    width: barWidth(chart, item.count),
                    background: item.gradient
                  }"
                ></span>
              </span>
              <strong class="bar-count">
                {{ item.count.toLocaleString() }}
              </strong>
            </button>
          </div>
        </figure>
      </div>
    </section>

    <section
      id="dashboard-selection"
      class="selection-panel"
      :class="{ visible: selection }"
      aria-live="polite"
    >
      <template v-if="selection">
        <header>
          <div>
            <p class="chart-kicker">{{ selectionKindLabels[selection.kind] }}</p>
            <h2>{{ selection.label }}</h2>
            <p v-if="selection.kind === 'citation'">
              {{ selection.count.toLocaleString() }} citations
            </p>
            <p v-else>
              {{ selectedIndices.length }} of {{ totalIndices }} indices
              ({{ percentageLabel(selectedIndices.length) }})
            </p>
          </div>
          <button type="button" class="clear-selection" @click="selection = null">
            Clear selection
          </button>
        </header>

        <div class="index-links">
          <a
            v-for="index in selectedIndices"
            :key="index.key"
            :href="indexLink(index.key)"
            :title="index.name"
          >
            <strong>{{ index.key }}</strong>
            <span>{{ index.name }}</span>
          </a>
        </div>
      </template>
      <p v-else class="selection-placeholder">
        Select any bar to display its spectral indices here.
      </p>
    </section>
  </div>
</template>

<style scoped>
.catalogue-dashboard {
  --dashboard-border: color-mix(in srgb, var(--vp-c-divider) 72%, transparent);
  --dashboard-surface: color-mix(in srgb, var(--vp-c-bg-soft) 80%, transparent);
  --dashboard-shadow: 0 20px 52px rgb(15 23 42 / 8%);
  width: min(1180px, 100%);
  margin: 0 auto;
  padding: 28px 0 42px;
}

:global(.dark) .catalogue-dashboard {
  --dashboard-shadow: 0 22px 56px rgb(0 0 0 / 24%);
}

.dashboard-header {
  max-width: 780px;
  margin-bottom: 26px;
}

.dashboard-eyebrow,
.chart-kicker {
  margin: 0 0 7px;
  color: var(--vp-c-brand-1);
  font-size: 0.72rem;
  font-weight: 750;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.dashboard-header h1 {
  margin: 0;
  border: 0;
  font-size: clamp(2.2rem, 5vw, 3.5rem);
  line-height: 1.04;
  letter-spacing: -0.045em;
}

.dashboard-header > p:last-child {
  margin: 16px 0 0;
  color: var(--vp-c-text-2);
  font-size: 1.02rem;
  line-height: 1.7;
}

.dashboard-tabs {
  display: inline-flex;
  gap: 5px;
  max-width: 100%;
  margin-bottom: 22px;
  padding: 5px;
  overflow-x: auto;
  border: 1px solid var(--dashboard-border);
  border-radius: 14px;
  background: color-mix(in srgb, var(--vp-c-bg-soft) 70%, transparent);
  box-shadow: 0 10px 32px rgb(15 23 42 / 6%);
  backdrop-filter: blur(16px) saturate(125%);
}

.dashboard-tabs button {
  flex: 0 0 auto;
  padding: 9px 16px;
  border: 1px solid transparent;
  border-radius: 10px;
  background: transparent;
  color: var(--vp-c-text-2);
  cursor: pointer;
  font: inherit;
  font-size: 0.82rem;
  font-weight: 700;
  transition:
    border-color 180ms ease,
    background-color 180ms ease,
    box-shadow 180ms ease,
    color 180ms ease;
}

.dashboard-tabs button:hover,
.dashboard-tabs button:focus-visible {
  color: var(--vp-c-brand-1);
  box-shadow: 0 0 22px color-mix(in srgb, var(--vp-c-brand-1) 15%, transparent);
  outline: none;
}

.dashboard-tabs button[aria-selected='true'] {
  border-color: color-mix(in srgb, var(--vp-c-brand-1) 28%, transparent);
  background: color-mix(in srgb, var(--vp-c-brand-soft) 58%, transparent);
  color: var(--vp-c-brand-1);
}

.tab-panel {
  animation: reveal-panel 220ms ease both;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
  align-items: start;
}

.wide-card {
  grid-column: 1 / -1;
}

.chart-card {
  min-width: 0;
  margin: 0;
  padding: 24px;
  border: 1px solid var(--dashboard-border);
  border-radius: 18px;
  background: var(--dashboard-surface);
  box-shadow: var(--dashboard-shadow);
  backdrop-filter: blur(16px) saturate(125%);
}

.chart-card figcaption {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 22px;
}

.chart-card h2,
.selection-panel h2 {
  margin: 0;
  border: 0;
  font-size: 1.2rem;
  line-height: 1.3;
}

.chart-total {
  flex: 0 0 auto;
  padding: 5px 9px;
  border: 1px solid var(--dashboard-border);
  border-radius: 999px;
  color: var(--vp-c-text-2);
  font-size: 0.72rem;
  font-weight: 700;
}

.chart-note {
  margin: -9px 0 18px;
  color: var(--vp-c-text-3);
  font-size: 0.78rem;
  line-height: 1.45;
}

.bar-chart {
  display: grid;
  gap: 8px;
}

.empty-chart {
  margin: 24px 0;
  padding: 28px 18px;
  border: 1px dashed var(--dashboard-border);
  border-radius: 12px;
  color: var(--vp-c-text-3);
  font-size: 0.82rem;
  text-align: center;
}

.scroll-chart {
  max-height: 500px;
  overflow-y: auto;
  padding-right: 6px;
  scrollbar-color: color-mix(in srgb, var(--vp-c-brand-1) 30%, transparent)
    transparent;
  scrollbar-width: thin;
}

.citation-chart {
  max-height: 660px;
}

.modality-chart {
  margin-top: 4px;
}

.bar-row {
  display: grid;
  grid-template-columns: 92px minmax(80px, 1fr) 42px;
  gap: 10px;
  align-items: center;
  width: 100%;
  padding: 7px 8px;
  border: 1px solid transparent;
  border-radius: 10px;
  background: transparent;
  color: var(--vp-c-text-1);
  cursor: pointer;
  font: inherit;
  text-align: left;
  transition:
    border-color 180ms ease,
    background-color 180ms ease,
    box-shadow 180ms ease;
}

.year-row {
  grid-template-columns: 54px minmax(80px, 1fr) 34px;
}

.type-row {
  grid-template-columns: 126px minmax(80px, 1fr) 34px;
}

.journal-row {
  grid-template-columns: minmax(150px, 260px) minmax(100px, 1fr) 34px;
}

.citation-row {
  grid-template-columns: minmax(84px, 120px) minmax(100px, 1fr) 64px;
}

.bar-row:hover,
.bar-row:focus-visible,
.bar-row.selected {
  border-color: color-mix(in srgb, var(--vp-c-brand-1) 36%, transparent);
  background: color-mix(in srgb, var(--vp-c-brand-soft) 48%, transparent);
  box-shadow: 0 0 22px color-mix(in srgb, var(--vp-c-brand-1) 14%, transparent);
  outline: none;
}

.bar-label {
  overflow: hidden;
  font-size: 0.79rem;
  font-weight: 650;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.bar-track {
  display: block;
  overflow: hidden;
  height: 18px;
  border-radius: 5px;
  background: color-mix(in srgb, var(--vp-c-default-soft) 78%, transparent);
}

.bar-fill {
  display: block;
  min-width: 4px;
  height: 100%;
  border-radius: inherit;
  box-shadow: inset 0 1px 0 rgb(255 255 255 / 28%);
  transform-origin: left;
  animation: reveal-bar 650ms cubic-bezier(0.2, 0.75, 0.25, 1) both;
}

.bar-count {
  font-size: 0.82rem;
  font-variant-numeric: tabular-nums;
  text-align: right;
}

.selection-panel {
  min-height: 86px;
  margin-top: 18px;
  padding: 22px 24px;
  border: 1px dashed var(--dashboard-border);
  border-radius: 18px;
  background: color-mix(in srgb, var(--vp-c-bg-soft) 52%, transparent);
}

.selection-panel.visible {
  border-style: solid;
  box-shadow: var(--dashboard-shadow);
}

.selection-panel header {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 18px;
}

.selection-panel header p:last-child {
  margin: 5px 0 0;
  color: var(--vp-c-text-2);
  font-size: 0.82rem;
}

.clear-selection {
  flex: 0 0 auto;
  padding: 7px 11px;
  border: 1px solid var(--dashboard-border);
  border-radius: 999px;
  background: color-mix(in srgb, var(--vp-c-bg) 70%, transparent);
  color: var(--vp-c-text-2);
  cursor: pointer;
  font-size: 0.76rem;
  font-weight: 650;
  transition:
    border-color 180ms ease,
    color 180ms ease,
    box-shadow 180ms ease;
}

.clear-selection:hover,
.clear-selection:focus-visible {
  border-color: var(--vp-c-brand-1);
  color: var(--vp-c-brand-1);
  box-shadow: 0 0 20px color-mix(in srgb, var(--vp-c-brand-1) 18%, transparent);
  outline: none;
}

.index-links {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
  gap: 8px;
  max-height: 390px;
  overflow: auto;
  padding: 2px;
}

.index-links a {
  display: grid;
  gap: 2px;
  min-width: 0;
  padding: 9px 11px;
  border: 1px solid var(--dashboard-border);
  border-radius: 10px;
  background: color-mix(in srgb, var(--vp-c-bg) 68%, transparent);
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition:
    border-color 180ms ease,
    box-shadow 180ms ease;
}

.index-links a:hover,
.index-links a:focus-visible {
  border-color: var(--vp-c-brand-1);
  box-shadow: 0 0 18px color-mix(in srgb, var(--vp-c-brand-1) 16%, transparent);
  outline: none;
}

.index-links strong {
  color: var(--vp-c-brand-1);
  font-size: 0.8rem;
}

.index-links span {
  overflow: hidden;
  color: var(--vp-c-text-2);
  font-size: 0.72rem;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.selection-placeholder {
  margin: 8px 0;
  color: var(--vp-c-text-3);
  font-size: 0.86rem;
  text-align: center;
}

@keyframes reveal-panel {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
}

@keyframes reveal-bar {
  from {
    opacity: 0;
    transform: scaleX(0);
  }
}

@media (max-width: 900px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }

  .wide-card {
    grid-column: auto;
  }
}

@media (max-width: 620px) {
  .catalogue-dashboard {
    padding-top: 14px;
  }

  .chart-card,
  .selection-panel {
    padding: 18px 14px;
    border-radius: 14px;
  }

  .dashboard-tabs {
    display: flex;
  }

  .dashboard-tabs button {
    flex: 1 0 auto;
    padding-inline: 12px;
  }

  .bar-row,
  .year-row,
  .type-row,
  .journal-row,
  .citation-row {
    grid-template-columns: minmax(72px, 96px) minmax(58px, 1fr) 54px;
    gap: 7px;
    padding-inline: 5px;
  }

  .selection-panel header {
    display: grid;
  }

  .clear-selection {
    justify-self: start;
  }
}

@media (prefers-reduced-motion: reduce) {
  .tab-panel,
  .bar-fill {
    animation: none;
  }

  .dashboard-tabs button,
  .bar-row,
  .clear-selection,
  .index-links a {
    transition: none;
  }
}
</style>

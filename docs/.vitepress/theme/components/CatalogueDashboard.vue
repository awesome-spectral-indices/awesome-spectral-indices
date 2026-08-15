<script setup>
import { computed, ref } from 'vue'
import { withBase } from 'vitepress'
import catalogue from '../../../../output/v1/spectral-indices-dict.json'

const domainDefinitions = [
  {
    key: 'vegetation',
    label: 'Vegetation',
    gradient: 'linear-gradient(90deg, #386641, #6a994e 58%, #a7c957)'
  },
  {
    key: 'water',
    label: 'Water',
    gradient: 'linear-gradient(90deg, #005f73, #0a9396 58%, #79cdcf)'
  },
  {
    key: 'burn',
    label: 'Burn',
    gradient: 'linear-gradient(90deg, #d00000, #f48c06 62%, #ffba08)'
  },
  {
    key: 'snow',
    label: 'Snow',
    gradient: 'linear-gradient(90deg, #495057, #6c757d 58%, #b1b6bb)'
  },
  {
    key: 'urban',
    label: 'Urban',
    gradient: 'linear-gradient(90deg, #003566, #d3b000 70%, #ffd60a)'
  },
  {
    key: 'soil',
    label: 'Soil',
    gradient: 'linear-gradient(90deg, #99582a, #bb9457 58%, #ffe6a7)'
  },
  {
    key: 'geology',
    label: 'Geology',
    gradient: 'linear-gradient(90deg, #8a4f22, #c6874c 58%, #f4d5a6)'
  },
  {
    key: 'clouds',
    label: 'Clouds',
    gradient: 'linear-gradient(90deg, #0077b6, #60e1f7 58%, #abf1ff)'
  }
]

const modalityDefinitions = [
  {
    key: 'multispectral',
    label: 'Multispectral',
    gradient: 'linear-gradient(90deg, #166534, #4d9b65 58%, #a7c957)'
  },
  {
    key: 'hyperspectral',
    label: 'Hyperspectral',
    gradient: 'linear-gradient(90deg, #5b21b6, #db2777 52%, #0891b2)'
  },
  {
    key: 'thermal',
    label: 'Thermal',
    gradient: 'linear-gradient(90deg, #b91c1c, #f97316 58%, #fbbf24)'
  },
  {
    key: 'radar',
    label: 'Radar',
    gradient: 'linear-gradient(90deg, #374151, #6b7280 58%, #d1d5db)'
  }
]

const routeOverrides = {
  BAI: 'BAI-burn',
  BaI: 'BaI-soil',
  MSR705: 'MSR705-ratio',
  mSR705: 'mSR705-modified'
}

const indices = Object.entries(catalogue.SpectralIndices)
  .map(([key, index]) => ({ key, ...index }))
  .sort((left, right) => left.key.localeCompare(right.key))

const totalIndices = indices.length
const selection = ref(null)

function countBy(definitions, predicate) {
  return definitions
    .map((definition) => ({
      ...definition,
      count: indices.filter((index) => predicate(index, definition.key)).length
    }))
    .sort((left, right) => right.count - left.count || left.label.localeCompare(right.label))
}

const domainBars = countBy(
  domainDefinitions,
  (index, key) => index.classification.application_domain === key
)

const modalityBars = countBy(
  modalityDefinitions,
  (index, key) => index.classification.sensing_modalities.includes(key)
)

const domainMaximum = Math.max(...domainBars.map((item) => item.count))
const modalityMaximum = Math.max(...modalityBars.map((item) => item.count))

const selectedDefinition = computed(() => {
  if (!selection.value) return null
  const definitions = selection.value.kind === 'domain'
    ? domainDefinitions
    : modalityDefinitions
  return definitions.find((item) => item.key === selection.value.key)
})

const selectedIndices = computed(() => {
  if (!selection.value) return []
  if (selection.value.kind === 'domain') {
    return indices.filter(
      (index) => index.classification.application_domain === selection.value.key
    )
  }
  return indices.filter((index) =>
    index.classification.sensing_modalities.includes(selection.value.key)
  )
})

function percentage(count) {
  if (!totalIndices) return 0
  return (count / totalIndices) * 100
}

function percentageLabel(count) {
  const value = percentage(count)
  if (value === 0 || value === 100) return `${value.toFixed(0)}%`
  return `${value.toFixed(1)}%`
}

function barWidth(count, maximum) {
  return maximum ? `${(count / maximum) * 100}%` : '0%'
}

function barLabel(item) {
  return `${item.label}: ${item.count} of ${totalIndices} indices (${percentageLabel(item.count)})`
}

function isSelected(kind, key) {
  return selection.value?.kind === kind && selection.value?.key === key
}

function selectBar(kind, key) {
  selection.value = isSelected(kind, key) ? null : { kind, key }
}

function indexLink(key) {
  const route = routeOverrides[key] ?? key
  return withBase(`/indices/${encodeURIComponent(route)}`)
}
</script>

<template>
  <div class="catalogue-dashboard">
    <header class="dashboard-header">
      <p class="dashboard-eyebrow">V1 catalogue overview</p>
      <h1>Catalogue Dashboard</h1>
      <p>
        Explore how the {{ totalIndices }} spectral indices are distributed.
        Hover or focus for exact values, and select a bar to inspect its indices.
      </p>
    </header>

    <div class="dashboard-grid">
      <figure class="chart-card" aria-labelledby="domain-chart-title">
        <figcaption>
          <div>
            <p class="chart-kicker">Applications</p>
            <h2 id="domain-chart-title">Indices by application domain</h2>
          </div>
          <span class="chart-total">{{ totalIndices }} total</span>
        </figcaption>

        <div class="bar-chart">
          <button
            v-for="item in domainBars"
            :key="item.key"
            type="button"
            class="bar-row"
            :class="{ selected: isSelected('domain', item.key) }"
            :aria-label="barLabel(item)"
            :aria-pressed="isSelected('domain', item.key)"
            aria-controls="dashboard-selection"
            :title="barLabel(item)"
            @click="selectBar('domain', item.key)"
          >
            <span class="bar-label">{{ item.label }}</span>
            <span class="bar-track" aria-hidden="true">
              <span
                class="bar-fill"
                :style="{
                  width: barWidth(item.count, domainMaximum),
                  background: item.gradient
                }"
              ></span>
            </span>
            <strong class="bar-count">{{ item.count }}</strong>
          </button>
        </div>
      </figure>

      <figure class="chart-card" aria-labelledby="modality-chart-title">
        <figcaption>
          <div>
            <p class="chart-kicker">Measurements</p>
            <h2 id="modality-chart-title">Indices by sensing modality</h2>
          </div>
          <span class="chart-total">May overlap</span>
        </figcaption>

        <p class="chart-note">
          An index is counted in every modality required by its formula.
        </p>

        <div class="bar-chart modality-chart">
          <button
            v-for="item in modalityBars"
            :key="item.key"
            type="button"
            class="bar-row"
            :class="{ selected: isSelected('modality', item.key) }"
            :aria-label="barLabel(item)"
            :aria-pressed="isSelected('modality', item.key)"
            aria-controls="dashboard-selection"
            :title="barLabel(item)"
            @click="selectBar('modality', item.key)"
          >
            <span class="bar-label">{{ item.label }}</span>
            <span class="bar-track" aria-hidden="true">
              <span
                class="bar-fill"
                :style="{
                  width: barWidth(item.count, modalityMaximum),
                  background: item.gradient
                }"
              ></span>
            </span>
            <strong class="bar-count">{{ item.count }}</strong>
          </button>
        </div>
      </figure>
    </div>

    <section
      id="dashboard-selection"
      class="selection-panel"
      :class="{ visible: selection }"
      aria-live="polite"
    >
      <template v-if="selection && selectedDefinition">
        <header>
          <div>
            <p class="chart-kicker">
              {{ selection.kind === 'domain' ? 'Application domain' : 'Sensing modality' }}
            </p>
            <h2>{{ selectedDefinition.label }}</h2>
            <p>
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
  max-width: 760px;
  margin-bottom: 30px;
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

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 18px;
  align-items: start;
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

.modality-chart {
  margin-top: 4px;
}

.bar-row {
  display: grid;
  grid-template-columns: 92px minmax(80px, 1fr) 34px;
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

@keyframes reveal-bar {
  from {
    opacity: 0;
    transform: scaleX(0);
  }
}

@media (max-width: 860px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 520px) {
  .catalogue-dashboard {
    padding-top: 14px;
  }

  .chart-card,
  .selection-panel {
    padding: 18px 14px;
    border-radius: 14px;
  }

  .bar-row {
    grid-template-columns: 78px minmax(58px, 1fr) 30px;
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
  .bar-fill {
    animation: none;
  }

  .bar-row,
  .clear-selection,
  .index-links a {
    transition: none;
  }
}
</style>

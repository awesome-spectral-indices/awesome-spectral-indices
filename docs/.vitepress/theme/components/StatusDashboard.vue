<script setup>
import { ref } from 'vue'
import { withBase } from 'vitepress'
import catalogue from '../../../../output/v1/spectral-indices-dict.json'

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
const linkDetails = ref(null)
const typeDetails = ref(null)

const downIndices = indices.filter(
  (index) => index.source.source_link_status === 'down'
)
const operationalCount = totalIndices - downIndices.length

const preprintIndices = indices.filter(
  (index) => index.source.source_type === 'preprint'
)
const unclassifiedIndices = indices.filter(
  (index) => index.source.source_type === null
)
const classifiedCount =
  totalIndices - preprintIndices.length - unclassifiedIndices.length

const linkSegments = [
  {
    key: 'operational',
    label: 'Operational',
    count: operationalCount,
    className: 'operational'
  },
  {
    key: 'down',
    label: 'Down',
    count: downIndices.length,
    className: 'down'
  }
]

const typeSegments = [
  {
    key: 'classified',
    label: 'Classified',
    count: classifiedCount,
    className: 'operational'
  },
  {
    key: 'preprint',
    label: 'Preprint',
    count: preprintIndices.length,
    className: 'warning'
  },
  {
    key: 'unclassified',
    label: 'Not classified',
    count: unclassifiedIndices.length,
    className: 'down'
  }
]

function percentage(count) {
  return totalIndices ? (count / totalIndices) * 100 : 0
}

function percentageLabel(count) {
  const value = percentage(count)
  if (value === 0 || value === 100) return `${value.toFixed(0)}%`
  return `${value.toFixed(1)}%`
}

function segmentTitle(segment) {
  return `${segment.label}: ${segment.count} of ${totalIndices} (${percentageLabel(segment.count)})`
}

function openLinkDetails() {
  if (linkDetails.value) linkDetails.value.open = true
}

function openTypeDetails() {
  if (typeDetails.value) typeDetails.value.open = true
}

function indexLink(key) {
  const route = routeOverrides[key] ?? key
  return withBase(`/indices/${encodeURIComponent(route)}`)
}
</script>

<template>
<div class="status-page-content">
  <header class="status-page-header">
    <h1>Catalogue Status</h1>
    <p>
      This page provides a current snapshot of metadata quality across the v1
      catalogue. Each bar represents all {{ totalIndices }} spectral indices and
      is calculated directly from the generated catalogue.
    </p>
  </header>

  <div class="status-dashboard">
  <section class="status-block" aria-labelledby="source-links-heading">
    <header class="status-header">
      <div>
        <h2 id="source-links-heading">Source Links</h2>
        <p>Availability of the scientific source linked from each index.</p>
      </div>
      <span class="status-summary operational">
        <span class="status-dot" aria-hidden="true"></span>
        {{ operationalCount }} of {{ totalIndices }} operational
      </span>
    </header>

    <div
      class="status-bar"
      role="group"
      aria-label="Source-link availability"
    >
      <button
        v-for="segment in linkSegments"
        v-show="segment.count"
        :key="segment.key"
        type="button"
        class="status-segment"
        :class="segment.className"
        :style="{ width: `${percentage(segment.count)}%` }"
        :title="segmentTitle(segment)"
        :aria-label="segmentTitle(segment)"
        aria-controls="source-link-details"
        @click="openLinkDetails"
      ></button>
    </div>

    <div class="status-legend" aria-label="Source-link legend">
      <div v-for="segment in linkSegments" :key="segment.key" class="legend-item">
        <span class="legend-swatch" :class="segment.className" aria-hidden="true"></span>
        <span>{{ segment.label }}</span>
        <strong>{{ segment.count }}</strong>
        <small>{{ percentageLabel(segment.count) }}</small>
      </div>
    </div>

    <details id="source-link-details" ref="linkDetails" class="status-details">
      <summary>
        <span>Indices with down source links</span>
        <strong>{{ downIndices.length }}</strong>
      </summary>
      <div class="details-content">
        <p v-if="!downIndices.length" class="empty-status">
          All source links are operational.
        </p>
        <ul v-else class="affected-list">
          <li v-for="index in downIndices" :key="index.key">
            <a :href="indexLink(index.key)">
              <strong>{{ index.acronym }}</strong>
              <span>{{ index.name }}</span>
            </a>
          </li>
        </ul>
      </div>
    </details>
  </section>

  <section class="status-block" aria-labelledby="source-types-heading">
    <header class="status-header">
      <div>
        <h2 id="source-types-heading">Source Types</h2>
        <p>Completeness and publication status of source classifications.</p>
      </div>
      <span class="status-summary" :class="unclassifiedIndices.length ? 'down' : 'operational'">
        <span class="status-dot" aria-hidden="true"></span>
        {{ classifiedCount + preprintIndices.length }} of {{ totalIndices }} classified
      </span>
    </header>

    <div
      class="status-bar"
      role="group"
      aria-label="Source-type completeness"
    >
      <button
        v-for="segment in typeSegments"
        v-show="segment.count"
        :key="segment.key"
        type="button"
        class="status-segment"
        :class="segment.className"
        :style="{ width: `${percentage(segment.count)}%` }"
        :title="segmentTitle(segment)"
        :aria-label="segmentTitle(segment)"
        aria-controls="source-type-details"
        @click="openTypeDetails"
      ></button>
    </div>

    <div class="status-legend" aria-label="Source-type legend">
      <div v-for="segment in typeSegments" :key="segment.key" class="legend-item">
        <span class="legend-swatch" :class="segment.className" aria-hidden="true"></span>
        <span>{{ segment.label }}</span>
        <strong>{{ segment.count }}</strong>
        <small>{{ percentageLabel(segment.count) }}</small>
      </div>
    </div>

    <p class="status-note">
      Classified includes every populated source type except preprints, which
      are shown separately.
    </p>

    <details id="source-type-details" ref="typeDetails" class="status-details">
      <summary>
        <span>Review source-type classifications</span>
        <strong>{{ preprintIndices.length + unclassifiedIndices.length }}</strong>
      </summary>
      <div class="details-content type-details">
        <section>
          <h3>
            Preprints
            <span>{{ preprintIndices.length }}</span>
          </h3>
          <p v-if="!preprintIndices.length" class="empty-status">
            No indices currently use a preprint source.
          </p>
          <ul v-else class="affected-list">
            <li v-for="index in preprintIndices" :key="index.key">
              <a :href="indexLink(index.key)">
                <strong>{{ index.acronym }}</strong>
                <span>{{ index.name }}</span>
              </a>
            </li>
          </ul>
        </section>

        <section>
          <h3>
            Not classified
            <span>{{ unclassifiedIndices.length }}</span>
          </h3>
          <p v-if="!unclassifiedIndices.length" class="empty-status">
            Every index has a source type.
          </p>
          <ul v-else class="affected-list long-list">
            <li v-for="index in unclassifiedIndices" :key="index.key">
              <a :href="indexLink(index.key)">
                <strong>{{ index.acronym }}</strong>
                <span>{{ index.name }}</span>
              </a>
            </li>
          </ul>
        </section>
      </div>
    </details>
  </section>
  </div>
</div>
</template>

<style scoped>
.status-page-content {
  margin: 0 auto;
  max-width: 1152px;
  padding: 48px 24px clamp(4rem, 8vw, 6rem);
}

.status-page-header h1 {
  margin: 0;
  letter-spacing: -0.02em;
  line-height: 1.25;
  font-size: clamp(2rem, 5vw, 3rem);
}

.status-page-header p {
  margin: 0.75rem 0 0;
  max-width: 760px;
  color: var(--vp-c-text-2);
  line-height: 1.7;
  font-size: 1rem;
}

.status-dashboard {
  --status-operational: #2e7d32;
  --status-warning: #d89b00;
  --status-down: #c62828;
  margin-top: 2rem;
}

:global(.dark) .status-dashboard {
  --status-operational: #4ade80;
  --status-warning: #facc15;
  --status-down: #f87171;
}

.status-block {
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  border-radius: 18px;
  background: color-mix(in srgb, var(--vp-c-bg-soft) 82%, transparent);
  box-shadow: 0 14px 34px rgb(0 0 0 / 6%);
}

.status-block + .status-block {
  margin-top: 1.5rem;
}

.status-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1.5rem;
  padding: 1.5rem 1.5rem 1.25rem;
}

.status-header h2 {
  margin: 0;
  border: 0;
  padding: 0;
  font-size: 1.35rem;
}

.status-header p {
  margin: 0.35rem 0 0;
  color: var(--vp-c-text-2);
}

.status-summary {
  display: inline-flex;
  flex-shrink: 0;
  align-items: center;
  gap: 0.5rem;
  border: 1px solid color-mix(in srgb, currentColor 25%, transparent);
  border-radius: 999px;
  padding: 0.4rem 0.7rem;
  font-size: 0.78rem;
  font-weight: 700;
  line-height: 1.2;
}

.status-summary.operational {
  color: var(--status-operational);
}

.status-summary.down {
  color: var(--status-down);
}

.status-dot {
  border-radius: 50%;
  width: 0.55rem;
  height: 0.55rem;
  background: currentColor;
  box-shadow: 0 0 0 4px color-mix(in srgb, currentColor 14%, transparent);
}

.status-bar {
  display: flex;
  margin: 0 1.5rem;
  border-radius: 999px;
  height: 2rem;
  overflow: hidden;
  background: var(--vp-c-bg-alt);
  box-shadow: inset 0 1px 3px rgb(0 0 0 / 14%);
}

.status-segment {
  min-width: 4px;
  border: 0;
  border-radius: 0;
  padding: 0;
  cursor: pointer;
  transition: filter 0.2s ease, box-shadow 0.2s ease;
}

.status-segment:hover {
  filter: brightness(1.14) saturate(1.08);
  box-shadow: inset 0 0 0 2px rgb(255 255 255 / 45%);
}

.status-segment:focus-visible {
  position: relative;
  z-index: 1;
  outline: 3px solid var(--vp-c-brand-1);
  outline-offset: -3px;
}

.status-segment.operational,
.legend-swatch.operational {
  background-color: var(--status-operational);
}

.status-segment.warning,
.legend-swatch.warning {
  background-color: var(--status-warning);
}

.status-segment.down,
.legend-swatch.down {
  background-color: var(--status-down);
}

.status-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem 1.25rem;
  padding: 0.9rem 1.5rem 1.25rem;
}

.legend-item {
  display: grid;
  grid-template-columns: auto auto auto auto;
  align-items: baseline;
  gap: 0.4rem;
  color: var(--vp-c-text-2);
  font-size: 0.82rem;
}

.legend-item strong {
  color: var(--vp-c-text-1);
}

.legend-item small {
  color: var(--vp-c-text-3);
}

.legend-swatch {
  align-self: center;
  border-radius: 50%;
  width: 0.65rem;
  height: 0.65rem;
}

.status-note {
  margin: -0.45rem 1.5rem 1.25rem;
  color: var(--vp-c-text-3);
  font-size: 0.8rem;
}

.status-details {
  border-top: 1px solid var(--vp-c-divider);
}

.status-details summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-weight: 650;
  list-style: none;
  transition: background-color 0.2s ease;
}

.status-details summary::-webkit-details-marker {
  display: none;
}

.status-details summary::before {
  color: var(--vp-c-text-3);
  content: "›";
  font-size: 1.5rem;
  line-height: 1;
  transition: transform 0.2s ease;
}

.status-details[open] summary::before {
  transform: rotate(90deg);
}

.status-details summary:hover {
  background: color-mix(in srgb, var(--vp-c-bg-alt) 65%, transparent);
}

.status-details summary span {
  margin-right: auto;
}

.status-details summary strong,
.type-details h3 span {
  border-radius: 999px;
  padding: 0.15rem 0.5rem;
  color: var(--vp-c-text-2);
  background: var(--vp-c-bg-alt);
  font-size: 0.75rem;
}

.details-content {
  border-top: 1px solid var(--vp-c-divider);
  padding: 1.25rem 1.5rem 1.5rem;
}

.type-details {
  display: grid;
  gap: 1.5rem;
}

.type-details h3 {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  margin: 0 0 0.75rem;
  font-size: 1rem;
}

.affected-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  margin: 0;
  padding: 0;
  list-style: none;
}

.affected-list.long-list {
  max-height: 30rem;
  overflow-y: auto;
  border-top: 1px solid var(--vp-c-divider);
  border-bottom: 1px solid var(--vp-c-divider);
}

.affected-list li {
  border-bottom: 1px solid var(--vp-c-divider);
}

.affected-list a {
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
  padding: 0.7rem 0.8rem;
  color: var(--vp-c-text-1);
  text-decoration: none;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.affected-list a:hover {
  color: var(--vp-c-brand-1);
  background: var(--vp-c-bg-alt);
}

.affected-list a span {
  overflow: hidden;
  color: var(--vp-c-text-2);
  font-size: 0.78rem;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.empty-status {
  margin: 0;
  color: var(--vp-c-text-2);
}

@media (max-width: 640px) {
  .status-header {
    flex-direction: column;
    gap: 0.9rem;
  }

  .status-summary {
    align-self: flex-start;
  }

  .status-bar {
    height: 1.7rem;
  }

  .legend-item {
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .status-segment,
  .status-details summary::before,
  .affected-list a {
    transition: none;
  }
}
</style>

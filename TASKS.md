# Project Tasks

## Current milestone: 1 — Build the market map

### Completed

- [x] Define the portfolio audience and business decision.
- [x] Create the repository structure.
- [x] Record official source endpoints and documentation.
- [x] Add a reusable Census API helper and offline unit tests.
- [x] Create the first analysis notebook outline.

### Next smallest action

- [ ] Inspect the Census MRTS variable metadata and confirm the exact fields, units, seasonal-adjustment flags, and category codes required for the six-category market map.

### Remaining work in milestone 1

- [ ] Obtain and configure a Census API key locally.
- [ ] Write a bounded MRTS extraction function.
- [ ] Save a dated raw extract with source metadata.
- [ ] Validate row uniqueness, monthly continuity, units, and missing values.
- [ ] Create the analysis-ready monthly category table.
- [ ] Calculate year-over-year growth and category market share.
- [ ] Produce the indexed-sales, market-share, and growth-heatmap figures.
- [ ] Write two or three evidence-backed preliminary findings.

## Later milestones

### 2 — Separate inflation from real demand

- [ ] Select and document BLS CPI series.
- [ ] Design a transparent Census-to-CPI category crosswalk.
- [ ] Calculate approximate real sales indexes.
- [ ] Quantify how conclusions change after inflation adjustment.

### 3 — Measure inventory risk

- [ ] Add retail inventory and inventory-to-sales series.
- [ ] Add wholesale indicators as upstream context.
- [ ] Calculate historical percentiles and z-scores.
- [ ] Test lead/lag relationships without making causal claims.

### 4 — Rank category attractiveness

- [ ] Define the score and business rationale.
- [ ] Normalize the component metrics.
- [ ] Run weight and period sensitivity checks.
- [ ] Produce a decision-oriented category comparison.

### 5 — Add forecasting evidence

- [ ] Establish seasonal-naive and last-value baselines.
- [ ] Fit a statistical time-series model.
- [ ] Fit one tree-based model only if it adds value.
- [ ] Evaluate models with expanding or rolling windows.

### 6 — Package for job applications

- [ ] Build a concise Streamlit dashboard.
- [ ] Write the executive market brief.
- [ ] Replace README placeholders with verified findings.
- [ ] Add final screenshots, tests, and CI checks.


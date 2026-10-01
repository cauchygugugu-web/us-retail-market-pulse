# Project Tasks

This file is the durable project checklist. Update it after each meaningful work session.

## Current status

- Current phase: data-access setup
- Current milestone: 1 — build the first retail market map
- Analytical findings: none yet
- GitHub repository: <https://github.com/cauchygugugu-web/us-retail-market-pulse>

## Next smallest action

- [ ] Review and commit the validated single-sample milestone before expanding Census downloads.

Keep the first API request small and bounded; do not write findings before data validation.

## Completed foundation

- [X] Define the business question and six-category scope.
- [x] Create a local Python virtual environment in PyCharm.
- [x] Use a `src/` package layout.
- [x] Add `pyproject.toml` with runtime and development dependencies.
- [x] Add `.gitignore` rules for environments, secrets, caches, generated metadata, and data.
- [x] Add a package-import smoke test.
- [x] Confirm that pytest passes and Ruff reports no errors.
- [x] Create and publish the public GitHub repository.
- [x] Add durable task and future-chat instructions.

## Milestone 1 — Market map

### Source definition

- [x] Verify Census MRTS fields and definitions.
- [x] Verify the exact codes for the six target categories.
- [x] Verify a compatible retail-total series for market-share calculations.
- [x] Record units, frequency, seasonal adjustment, and revision status.
- [x] Create `config/sources.json` with verified endpoints and metadata links.
- [x] Correct the month-identifier description in the source documentation and configuration using the saved sample.

### Data access

- [x] Add `.env.example` without real credentials.
- [x] Configure the Census API key in a local `.env` file.
- [x] Create `src/us_retail_market_pulse/census.py`.
- [x] Add a pure parameter-building function for one MRTS category and one year.
- [x] Add an offline unit test for `build_mrts_params` using a dummy API key.
- [x] Build a bounded URL/request helper.
- [x] Add an offline test that verifies the endpoint, parameters, timeout, and single request.
- [x] Check the HTTP status and report non-200 responses without including the request URL or API key.
- [x] Add an offline test for a non-200 Census response and confirm the error excludes the API key.
- [x] Handle a request timeout with a safe error message and offline test.
- [x] Parse a valid Census MRTS JSON table into row dictionaries with header and row-shape checks.
- [x] Test that a missing required Census MRTS column raises a clear, key-safe error.
- [x] Test that a Census MRTS data row with the wrong value count raises a clear error.
- [x] Test that invalid Census MRTS JSON raises a clear, key-safe error.
- [x] Validate response structure and provide useful errors for malformed results.
- [x] Add offline unit tests for request parameters, endpoint, and response parsing.

### Raw data and validation

- [x] Download and inspect a bounded 2024 MRTS sample for category `441` (12 rows, unique header).
- [x] Preserve the 2024 category `441` raw response unchanged in `data/raw/` (657 bytes).
- [x] Save key-free request parameters, source endpoint, raw filename, and UTC save time in companion metadata.
- [x] Confirm the 2024 category `441` sample has 12 unique `time` months and no gaps.
- [x] Confirm the saved 2024 category `441` sample has no null or blank values.
- [x] Confirm all 12 saved `cell_value` strings convert to numbers without altering the raw extract.
- [x] Confirm all saved rows match category `441`, data type `SM`, seasonal adjustment `yes`, and U.S. geography.
- [x] Add a reusable MRTS row validator and a valid 12-month offline test.
- [x] Test and enforce chronological month order in the MRTS row validator.
- [x] Add focused validator error-path tests for month order and nonnumeric values.
- [x] Run the reusable validator successfully against the saved 2024 category `441` sample.
- [ ] Recheck row uniqueness and monthly continuity when the full period is downloaded.
- [ ] Confirm compatible units and adjustment status across all series.

### Analysis

- [ ] Build an analysis-ready monthly category table.
- [ ] Calculate year-over-year nominal sales growth.
- [ ] Calculate category market share.
- [ ] Calculate an indexed sales series.
- [ ] Create sales-trend, market-share, and growth-heatmap figures.
- [ ] Write two or three preliminary findings supported by verified outputs.

## Milestone 2 — Inflation-adjusted demand

- [ ] Select and document appropriate BLS CPI series.
- [ ] Create a transparent Census-to-CPI category crosswalk.
- [ ] Document imperfect category matches and sensitivity limits.
- [ ] Calculate approximate real sales indexes.
- [ ] Compare nominal and real growth rankings.

## Milestone 3 — Inventory risk

- [ ] Add retail inventory or inventory-to-sales data.
- [ ] Add wholesale indicators only when they provide useful upstream context.
- [ ] Calculate historical percentiles or rolling z-scores.
- [ ] Identify inventory accumulation and normalization periods.
- [ ] Test predictive relationships without making causal claims.

## Milestone 4 — Category attractiveness

- [ ] Define score components and business rationale.
- [ ] Standardize component metrics and document their directions.
- [ ] Choose transparent weights.
- [ ] Rank the six categories.
- [ ] Test sensitivity to weights and analysis periods.
- [ ] Translate the result into a screening recommendation, not an investment claim.

## Milestone 5 — Portfolio presentation

- [ ] Keep reusable logic in `src/`, not only in notebooks.
- [ ] Maintain reviewable notebooks for exploration and explanation.
- [ ] Add focused automated tests for transformations and metrics.
- [ ] Add GitHub Actions for pytest and Ruff.
- [ ] Build a concise Streamlit dashboard.
- [ ] Add selected charts and screenshots to the repository.
- [ ] Rewrite the README around verified findings and reproducible setup.
- [ ] Produce a short decision-oriented market brief.

## Optional stretch work

- [ ] Add seasonal-naive and last-value forecasting baselines.
- [ ] Evaluate a statistical time-series model with chronological validation.
- [ ] Test whether inventory features improve out-of-sample forecasts.
- [ ] Deploy the Streamlit dashboard.

## Learning backlog — lower priority

- [ ] After the current project work, study the Requests library: `requests.get`, `params`, `timeout`, response objects, and error handling. Do not delay the current data-access tasks for this.
- [ ] After the current project work, study Python's `json` library: JSON data types, `json.load`, `json.loads`, `json.dump`, `json.dumps`, encoding, and common parsing errors. Do not delay the current project tasks for this.

## End-of-session checklist

- [ ] Update this file.
- [ ] Record important definitions or caveats in project documentation.
- [ ] Run relevant tests.
- [ ] Run Ruff.
- [ ] Review `git diff` and confirm no secrets or generated data are staged.
- [ ] Commit with a short, descriptive message.
- [ ] Push to GitHub.

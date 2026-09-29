# Project Charter

## Working title

U.S. Retail Market Pulse: Growth, Inflation, and Inventory Risk

## Audience

- Market-analysis hiring managers
- Strategy and category-management stakeholders
- Analysts who want to reproduce or challenge the result

## Decision to support

Identify U.S. retail categories that appear attractive for deeper expansion research based on market size, real growth, momentum, stability, share change, and inventory risk.

The project will create a screening tool, not a final investment recommendation. Company capabilities, margins, competitive intensity, geography, and customer fit remain outside the initial score.

## Main questions

1. Which categories are growing in nominal and inflation-adjusted terms?
2. Which categories are gaining or losing retail market share?
3. Where are inventory conditions unusually tight or elevated?
4. Do wholesale and retail inventory measures contain useful leading information?
5. How sensitive is the category ranking to metric weights and analysis periods?

## Initial scope

- Geography: United States
- Frequency: Monthly
- Starting period: 2012, subject to source validation
- Categories: Six contrasting retail categories
- Primary evidence: Official Census and BLS time series

## Deliverables

- Reproducible Python data pipeline
- Data-quality checks and data dictionary
- Reviewable analysis notebooks
- Decision-oriented figures
- Transparent category-attractiveness score
- Short market brief
- Optional Streamlit dashboard

## Success criteria

- A new user can reproduce the analysis from documented steps.
- Every reported metric has a definition, unit, period, and source.
- The recommendation is supported by several complementary measures.
- The analysis clearly separates observed facts, interpretation, and uncertainty.
- Forecasts are evaluated against simple baselines with chronological validation.
- The README communicates the business question and verified findings in under two minutes.

## Non-goals for the first version

- Claiming that aggregate category trends determine an individual company's outcome
- Causal identification of monetary policy, inflation, or inventory effects
- Store-level pricing or customer segmentation
- Deep learning
- Real-time production infrastructure


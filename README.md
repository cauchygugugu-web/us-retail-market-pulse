# U.S. Retail Market Pulse

An analysis of growth, inflation, and inventory risk across major U.S. retail categories.

## Business question

If a retailer is deciding where to expand in the United States, which categories show the strongest combination of real demand growth, market-share momentum, stability, and manageable inventory risk?

This project is designed as a portfolio-ready market analysis. It will turn official U.S. economic data into a reproducible analysis, a decision-oriented market brief, and an interactive dashboard.

## Planned analysis

1. Map market size, growth, and category share.
2. Separate nominal sales growth from inflation-adjusted growth.
3. Identify inventory accumulation and normalization signals.
4. Build a transparent category-attractiveness score.
5. Test whether inventory measures add useful predictive information.
6. Communicate the result in a concise market brief and dashboard.

## Initial category scope

- Motor vehicles and parts dealers
- Furniture and home furnishings stores
- Building material and garden equipment dealers
- Clothing and clothing accessories stores
- Food and beverage stores
- Nonstore retailers

Exact Census category codes will be verified against the source metadata before they are used in analysis.

## Data sources

- [U.S. Census Bureau Monthly Retail Trade and Food Services](https://www.census.gov/retail/)
- [U.S. Census Bureau Monthly Wholesale Trade](https://www.census.gov/wholesale/)
- [U.S. Bureau of Labor Statistics Consumer Price Index](https://www.bls.gov/cpi/data.htm)
- Optional macro context from [FRED](https://fred.stlouisfed.org/)

Source endpoints and documentation links are recorded in [`config/sources.json`](config/sources.json).

## Repository structure

```text
config/                  Source registry and analysis configuration
data/raw/                Immutable source extracts (not committed)
data/interim/            Cleaned intermediate data (not committed)
data/processed/          Analysis-ready data (not committed)
docs/                    Project charter, methodology, and data dictionary
notebooks/               Reviewable analysis notebooks
reports/figures/         Exported portfolio figures
src/                     Reusable Python package
tests/                   Automated tests
PROJECT_GUIDE.zh-CN.md   Chinese learning and continuity guide
TASKS.md                 Milestones and the next smallest action
LEARNING_LOG.md          Learning notes and decision log
```

## Local setup

Python 3.11 or newer is recommended.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[analysis,dev]"
Copy-Item .env.example .env
```

Request a Census API key, place it in `.env`, and never commit `.env`.

## Current status

The repository scaffold and first notebook outline are ready. No analytical findings have been claimed yet. The next task is to inspect the Census MRTS metadata and confirm the exact series and category codes needed for the market map.

See [`TASKS.md`](TASKS.md) for the active milestone and [`PROJECT_GUIDE.zh-CN.md`](PROJECT_GUIDE.zh-CN.md) for the learning path.

## Reproducibility principles

- Official sources are preferred over republished datasets.
- Raw extracts remain unchanged after download.
- Transformations live in `src/`, not only in notebooks.
- Time-series evaluation preserves chronological order.
- Nominal and inflation-adjusted measures are labeled explicitly.
- Predictive relationships are not presented as causal effects.
- Every portfolio claim must be traceable to a source and reproducible output.


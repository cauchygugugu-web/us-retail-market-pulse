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

Exact endpoints, series identifiers, units, and adjustment flags will be recorded only after
they are verified against the official source metadata.

## Repository structure

```text
src/us_retail_market_pulse/  Reusable Python package
tests/                       Automated tests
data/raw/                    Immutable source extracts (local only)
data/processed/              Analysis-ready data (local only)
notebooks/                   Reviewable analysis notebooks
reports/figures/             Exported portfolio figures
pyproject.toml               Project metadata, dependencies, and tool configuration
TASKS.md                     Milestones and the next smallest action
AGENTS.md                    Continuity instructions for future Codex chats
```

## Local setup

Python 3.11 or newer is recommended.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Copy `.env.example` to a local `.env` file and add the Census API key there. API keys must never
be committed.

## Current status

The project foundation and Census MRTS source definitions are ready. The request, parsing, and
validation helpers have offline tests. A bounded 2024 sample for category `441` has been downloaded,
preserved unchanged in `data/raw/`, and validated for structure, monthly continuity, values,
category, geography, and seasonal-adjustment status. No analytical findings have been claimed.

The next task is to add an offline-tested, reusable raw-extract save function that writes key-free
metadata and refuses to overwrite existing files. After that, the Census download can be expanded
to the six target categories and the retail-total denominator for a documented analysis period.
See [`TASKS.md`](TASKS.md) for the detailed checklist and [`AGENTS.md`](AGENTS.md) for continuity
instructions.

## Reproducibility principles

- Official sources are preferred over republished datasets.
- Raw extracts remain unchanged after download.
- Transformations live in `src/`, not only in notebooks.
- Time-series evaluation preserves chronological order.
- Nominal and inflation-adjusted measures are labeled explicitly.
- Predictive relationships are not presented as causal effects.
- Every portfolio claim must be traceable to a source and reproducible output.

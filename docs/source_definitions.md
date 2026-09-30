# Census MRTS Source Definitions

## Dataset

- Program: Monthly Retail Trade and Food Services
- Program code: `MRTS`
- API endpoint: `https://api.census.gov/data/timeseries/eits/mrts`
- Frequency: Monthly
- Geographic coverage: U.S. total

This project uses the full Monthly Retail Trade and Food Services dataset (`mrts`), not the advance-release dataset (`marts`).

## Sales measure

| Property | Verified value |
|---|---|
| Data type code | `SM` |
| Description | Sales - Monthly |
| Value field | `cell_value` |
| Unit | `MLN$` — millions of U.S. dollars |
| Category field | `category_code` |
| Time filter | `time` |
| Month identifier | `time_slot_id` |
| Seasonal-adjustment field | `seasonally_adj` |
| Available adjustment values | `yes` and `no` |
| Price basis | Nominal — not inflation-adjusted |

## Retail categories

| Analysis category | Census category code |
|---|---|
| Motor Vehicle and Parts Dealers | `441` |
| Furniture and Home Furnishings Stores | `442` |
| Building Material and Garden Equipment and Supplies Dealers | `444` |
| Clothing and Clothing Accessories Stores | `448` |
| Food and Beverage Stores | `445` |
| Nonstore Retailers | `454` |

## Market-share denominator

Use `44000` — Retail Trade — as the denominator for retail-category market share.

Do not use `44X72` because it includes Food Services and Drinking Places in addition to retail trade. Food and Beverage Stores (`445`) are retail stores and are different from restaurants and drinking places (`722`).

All market-share calculations must use numerator and denominator series with compatible units and the same seasonal-adjustment status.

The six selected categories do not exhaust Retail Trade, so their market shares are not expected to sum to 100%.

## Revision status

MRTS estimates are revisable. Annual revisions may include historical corrections, benchmarking to annual survey results, and updates to seasonal-adjustment models.

The extraction metadata should record the source URL and extraction timestamp so that results can be reproduced against a known data release.

Beginning with the 2025 benchmark release, the MRTS time series was restated to the 2017 NAICS classification. Nonemployer firms were removed from the historical series, so the current estimates represent employer firms.

## Official references

- Census API variables: <https://api.census.gov/data/timeseries/eits/mrts/variables.html>
- MRTS machine-readable package (MRTS-mf.zip): <https://www.census.gov/econ_datasets/>
- MRTS survey description: <https://www.census.gov/retail/mrts/about_the_surveys.html>
- MRTS methodology: <https://www.census.gov/retail/mrts/how_surveys_are_collected.html>
- Annual revision reports: <https://www.census.gov/retail/mrts/historic_releases.html>
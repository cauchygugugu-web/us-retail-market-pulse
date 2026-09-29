# Data Dictionary

This file starts as a source-planning table. Replace `To verify` values only after checking official metadata.

| Analytical field | Meaning | Frequency | Unit | Adjustment | Source | Status |
|---|---|---:|---|---|---|---|
| `date` | Reference month | Monthly | Date | N/A | Census/BLS | To verify |
| `category_code` | Official source category identifier | Monthly | Code | N/A | Census | To verify |
| `category_name` | Human-readable retail category | Monthly | Text | N/A | Census | To verify |
| `sales_nominal` | Retail sales | Monthly | USD millions expected | To verify | Census MRTS | To verify |
| `inventory_nominal` | End-of-month retail inventory | Monthly | USD millions expected | To verify | Census MRTS | To verify |
| `inventory_sales_ratio` | Inventory divided by sales | Monthly | Ratio | To verify | Census MRTS | To verify |
| `cpi_index` | Consumer price index mapped to a category | Monthly | Index | To verify | BLS | To verify |
| `sales_real_index` | Approximate inflation-adjusted sales index | Monthly | Index | Derived | Project | Planned |
| `sales_yoy_pct` | Twelve-month nominal sales growth | Monthly | Percent | Derived | Project | Planned |
| `market_share_pct` | Category share of compatible retail total | Monthly | Percent | Derived | Project | Planned |

## Required source metadata

Every raw extract should preserve or record:

- source organization and program;
- endpoint or download URL;
- request parameters or series IDs;
- extraction timestamp;
- reference period;
- unit and scale;
- seasonal-adjustment status;
- preliminary or revised status when available;
- source notes relevant to comparability.


# Methodology Notes

This document will evolve with the analysis. A method is not considered final until its inputs, formula, interpretation, and limitations are documented here.

## Planned measures

### Year-over-year growth

For a monthly series \(x_t\):

```text
YoY growth = (x_t / x_(t-12) - 1) * 100
```

This controls for recurring seasonal patterns better than a raw month-over-month comparison, but it can still be distorted by unusual base periods.

### Market share

```text
Category share = category sales / retail-and-food-services total sales
```

The numerator and denominator must use compatible adjustment status, units, and dates.

### Approximate real sales

```text
Real sales index = nominal sales index / price index * 100
```

This is an analytical approximation. Census retail categories and BLS CPI item categories do not necessarily align exactly. Every crosswalk choice must be documented and tested for sensitivity.

### Inventory risk

Candidate measures include the inventory-to-sales ratio, its historical percentile, and a rolling z-score. Elevated inventory is not automatically negative: interpretation depends on expected demand, supply constraints, and category characteristics.

### Category-attractiveness score

The score will combine growth, momentum, stability, share change, and inventory risk. Component definitions, directions, normalization, weights, and sensitivity checks will be documented before a ranking is presented.

## Time-series validation

- Preserve chronological ordering.
- Compare every model with a simple baseline.
- Fit transformations using training data only.
- Use rolling or expanding windows.
- Do not use revised future observations as though they were known historically without documenting the limitation.

## Interpretation boundary

Regression coefficients and lead/lag tests will be described as associations or predictive relationships unless a credible causal design is established.


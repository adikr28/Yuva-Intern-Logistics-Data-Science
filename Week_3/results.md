# Week 3 – Numerical Results and Interpretation

> These results come from a hypothetical, reproducible logistics dataset simulated for the YuvaIntern Week 3 task. They are demonstration results, not real-company measurements.

## Overall KPIs

| Metric | Result |
|---|---:|
| Shipments | 12,000 |
| Late shipment rate | 34.65% |
| On-time rate | 65.35% |
| Average delivery time | 6.74 days |
| Median delivery time | 6.40 days |
| Average transportation cost | 1,837.71 |

### Interpretation
The simulated network delivers 65.35% of shipments on time, leaving a 34.65% late rate. Mean delivery time is 0.34 days above the median, indicating a moderately right-skewed distribution with slower shipments pulling the average upward.

## What the analysis demonstrates

- Transport modes have different delivery-time, cost, and reliability profiles.
- Regional late rates can differ materially, making regional segmentation more useful than a single global KPI.
- Distance and shipment characteristics can be screened as cost drivers using correlation before moving to regression.
- Visualizations reveal distribution shape and segment differences that a single average cannot show.

## Business implication
A logistics manager should evaluate mode selection using a combination of speed, cost, and reliability. Regions with higher late rates should be investigated for carrier performance, route density, depot capacity, and last-mile constraints before operational changes are made.

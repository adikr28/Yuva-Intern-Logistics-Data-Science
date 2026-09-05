# Week 3 – Numerical Results and Interpretation

> These results come from a hypothetical, reproducible logistics dataset simulated for the YuvaIntern Week 3 task. They are demonstration results, not real-company measurements.

## Overall KPIs

| Metric | Result |
|---|---:|
| Shipments | 12,000 |
| Late shipment rate | 34.65% |
| On-time rate | 65.35% |
| Average delivery time | 6.74 days |
| Median delivery time | 6.49 days |
| Average transportation cost | 1,837.71 simulated currency units |
| Distance vs cost correlation | 0.78 |
| Volume vs cost correlation | -0.08 |
| Delivery time vs satisfaction correlation | -0.57 |

## Interpretation
The simulated network delivers 65.35% of shipments on time, leaving a 34.65% late rate. Mean delivery time is 0.25 days above the median, indicating a modest right-skew caused by slower shipments.

Distance has the strongest listed relationship with transport cost (r = 0.78), while shipment volume has a weak negative correlation in this particular simulation (r = -0.08). This illustrates why analysts should test relationships empirically rather than assume that every operational variable will have a strong positive correlation.

Delivery time and customer satisfaction have a negative correlation of -0.57 in the simulation. This connects an operational service metric with customer experience, although correlation alone does not establish causation.

## What the analysis demonstrates

- Transport modes have different delivery-time, cost, and reliability profiles.
- Regional late rates can differ materially, making regional segmentation more useful than a single global KPI.
- Distance can be screened as a cost driver using correlation before moving to regression.
- Delivery-time distributions reveal information that a single average can hide.
- Customer-impact analysis can connect operational performance to satisfaction.
- Visualizations make segment differences and relationships easier to communicate to decision-makers.

## Business implication
A logistics manager should evaluate mode selection using a combination of speed, cost, and reliability. Regions with higher late rates should be investigated for carrier performance, route density, depot capacity, and last-mile constraints before operational changes are made.

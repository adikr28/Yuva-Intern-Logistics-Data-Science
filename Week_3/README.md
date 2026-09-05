# Week 3 – Advanced Data Analysis and Visualization

## Objective
Explore and visualize a hypothetical logistics dataset using Python, calculate descriptive statistics and logistics KPIs, identify cost drivers and regional/transport bottlenecks, and translate the findings into operational recommendations.

## Dataset
A reproducible hypothetical dataset of **12,000 shipments** was simulated with random seed **42**. Variables include region, transport mode, shipment volume, distance, transport cost, delivery time, estimated delivery time, late flag, fuel cost, and customer satisfaction.

Because YuvaIntern explicitly allows a hypothetical dataset, the numerical findings in this week are **simulation results, not real-company logistics measurements**.

## Evidence Snapshot
- Shipments simulated: **12,000**
- Overall late-shipment rate: **34.65%**
- Overall on-time rate: **65.35%**
- Average delivery time: **6.74 days**
- Median delivery time: **6.40 days**
- Average transportation cost: **1,837.71** simulated currency units

See `results.md` for the detailed mode/region tables and interpretations.

## Analysis Covered
1. Central tendency and dispersion
2. Delivery-time distribution
3. Transport-mode comparison
4. Transportation-cost analysis
5. Regional late-shipment analysis
6. Correlation analysis
7. Evidence-based recommendations

## Files
- `analysis.py` – reproducible Python script that generates the dataset, calculations, and charts.
- `results.md` – numerical evidence and interpretation.
- `charts/` – visualization outputs when generated locally.

## Reproducibility
Run:

```bash
pip install -r ../requirements.txt
python analysis.py
```

The fixed random seed ensures the same simulated dataset and results are reproduced.

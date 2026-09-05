# Week 3 – Advanced Data Analysis and Visualization

## Scope
Evidence-based exploratory data analysis and visualization using a reproducible **simulated logistics dataset**, as permitted by the YuvaIntern task.

## Dataset
- 12,000 shipment records
- Five regions: North, South, East, West, Central
- Four transport modes: Road, Rail, Air, Sea
- Fixed random seed: 42 for reproducibility

Because the task explicitly permits a hypothetical dataset, the numerical findings below are **simulation results, not real-company measurements**.

## Key Results
- Shipments analyzed: **12,000**
- Late-delivery rate: **34.65%**
- On-time rate: **65.35%**
- Average delivery time: **6.74 days**
- Median delivery time: **6.49 days**
- Average transport cost: **1,837.71 simulated currency units**
- Distance vs transport-cost correlation: **0.78**
- Shipment-volume vs transport-cost correlation: **-0.08**
- Delivery-time vs customer-satisfaction correlation: **-0.57**

## Analysis Covered
1. Central tendency and dispersion
2. Delivery-time distribution
3. Transport-mode comparison
4. Transportation-cost analysis
5. Regional late-shipment analysis
6. Correlation analysis
7. Delivery time vs customer satisfaction
8. Evidence-based recommendations

## Files
- `analysis.py` – reproducible Python script that generates the dataset, calculations, and charts.
- `results.md` – numerical evidence and interpretation.
- `week3_logistics_simulated_data.csv` – simulated dataset used for the analysis.
- `charts/` – visualization outputs when generated locally.

## Reproducibility
Run:

```bash
pip install -r ../requirements.txt
python analysis.py
```

The fixed random seed ensures the same simulated dataset and results are reproduced.

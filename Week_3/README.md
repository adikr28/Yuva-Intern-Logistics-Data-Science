# YuvaIntern – Week 3: Advanced Data Analysis and Visualization in Logistics

## Overview

This project demonstrates exploratory data analysis (EDA) and visualization for a simulated logistics operation using Python.

The Week 3 task focuses on:
- Data simulation
- Exploratory data analysis
- Central tendency and descriptive statistics
- Correlation analysis
- Logistics performance visualization
- Operational insights and recommendations

> **Data note:** The dataset is simulated/hypothetical, as permitted by the Week 3 task. The numerical results are demonstrations of analytical technique and are not real company performance.

## Dataset

- 12,000 shipment records
- 5 regions: North, South, East, West, Central
- 4 transport modes: Road, Rail, Air, Sea
- Delivery time
- Estimated delivery time
- Late-delivery flag
- Shipment volume
- Distance
- Transportation cost
- Fuel cost
- Customer satisfaction

## Key Results

- Late-delivery rate: **34.65%**
- On-time rate: **65.35%**
- Average delivery time: **6.74 days**
- Median delivery time: **6.49 days**
- Average transport cost: **1,837.71**
- Distance vs transport cost correlation: **0.78**
- Shipment volume vs transport cost correlation: **-0.08**
- Delivery time vs customer satisfaction correlation: **-0.57**

## Visualizations

1. Delivery-time distribution
2. Average delivery time by transport mode
3. Transportation cost vs distance
4. Late shipment rate by region
5. Delivery time vs customer satisfaction

## Files

- `Week_3_Logistics_Analysis_Report.docx` – complete internship report
- `week3_logistics_analysis.py` – reproducible Python analysis
- `week3_logistics_simulated_data.csv` – simulated dataset
- `charts/` – generated visualization outputs

## How to Run

Install the required libraries:

```bash
pip install pandas matplotlib
```

Then run:

```bash
python week3_logistics_analysis.py
```

The script prints KPI, descriptive-statistics, correlation, mode, and regional results and regenerates the five charts.

## Main Analytical Takeaway

The analysis demonstrates why logistics decisions should not rely on a single KPI. Delivery reliability, delivery-time distribution, transport mode, distance, regional performance, cost, and customer satisfaction should be considered together.

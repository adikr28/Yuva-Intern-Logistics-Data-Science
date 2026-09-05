# YuvaIntern – Week 4: Predictive Modeling and Optimization in Logistics

## Objective

This project builds and evaluates predictive models to forecast **delivery time in days** for a simulated logistics operation, then converts the model findings into an operational optimization strategy.

> **Data note:** The dataset is simulated/hypothetical, as permitted by the Week 4 task. The model results are demonstrations of the predictive workflow and are not real company performance.

## Dataset

- 12,000 shipment records
- Target: `delivery_time_days`
- Features: shipment volume, distance, transport mode, region, fuel cost, estimated delivery days
- Train/test split: 80% / 20%
- Random state: 42

## Models

1. Linear Regression — baseline
2. Decision Tree Regressor — non-linear benchmark
3. Random Forest Regressor — ensemble model

## Test-set results

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 0.8436 | 1.0705 | 0.7600 |
| Random Forest | 0.8681 | 1.0975 | 0.7477 |
| Decision Tree | 0.9111 | 1.1548 | 0.7206 |

**Best model: Linear Regression**

## 5-fold cross-validation

- MAE: **0.8440 ± 0.0164 days**
- RMSE: **1.0700 ± 0.0201 days**
- R²: **0.7575 ± 0.0136**

## Optimization Strategy

The model is used as an early-warning layer. Shipments in the top 25% of predicted delivery times are flagged for proactive review. The 75th-percentile threshold in this run is **7.87 days**, flagging **25%** of the test set by construction.

Recommended actions include route review, transport-mode review, capacity/carrier review, proactive customer communication, and re-scoring when new operational information becomes available. These are prioritization strategies and should be validated with real historical outcomes before deployment.

## Feature importance

Permutation importance for the selected model ranked the main predictors as:

1. `estimated_delivery_days`
2. `distance_km`
3. `transport_mode`
4. `region`
5. `fuel_cost`
6. `shipment_volume_kg`

Feature importance indicates predictive usefulness, not causation.

## Files

- `README.md` – project overview and results
- `week4_logistics_prediction.py` – reproducible Python implementation
- `week4_model_results.csv` – model metrics
- `week4_feature_importance.csv` – permutation importance
- `Week_4_Predictive_Modeling_Report.docx` – complete internship report (upload this binary file manually if it is not yet in the repository)
- `charts/` – generated visualizations (upload the PNG files manually if needed)

## Run

```bash
pip install pandas numpy matplotlib scikit-learn
python week4_logistics_prediction.py
```

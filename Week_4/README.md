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

## Evaluation

The models are evaluated using:
- MAE
- RMSE
- R²

The best model is additionally evaluated with 5-fold cross-validation.

### Test-set results

            Model      MAE     RMSE       R2
Linear Regression 0.843634 1.070486 0.759952
    Random Forest 0.868149 1.097481 0.747692
    Decision Tree 0.911089 1.154825 0.720637

### Best model

**Linear Regression**

5-fold cross-validation:
- MAE: **0.8440 ± 0.0164 days**
- RMSE: **1.0700 ± 0.0201 days**
- R²: **0.7575 ± 0.0136**

## Optimization Strategy

The model can be used as an early-warning layer. Shipments whose predicted delivery time falls in the top 25% of predictions are flagged as high risk. In the test set, this represents **25.00%** of shipments by construction.

Recommended actions for flagged shipments:
1. Review route and distance before dispatch.
2. Check whether a different transport mode can meet the service requirement.
3. Prioritize high-risk shipments for capacity/carrier review.
4. Use predicted delivery time to communicate realistic expectations.
5. Re-score shipments as operational information changes.

This is a prioritization strategy, not proof that changing a route will reduce delivery time. Any operational intervention should be tested against real historical outcomes.

## Key Findings

- The model comparison identifies **Linear Regression** as the strongest test-set model by RMSE.
- The strongest predictive features are shown in `charts/feature_importance.png`.
- The actual-vs-predicted chart shows how closely the selected model tracks delivery time.
- Residual analysis is included to identify systematic prediction errors.
- Cross-validation is included to test whether performance is stable across different data splits.

## Files

- `Week_4_Predictive_Modeling_Report.docx` – final internship report
- `week4_logistics_prediction.py` – reproducible Python implementation
- `week3_logistics_simulated_data.csv` – source simulated dataset
- `week4_model_results.csv` – model metrics
- `week4_predictions.csv` – held-out predictions
- `week4_feature_importance.csv` – permutation importance
- `charts/` – four visualization outputs

## Run

```bash
pip install pandas numpy matplotlib scikit-learn
python week4_logistics_prediction.py
```

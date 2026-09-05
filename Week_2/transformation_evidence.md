# Week 2 – Transformation Evidence Plan

The Week 2 submission was evaluated at **58/100** with feedback that it was thorough and well-structured but needed **more concrete examples and numbers**, plus specific explanations of **how each transformation affects subsequent analysis**.

This document maps each preprocessing step to a measurable validation and its downstream impact. The numerical values below are intentionally left to the actual dataset run rather than being invented.

| Transformation | Evidence to record | Why it matters downstream |
|---|---|---|
| Missing-value profiling | Missing count and percentage by column | Shows whether dropping/imputation can bias the sample |
| Duplicate checks | Exact duplicate count + key-duplicate count | Prevents inflated order counts and KPI denominators |
| Timestamp parsing | Number of parse failures | Prevents invalid delivery-duration calculations |
| Timestamp chronology | Count of rows violating expected event order | Prevents negative/impossible process durations |
| Delivered-order filter | Delivered rows before/after filtering | Defines the valid population for delivery KPIs |
| IQR outlier detection | Q1, Q3, IQR, lower/upper bounds, outlier count | Shows how extreme observations could influence means/models |
| Categorical cleaning | Number of unique categories before/after normalization | Prevents artificial categories caused by whitespace/case differences |
| Feature engineering | Sample calculations for delivery_days and delay_days | Converts raw timestamps into business KPIs |
| Scaling | Mean/std before and after StandardScaler | Demonstrates equalization of feature scale for distance-based models |
| Train/test preprocessing | Training rows, test rows, fitted-transform logic | Prevents test-set information leaking into model training |

## Concrete example: missing values

```python
missing_report = (
    df.isna().sum()
      .to_frame("missing_count")
)
missing_report["missing_percent"] = (
    missing_report["missing_count"] / len(df) * 100
)
```

**Downstream effect:** if a delivery timestamp is missing because an order was cancelled, imputing it would create a false delivery event and distort average delivery time. Such records should normally be excluded from delivery-time calculations rather than filled with an arbitrary date.

## Concrete example: outliers

```python
q1 = df["delivery_days"].quantile(0.25)
q3 = df["delivery_days"].quantile(0.75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr

outlier_count = (df["delivery_days"] > upper).sum()
```

**Downstream effect:** removing genuine long deliveries may reduce the reported mean but can hide the operational failures the project is designed to detect. Therefore, the project will compare KPI results before and after any justified treatment.

## Concrete example: scaling

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
```

**Downstream effect:** a feature such as order value may have a much larger numeric range than seller count. Without scaling, K-Means distance calculations can be dominated by the larger-scale feature. Standardization makes the contribution of each feature comparable in the clustering step.

## Week 2 run requirement

The next execution step is to download the Olist files, run the preprocessing code, capture the actual counts/percentages, and add a before-vs-after validation table to the Week 2 notebook and report.

"""
YuvaIntern Week 4 — Predictive Modeling and Optimization in Logistics

Run this script from the Week_4 folder:
    pip install pandas numpy matplotlib scikit-learn
    python week4_logistics_prediction.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.inspection import permutation_importance

df = pd.read_csv("week3_logistics_simulated_data.csv")

target = "delivery_time_days"
features = [
    "shipment_volume_kg", "distance_km", "transport_mode",
    "region", "fuel_cost", "estimated_delivery_days"
]

X = df[features]
y = df[target]

num_features = ["shipment_volume_kg", "distance_km", "fuel_cost", "estimated_delivery_days"]
cat_features = ["transport_mode", "region"]

preprocess = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), num_features),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), cat_features)
])

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(max_depth=8, min_samples_leaf=10, random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=250, max_depth=12, min_samples_leaf=3, random_state=42, n_jobs=-1
    ),
}

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

results = []
fitted = {}

for name, model in models.items():
    pipe = Pipeline([("prep", preprocess), ("model", model)])
    pipe.fit(X_train, y_train)
    pred = pipe.predict(X_test)
    fitted[name] = pipe
    results.append({
        "Model": name,
        "MAE": mean_absolute_error(y_test, pred),
        "RMSE": np.sqrt(mean_squared_error(y_test, pred)),
        "R2": r2_score(y_test, pred),
    })

results_df = pd.DataFrame(results).sort_values("RMSE")
print("\nMODEL COMPARISON\n")
print(results_df.to_string(index=False))

best_name = results_df.iloc[0]["Model"]
best_model = fitted[best_name]
best_pred = best_model.predict(X_test)

kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_mae = -cross_val_score(best_model, X, y, cv=kf, scoring="neg_mean_absolute_error", n_jobs=-1)
cv_rmse = np.sqrt(-cross_val_score(best_model, X, y, cv=kf, scoring="neg_mean_squared_error", n_jobs=-1))
cv_r2 = cross_val_score(best_model, X, y, cv=kf, scoring="r2", n_jobs=-1)

print("\n5-FOLD CROSS-VALIDATION FOR BEST MODEL")
print(f"MAE:  {cv_mae.mean():.4f} ± {cv_mae.std():.4f}")
print(f"RMSE: {cv_rmse.mean():.4f} ± {cv_rmse.std():.4f}")
print(f"R2:   {cv_r2.mean():.4f} ± {cv_r2.std():.4f}")

perm = permutation_importance(
    best_model, X_test, y_test, n_repeats=5, random_state=42, n_jobs=-1
)
importance = pd.DataFrame({
    "Feature": X_test.columns,
    "Importance": perm.importances_mean
}).sort_values("Importance", ascending=False)

print("\nFEATURE IMPORTANCE")
print(importance.to_string(index=False))

# A simple predictive-risk rule for operational prioritization.
predictions = pd.DataFrame(index=X_test.index)
predictions["actual_delivery_days"] = y_test
predictions["predicted_delivery_days"] = best_pred
threshold = predictions["predicted_delivery_days"].quantile(0.75)
predictions["high_risk_flag"] = predictions["predicted_delivery_days"] >= threshold

print(f"\nHigh-risk threshold (75th percentile): {threshold:.2f} days")
print(f"High-risk shipments: {predictions['high_risk_flag'].mean()*100:.2f}%")

# Reproduce core visualization.
plt.figure(figsize=(7,6))
plt.scatter(y_test, best_pred, s=10, alpha=0.35)
mn, mx = min(y_test.min(), best_pred.min()), max(y_test.max(), best_pred.max())
plt.plot([mn, mx], [mn, mx], linestyle="--")
plt.xlabel("Actual delivery time (days)")
plt.ylabel("Predicted delivery time (days)")
plt.title(f"Actual vs Predicted Delivery Time — {best_name}")
plt.tight_layout()
plt.savefig("actual_vs_predicted.png", dpi=180)
plt.show()

"""
YuvaIntern - Week 3
Advanced Data Analysis and Visualization in Logistics

Reproducible analysis for the simulated logistics dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA = "week3_logistics_simulated_data.csv"

df = pd.read_csv(DATA)

# -----------------------------
# Data-quality checks
# -----------------------------
print("Shape:", df.shape)
print("Missing values:", df.isna().sum().sum())
print("Duplicate shipment IDs:", df["shipment_id"].duplicated().sum())

# -----------------------------
# KPI calculations
# -----------------------------
late_rate = df["late_flag"].mean() * 100
on_time_rate = 100 - late_rate
avg_delivery = df["delivery_time_days"].mean()
median_delivery = df["delivery_time_days"].median()
avg_cost = df["transport_cost"].mean()
total_cost = df["transport_cost"].sum()

print("\nKPI RESULTS")
print(f"Late-delivery rate: {late_rate:.2f}%")
print(f"On-time rate: {on_time_rate:.2f}%")
print(f"Average delivery time: {avg_delivery:.2f} days")
print(f"Median delivery time: {median_delivery:.2f} days")
print(f"Average transport cost: {avg_cost:.2f}")
print(f"Total transport cost: {total_cost:.2f}")

# -----------------------------
# Descriptive statistics
# -----------------------------
continuous = [
    "delivery_time_days",
    "transport_cost",
    "distance_km",
    "shipment_volume_kg",
]
print("\nDESCRIPTIVE STATISTICS")
print(df[continuous].describe().T[["min", "max", "mean", "50%", "std"]])

# -----------------------------
# Correlation analysis
# -----------------------------
corr_cols = [
    "shipment_volume_kg",
    "distance_km",
    "transport_cost",
    "delivery_time_days",
    "fuel_cost",
    "customer_satisfaction",
]
corr = df[corr_cols].corr()

print("\nCORRELATIONS")
print("Distance vs cost:", round(corr.loc["distance_km", "transport_cost"], 2))
print("Volume vs cost:", round(corr.loc["shipment_volume_kg", "transport_cost"], 2))
print(
    "Delivery time vs satisfaction:",
    round(corr.loc["delivery_time_days", "customer_satisfaction"], 2),
)

# -----------------------------
# Segment analysis
# -----------------------------
mode_summary = df.groupby("transport_mode").agg(
    shipments=("shipment_id", "count"),
    avg_delivery_days=("delivery_time_days", "mean"),
    avg_cost=("transport_cost", "mean"),
    late_rate=("late_flag", "mean"),
)
mode_summary["late_rate"] *= 100

region_summary = df.groupby("region").agg(
    shipments=("shipment_id", "count"),
    avg_delivery_days=("delivery_time_days", "mean"),
    avg_cost=("transport_cost", "mean"),
    late_rate=("late_flag", "mean"),
)
region_summary["late_rate"] *= 100

print("\nMODE SUMMARY")
print(mode_summary)

print("\nREGION SUMMARY")
print(region_summary.sort_values("late_rate", ascending=False))

# -----------------------------
# Visualizations
# -----------------------------
charts = "charts"

plt.figure(figsize=(8, 5))
plt.hist(df["delivery_time_days"], bins=35)
plt.axvline(avg_delivery, linestyle="--", label=f"Mean {avg_delivery:.2f}")
plt.axvline(
    median_delivery,
    linestyle=":",
    label=f"Median {median_delivery:.2f}",
)
plt.xlabel("Delivery time (days)")
plt.ylabel("Shipments")
plt.title("Distribution of Delivery Time")
plt.legend()
plt.tight_layout()
plt.savefig(f"{charts}/delivery_time_distribution.png", dpi=180)
plt.close()

plt.figure(figsize=(8, 5))
mode_summary["avg_delivery_days"].sort_values().plot(kind="bar")
plt.ylabel("Average delivery time (days)")
plt.title("Average Delivery Time by Transport Mode")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{charts}/delivery_by_mode.png", dpi=180)
plt.close()

sample = df.sample(2500, random_state=42)
plt.figure(figsize=(8, 5))
plt.scatter(
    sample["distance_km"],
    sample["transport_cost"],
    s=8,
    alpha=0.35,
)
plt.xlabel("Distance (km)")
plt.ylabel("Transportation cost")
plt.title("Transportation Cost vs Distance")
plt.tight_layout()
plt.savefig(f"{charts}/cost_vs_distance.png", dpi=180)
plt.close()

plt.figure(figsize=(8, 5))
region_summary["late_rate"].sort_values().plot(kind="barh")
plt.xlabel("Late shipment rate (%)")
plt.title("Late Shipment Rate by Region")
plt.tight_layout()
plt.savefig(f"{charts}/late_rate_region.png", dpi=180)
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(
    df["delivery_time_days"],
    df["customer_satisfaction"],
    s=8,
    alpha=0.25,
)
plt.xlabel("Delivery time (days)")
plt.ylabel("Customer satisfaction (1–5)")
plt.title("Delivery Time vs Customer Satisfaction")
plt.tight_layout()
plt.savefig(f"{charts}/delivery_vs_satisfaction.png", dpi=180)
plt.close()

print("\nAnalysis complete. Charts saved in:", charts)

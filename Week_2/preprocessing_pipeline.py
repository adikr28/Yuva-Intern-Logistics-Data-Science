"""YuvaIntern Week 2 - Logistics data collection and preprocessing example.

The script demonstrates the proposed preprocessing workflow. It expects the
Olist CSV files to be downloaded locally under data/raw/.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

ORDERS_PATH = "data/raw/olist_orders_dataset.csv"
ITEMS_PATH = "data/raw/olist_order_items_dataset.csv"

orders = pd.read_csv(ORDERS_PATH)
items = pd.read_csv(ITEMS_PATH)

# 1. Basic quality checks
print("Orders shape:", orders.shape)
print("Missing values:\n", orders.isna().sum().sort_values(ascending=False))
print("Exact duplicate rows:", orders.duplicated().sum())

# 2. Parse lifecycle timestamps
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# 3. Remove exact duplicates; preserve legitimate item-level repetition
orders = orders.drop_duplicates()
assert orders["order_id"].is_unique

# 4. Aggregate item-level data to order grain
order_items = (
    items.groupby("order_id")
    .agg(
        item_count=("order_item_id", "count"),
        order_value=("price", "sum"),
        freight_value=("freight_value", "sum"),
        seller_count=("seller_id", "nunique"),
    )
    .reset_index()
)

# 5. Join without multiplying order-level rows
df = orders.merge(order_items, on="order_id", how="left")

# 6. Feature engineering
df["delivery_days"] = (
    df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
).dt.total_seconds() / 86400

df["delay_days"] = (
    df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

df["late_flag"] = (df["delay_days"] > 0).astype("int8")

# 7. Keep delivered orders for delivery-time modeling
model_df = df[df["order_delivered_customer_date"].notna()].copy()

numeric_features = ["item_count", "order_value", "freight_value", "seller_count"]
X = model_df[numeric_features]
y = model_df["delivery_days"]

# 8. Split before fitting preprocessing objects to avoid leakage
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

preprocess = ColumnTransformer(
    transformers=[
        (
            "num",
            Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            ),
            numeric_features,
        )
    ]
)

X_train_ready = preprocess.fit_transform(X_train)
X_test_ready = preprocess.transform(X_test)

print("Training matrix:", X_train_ready.shape)
print("Testing matrix:", X_test_ready.shape)

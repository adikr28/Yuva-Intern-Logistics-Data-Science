"""Week 1 starter script: load and prepare Olist order-level data."""

import pandas as pd


def build_order_summary(data_dir: str = "data") -> pd.DataFrame:
    """Create an order-level table from Olist order and item data."""
    orders = pd.read_csv(f"{data_dir}/olist_orders_dataset.csv")
    items = pd.read_csv(f"{data_dir}/olist_order_items_dataset.csv")

    order_summary = (
        items.groupby("order_id")
        .agg(
            item_count=("order_item_id", "count"),
            order_value=("price", "sum"),
            freight_value=("freight_value", "sum"),
            seller_count=("seller_id", "nunique"),
        )
        .reset_index()
    )

    df = orders.merge(order_summary, on="order_id", how="left")

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]
    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    df["delivery_days"] = (
        df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
    ).dt.total_seconds() / 86400

    df["delivery_delay_days"] = (
        df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
    ).dt.total_seconds() / 86400

    df["late_flag"] = (df["delivery_delay_days"] > 0).astype("Int64")

    return df


if __name__ == "__main__":
    analysis_df = build_order_summary()
    print(analysis_df.head())
    print("Rows:", len(analysis_df))

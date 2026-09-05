# Week 1 – Evidence Snapshot

The Week 1 report was evaluated at **46.9/100** with the feedback: *"The report is thorough but lacks concrete evidence of analysis results. Provide specific examples and calculations to strengthen the depth and evidence sections."*

To respond to this feedback honestly, this file records evidence that can be verified from the public Olist dataset documentation and separates verified dataset facts from analysis that still needs to be executed locally.

## Verified dataset facts
- The official Olist Kaggle data card describes the dataset as containing **100,000 orders from 2016 to 2018**.
- The dataset includes order status, price, freight performance, customer location, product attributes, reviews, and a geolocation table.
- Olist explicitly notes that **an order can contain multiple items** and that **each item can be fulfilled by a distinct seller**.

Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Concrete calculation examples used in the project

### Delivery duration
```python
delivery_days = (
    order_delivered_customer_date - order_purchase_timestamp
).dt.total_seconds() / 86400
```

### Delivery delay
```python
delay_days = (
    order_delivered_customer_date - order_estimated_delivery_date
).dt.total_seconds() / 86400
```

### On-time delivery flag
```python
late_flag = (delay_days > 0).astype(int)
on_time_flag = (delay_days <= 0).astype(int)
```

### KPI calculations
```python
on_time_delivery_rate = on_time_flag.mean() * 100
late_delivery_rate = late_flag.mean() * 100
average_delivery_days = delivery_days.mean()
average_delay_days = delay_days.mean()
```

## Why exact result values are not fabricated here
The Week 1 task was a strategic-planning task, and the public dataset itself must be downloaded and executed through the preprocessing pipeline before final KPI values can be responsibly reported. The next analysis step is therefore to run the actual Olist files locally and replace these examples with measured results, charts, and a reproducible notebook.

## Planned evidence additions
1. Row counts and missing-value percentages for each source table.
2. Number and share of delivered orders used for KPI calculations.
3. On-time vs late delivery counts and percentages.
4. Median and mean delivery duration, plus outlier counts.
5. Top regions/sellers by late-delivery rate.
6. Delivery-delay vs review-score comparison.

# Week 1 – Strategic Planning Notes

## Business Problem
Analyze e-commerce delivery performance and identify factors associated with late deliveries, longer delivery times, and inefficient logistics costs.

## Primary KPIs
1. On-Time Delivery Rate
2. Average Delivery Time
3. Average Delivery Delay
4. Late Delivery Rate
5. Freight Cost per Order
6. Customer Satisfaction / Review Score

## Research Dataset
Brazilian E-Commerce Public Dataset by Olist.

## Proposed Methods
- Descriptive statistics and KPI analysis
- Exploratory data analysis
- Regression for delivery duration
- Classification for late-delivery risk
- Clustering for seller/region segmentation
- Vehicle Routing Problem optimization as an extension

## Roadmap
Data collection → validation → cleaning → joins → feature engineering → KPI baseline → EDA → predictive modeling → clustering → optimization → recommendations.

## Important Analytical Controls
- Avoid order-level duplication when joining item-level tables.
- Exclude post-delivery information from predictive features when predicting before delivery.
- Use time-aware validation when the model is intended to predict future orders.
- Treat correlation as evidence of association, not proof of causation.

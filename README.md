# YuvaIntern – Logistics Data Science

This repository contains my work for the **YuvaIntern Data Science Internship**, focused on logistics analytics, delivery performance, predictive modeling, and optimization.

## Project Continuity

The internship work is being developed as one connected logistics analytics project. Each week's deliverable builds on the previous stage instead of treating the tasks as unrelated exercises.

## Week 1 – Strategic Planning and Data Exploration

Week 1 defines the e-commerce logistics scenario, business problem, KPIs, research foundation, analytical roadmap, and proposed use of regression, classification, clustering, and route optimization.

## Week 2 – Data Collection, Cleaning, and Preprocessing

Week 2 converts the Week 1 strategy into a reproducible data-preparation workflow. It covers data profiling, missing-value handling, duplicate and key-integrity checks, timestamp validation, outlier investigation, categorical standardization, logistics feature engineering, scaling, and leakage prevention.

### Week 2 Focus
- Data collection simulation
- Data quality assessment
- Missing-value analysis
- Duplicate and table-grain validation
- Timestamp cleaning and chronology checks
- IQR-based outlier detection
- Categorical standardization
- Delivery-time and delay feature engineering
- Standardization for model-ready data
- Final validation checklist

### Dataset
The project uses the **Brazilian E-Commerce Public Dataset by Olist**, a public dataset containing order, seller, customer, product, payment, review, and geolocation information.

Dataset source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

> The raw dataset is not committed to this repository. This keeps the repository lightweight and avoids unnecessary duplication of publicly available data.

### Analytical Roadmap
1. Data collection and data dictionary creation
2. Data quality checks and cleaning
3. Relational joins and feature engineering
4. KPI calculation and baseline assessment
5. Exploratory data analysis
6. Regression / classification for delivery prediction
7. Clustering for operational segmentation
8. Vehicle-routing optimization as an extension
9. Business recommendations and decision support

### Tools
- Python
- Pandas
- NumPy
- Matplotlib
- scikit-learn
- OR-Tools
- Jupyter Notebook

### Repository Structure

```text
Yuva-Intern-Logistics-Data-Science/
├── README.md
├── Week_1/
│   └── planning_notes.md
├── Week_2/
│   ├── README.md
│   └── preprocessing_pipeline.py
├── notebooks/
│   └── README.md
├── data/
│   └── README.md
├── src/
│   └── data_preparation.py
└── requirements.txt
```

## Internship Deliverables

Week 1 establishes the strategy and analytical design. Week 2 establishes the data-quality and preprocessing foundation. Future weeks will extend the same project with implementation, exploratory analysis, modeling, visualization, and logistics decision support as required by the internship tasks.

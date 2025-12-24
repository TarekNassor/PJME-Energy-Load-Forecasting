# PJME Energy Load Forecasting

## Overview
This project focuses on forecasting hourly electricity demand (in MW) for the PJM East (PJME) region using machine learning. An XGBoost regression model is trained on historical energy consumption data with time-based feature engineering.

The goal is to demonstrate how gradient boosting can be applied to time series forecasting problems using structured datetime features.

---

## Dataset
- **Source:** PJME Hourly Energy Consumption Data
- **Target Variable:** `PJME_MW`
- **Frequency:** Hourly
- **Index:** Datetime

---

## Key Steps

### 1. Data Preparation
- Load and parse datetime index
- Visualize long-term and short-term consumption trends
- Split data into training and test sets (pre-2015 vs post-2015)

### 2. Feature Engineering
Time-based features extracted from the datetime index:
- Hour
- Day of week
- Day of year
- Month
- Quarter
- Year

### 3. Exploratory Data Analysis
- Hourly and monthly demand distributions
- Weekly consumption patterns
- Visual inspection of seasonality and trends

### 4. Model Training
- Model: **XGBoost Regressor**
- Objective: Regression
- Learning Rate: 0.01
- Max Depth: 3
- Early stopping to prevent overfitting

### 5. Evaluation
- Metric: Root Mean Squared Error (RMSE)
- Feature importance visualization
- Error analysis by date

---

## Results
- The model captures daily and seasonal demand patterns effectively.
- Hour and day-of-year are among the most important features.
- Predictions closely follow actual energy consumption trends.

---

## Visualizations
- Time series plots of training vs testing data
- Feature importance bar charts
- Actual vs predicted energy usage
- Weekly zoom-in comparisons

---

## Technologies Used
- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- XGBoost

---

## Future Improvements
- Add lag-based features
- Incorporate weather data
- Experiment with other forecasting models (LSTM, Prophet)
- Perform cross-validation for time series

---

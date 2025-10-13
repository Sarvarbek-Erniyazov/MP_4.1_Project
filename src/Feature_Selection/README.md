# Yeosu Climate Data Feature Selection Pipeline

## Overview
This module performs **feature selection** on the feature-engineered Yeosu climate dataset. It identifies the most relevant features for predicting **Average Temperature (°C)** using a **Random Forest Regressor** with **Recursive Feature Elimination (RFE)**. The pipeline logs all steps for traceability in `logs/Feature_Selection.log`.

## Data Sources
- **Input:** `data/skewness/yeosu_weather_FE_skew.csv`  
- **Output:** `data/Feature_Selection/yeosu_weather_selected.csv`  
- **Input format:** CSV with 31 feature-engineered variables.

## Feature Selection Steps

### 1. Load Data
- Reads the CSV containing feature-engineered climate data.
- Logs the dataset shape.

### 2. Recursive Feature Elimination (RFE)
- Uses `RandomForestRegressor` as the estimator.
- Iteratively removes less important features to select the **top N features** (default: 27).
- Ensures only the most predictive features are retained.
- Logs the list of selected features.

### 3. Save Selected Features
- Saves the selected features along with the target column into a new CSV.
- Output example shape: `(7183, 28)` (27 features + target).

## Running the Pipeline
Use `run_FS.py` to execute feature selection:

```bash
python run_FS.py

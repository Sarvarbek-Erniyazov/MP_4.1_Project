# Yeosu Climate Data Skewness Handling Pipeline

## Overview
This module addresses **skewness** in the feature-engineered Yeosu climate dataset. It ensures that highly skewed features are transformed for better statistical modeling and machine learning performance. All transformations are logged for reproducibility in `logs/skewness.log`.

## Data Sources
- **Input:** `data/Engineered/yeosu_weather_FE.csv`  
- **Output:** `data/skewness/yeosu_weather_FE_skew.csv`  
- **Input format:** CSV with 31 feature-engineered variables.

## Skewness Handling Steps

### 1. Load Data
- Reads the feature-engineered CSV.
- Logs dataset shape for reference.

### 2. Encode Categorical Columns
- Identifies object-type columns (`Date`, `Season_FE`) and encodes them as categorical codes.
- Logs all encoded columns.

### 3. Detect and Transform Skewed Features
- Computes skewness for numeric columns (excluding target: `Average Temperature (°C)`).
- Identifies features with **absolute skew > 1**.
- Applies **log1p transformation** to reduce skewness.
  - If a column contains non-positive values, shifts the column before log transformation.
- Logs all transformed columns with applied shifts.

### 4. Save Transformed Dataset
- Saves the skewness-handled dataset to CSV.
- Logs the final dataset shape and save path.

## Running the Pipeline
Use `run_skewness.py` to execute skewness handling:

```bash
python run_skewness.py

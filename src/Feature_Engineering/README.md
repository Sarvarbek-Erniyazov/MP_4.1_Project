# Yeosu Climate Data Feature Engineering Pipeline

## Overview
This module performs **feature engineering** on the processed daily climate data of Yeosu, South Korea, spanning **2006–2025**. The pipeline enhances the dataset with temporal, lag/rolling, interaction, and extreme/binary features, preparing it for machine learning or time series analysis.

All operations are logged for traceability in `logs/FE.log`.

## Data Sources
- **Input:** `data/processed/yeosu_daily_weather_all_years.csv`
- **Output:** `data/Engineered/yeosu_weather_FE.csv`
- **Input format:** CSV with cleaned and standardized meteorological variables.

## Feature Engineering Steps

### 1. Load Data
- Reads the processed CSV file into a Pandas DataFrame.
- Logs the loaded shape of the dataset.

### 2. Handle Missing Values
- Performs forward-fill and backward-fill to impute missing values.
- Ensures no gaps remain before feature creation.

### 3. Temporal Features
- Constructs a `Date` column from `Year`, `Month`, and `Day`.
- Adds:
  - `Day_of_Week_FE`: Day of the week (0–6)
  - `Day_of_Year_FE`: Day of the year (1–365/366)
  - `Season_FE`: Season mapping (`Winter`, `Spring`, `Summer`, `Autumn`)
  - Cyclical encoding for day of year: `Day_sin_FE`, `Day_cos_FE`

### 4. Lag & Rolling Features
- Lag features:
  - `AvgTemp_lag1_FE`, `AvgTemp_lag7_FE`
  - `Humidity_lag1_FE`, `Pressure_diff_FE`
- Rolling features (7-day):
  - `AvgTemp_7d_mean_FE`, `AvgTemp_7d_std_FE`
  - `Precip_7d_sum_FE`
- Missing values in lag/rolling features are forward/backward filled.

### 5. Interaction Features
- Combines key variables to capture interactions:
  - `Temp_Humidity_FE` = Temperature × Humidity
  - `Temp_Wind_FE` = Temperature × Wind Speed

### 6. Extreme / Binary Features
- Creates indicators for unusual conditions:
  - `HotDay_FE` (>30°C), `ColdDay_FE` (<0°C)
  - `WindyDay_FE` (>50 km/h)
  - `RainyDay_FE` (Precipitation > 0)

## Running the Pipeline
Use `run_FE.py` to execute the full feature engineering process:

```bash
python run_FE.py

# Yeosu Climate Data Processing Pipeline

## Overview
This module processes the raw daily climate data scraped for Yeosu, South Korea, spanning **2006 to 2025**. The pipeline cleans, merges, and standardizes the dataset, preparing it for analysis or machine learning tasks.

The pipeline also logs all events, warnings, and errors to ensure traceability and reproducibility.

## Data Sources
- **Raw data folder:** `data/raw`  
- **Processed output:** `data/processed/yeosu_daily_weather_all_years.csv`  
- **Input files:** `yeosu_daily_weather_<year>.csv` for each year  

## Processing Steps

### 1. Load Data
- Each year’s CSV file is loaded individually.
- Missing files are logged as warnings without halting the pipeline.
- Logs provide the shape of each year’s dataset.

### 2. Clean and Rename Columns
- Unnecessary columns for numerical modeling are dropped:
  - `VG`, `RA`, `SN`, `TS`, `FG`
- Remaining columns are renamed for clarity:

| Original | Renamed |
|----------|---------|
| T        | Average Temperature (°C) |
| TM       | Maximum Temperature (°C) |
| Tm       | Minimum Temperature (°C) |
| SLP      | Atmospheric Pressure (hPa) |
| H        | Relative Humidity (%) |
| PP       | Precipitation (mm) |
| VV       | Visibility (km) |
| V        | Wind Speed (km/h) |
| VM       | Max Sustained Wind (km/h) |

### 3. Merge Data
- All years are concatenated into a single DataFrame.
- The merged dataset is saved as CSV in the `processed` folder.

### 4. Logging
- Pipeline events, warnings, and errors are logged to `logs/processing.log`.
- Example log entries:


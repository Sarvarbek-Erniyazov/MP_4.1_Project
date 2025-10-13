# Yeosu Climate Data Analysis and Prediction Project

## Project Overview
The **primary goal** of this project is to develop an **end-to-end pipeline for historical climate data** for Yeosu, South Korea, starting from **web scraping raw data** to building a **predictive model** for daily average temperature.  

Unlike most studies that rely on pre-collected datasets, this project emphasizes **data acquisition from public sources**, transforming raw, unstructured tables into a clean, feature-rich dataset suitable for machine learning.  

The project covers data from **2006 to August 2025**, including key meteorological variables such as temperature, humidity, precipitation, wind speed, visibility, and atmospheric pressure.

---

## Project Objectives
1. **Web Scraping and Data Collection:**  
   - Acquire daily climate records directly from public websites.  
   - Automate data extraction for all available years, ensuring completeness and accuracy.  
   - Log missing data or errors to ensure traceability.

2. **Data Processing:**  
   - Merge yearly datasets into a consistent format.  
   - Clean missing values and standardize data types.  
   - Generate a master dataset suitable for analysis and modeling.

3. **Feature Engineering:**  
   - Extract temporal, lag, rolling, interaction, and extreme features.  
   - Encode cyclical patterns (e.g., day of year, seasons).  
   - Produce enriched datasets that maximize predictive performance.

4. **Skewness Handling:**  
   - Identify skewed numerical features.  
   - Apply log-based transformations with shifts for zero or negative values.  
   - Ensure stability and normality for regression models.

5. **Feature Selection:**  
   - Use **Recursive Feature Elimination (RFE) with Random Forest** to select the most informative features.  
   - Reduce dimensionality while retaining predictive power.

6. **Regression Modeling:**  
   - Train multiple regression models (Linear, Ridge, Lasso, ElasticNet, DecisionTree, RandomForest, GradientBoosting, SVR).  
   - Evaluate using **RMSE** and **R²**, selecting the best model for production.

7. **End-to-End Reproducibility:**  
   - Each pipeline stage is logged.  
   - Final models and datasets are stored for reproducibility and future use.  

---

## Data Source
- **Website:** [en.tutiempo.net](https://en.tutiempo.net)
- **Data Frequency:** Daily
- **Variables Collected:**
  - Day, Month, Year
  - Temperature (Average, Max, Min)
  - Atmospheric Pressure (hPa)
  - Relative Humidity (%)
  - Precipitation (mm)
  - Visibility (km)
  - Wind Speed (km/h)
  - Max Sustained Wind (km/h)
  - Rain, Snow, Thunderstorm, Fog

---

## Methodology

### 1. Web Scraping (Primary Focus)
- **Goal:** Collect raw climate data directly from public sources rather than relying on pre-processed datasets.  
- **Approach:** Python scripts using `requests` and `BeautifulSoup` automatically extract monthly climate tables for each year.  
- **Outcome:** A collection of raw CSV files for each year, merged into a **master dataset**.  

### 2. Data Processing
- Merge all yearly CSV files into a single dataset.  
- Drop irrelevant or empty columns.  
- Handle missing values via forward/backward fill.  
- Ensure consistent data types for downstream analysis.

### 3. Feature Engineering
- **Temporal features:** Day-of-week, day-of-year, season, cyclical encoding.  
- **Lag & rolling features:** 1-day lag, 7-day rolling mean/std, precipitation sums.  
- **Interaction features:** Temperature × Humidity, Temperature × Wind.  
- **Extreme/binary features:** HotDay (>30°C), ColdDay (<0°C), WindyDay, RainyDay.  
- **Output:** Dataset with 31 engineered features.

### 4. Skewness Handling
- Encode categorical columns.  
- Identify highly skewed numerical features (|skew| > 1).  
- Apply log transformations with shift for zero/negative values.  
- Produces a stable, normalized dataset for modeling.

### 5. Feature Selection
- Recursive Feature Elimination (RFE) with RandomForestRegressor.  
- Selected **top 27 features** most relevant to average temperature prediction.  
- Reduced dataset size improves model efficiency without losing information.

### 6. Regression Modeling
- Train multiple models: LinearRegression, Ridge, Lasso, ElasticNet, DecisionTree, RandomForest, GradientBoosting, SVR.  
- Evaluate models using RMSE and R² metrics.  
- **Best Model:** GradientBoosting Regressor with **R² = 0.9969**, **RMSE = 0.4718**.  
- Model is saved for deployment and further analysis.

---

## Results and Model Comparison

| Model                  | RMSE   | R² Score |
|------------------------|--------|----------|
| LinearRegression       | 0.5029 | 0.9965   |
| Ridge                  | 0.5029 | 0.9965   |
| Lasso                  | 0.7142 | 0.9930   |
| ElasticNet             | 0.6547 | 0.9941   |
| DecisionTree           | 0.7005 | 0.9933   |
| RandomForest           | 0.4767 | 0.9969   |
| GradientBoosting       | 0.4718 | 0.9969   |
| SVR                    | 2.2342 | 0.9315   |

**Observations:**
- GradientBoosting and RandomForest achieved the highest predictive accuracy.
- Temporal and lag features greatly improve model performance.
- Interaction and extreme features provide additional predictive value.
- Skewness handling stabilizes the dataset and prevents outlier distortion.
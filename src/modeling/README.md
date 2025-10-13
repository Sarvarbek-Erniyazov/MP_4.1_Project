# Yeosu Climate Data Regression Modeling Pipeline

## Overview
This module trains and evaluates multiple **regression models** to predict the **Average Temperature (°C)** for Yeosu using the selected and preprocessed climate features. The pipeline automatically identifies the best-performing model and saves it for future use.

## Data Sources
- **Input:** `data/Feature_Selection/yeosu_weather_selected.csv`  
- **Output:** Serialized best model saved as `.pkl` in `models/best_model/best_model.pkl`  
- **Input format:** CSV with numeric and encoded features, post-feature selection.

## Pipeline Steps

### 1. Load Data
- Reads the feature-selected dataset.
- Logs dataset shape for reproducibility.

### 2. Train-Test Split
- Splits data into training and testing sets (default `80/20` split).
- Ensures reproducibility with a fixed random seed.
- Logs the shape of train and test sets.

### 3. Train and Evaluate Models
- Trains multiple regression models:
  - LinearRegression
  - Ridge
  - Lasso
  - ElasticNet
  - DecisionTreeRegressor
  - RandomForestRegressor
  - GradientBoostingRegressor
  - Support Vector Regressor (SVR)
- Evaluates performance using:
  - **RMSE** (Root Mean Squared Error)
  - **R² Score**
- Logs model performance and identifies the best model.

### 4. Save Best Model
- Serializes and saves the best-performing model to a `.pkl` file.
- Ensures reproducibility and easy deployment.

## Model Results

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

**Best Model:** GradientBoosting with **R² = 0.9969**  
**Saved Model Path:** `models/best_model/best_model.pkl`

### Notes
- Gradient Boosting and Random Forest performed best with nearly identical R² scores.
- SVR performed poorly due to high complexity and scaling sensitivity.
- RMSE values indicate extremely accurate temperature predictions on the test set.
- Fully reproducible and traceable through detailed logging in `logs/modeling.log`.

## Running the Pipeline
Use `run_modeling.py` to execute the modeling pipeline:

```bash
python run_modeling.py

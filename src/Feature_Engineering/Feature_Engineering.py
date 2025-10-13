# Feature_Engineering.py
import pandas as pd
from pathlib import Path
import numpy as np
import logging

# -------------------------------
# Logging setup
# -------------------------------
log_path = Path(r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\logs\FE.log")
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class YeosuFE:
    def __init__(self, input_path, output_path):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.df = pd.DataFrame()

    # -------------------------------
    # Load data
    # -------------------------------
    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        logging.info(f"Loaded data: shape {self.df.shape}")

    # -------------------------------
    # Handle missing values
    # -------------------------------
    def handle_missing(self):
        # Forward-fill then back-fill for basic imputation
        self.df.ffill(inplace=True)
        self.df.bfill(inplace=True)
        logging.info("Handled missing values using forward/backward fill")

    # -------------------------------
    # Temporal features
    # -------------------------------
    def temporal_features(self):
        self.df['Date'] = pd.to_datetime(self.df[['Year', 'Month', 'Day']])
        self.df['Day_of_Week_FE'] = self.df['Date'].dt.dayofweek
        self.df['Day_of_Year_FE'] = self.df['Date'].dt.dayofyear
        # Season mapping
        self.df['Season_FE'] = self.df['Month'].map({12: 'Winter',1:'Winter',2:'Winter',
                                                     3:'Spring',4:'Spring',5:'Spring',
                                                     6:'Summer',7:'Summer',8:'Summer',
                                                     9:'Autumn',10:'Autumn',11:'Autumn'})
        # Cyclical encoding
        self.df['Day_sin_FE'] = np.sin(2 * np.pi * self.df['Day_of_Year_FE']/365)
        self.df['Day_cos_FE'] = np.cos(2 * np.pi * self.df['Day_of_Year_FE']/365)
        logging.info("Created temporal features with _FE suffix")

    # -------------------------------
    # Lag & rolling features
    # -------------------------------
    def lag_rolling_features(self):
        self.df.sort_values('Date', inplace=True)
        # Lag features
        self.df['AvgTemp_lag1_FE'] = self.df['Average Temperature (°C)'].shift(1)
        self.df['AvgTemp_lag7_FE'] = self.df['Average Temperature (°C)'].rolling(7).mean().shift(1)
        self.df['Humidity_lag1_FE'] = self.df['Relative Humidity (%)'].shift(1)
        self.df['Pressure_diff_FE'] = self.df['Atmospheric Pressure (hPa)'].diff()
        # Rolling
        self.df['AvgTemp_7d_mean_FE'] = self.df['Average Temperature (°C)'].rolling(7).mean()
        self.df['AvgTemp_7d_std_FE'] = self.df['Average Temperature (°C)'].rolling(7).std()
        self.df['Precip_7d_sum_FE'] = self.df['Precipitation (mm)'].rolling(7).sum()
        logging.info("Created lag and rolling features with _FE suffix")

        # -------------------------------
        # Handle remaining missing values for lag/rolling
        # -------------------------------
        lag_rolling_cols = [
            'AvgTemp_lag1_FE', 'AvgTemp_lag7_FE', 'Humidity_lag1_FE',
            'Pressure_diff_FE', 'AvgTemp_7d_mean_FE', 'AvgTemp_7d_std_FE', 'Precip_7d_sum_FE'
        ]
        self.df[lag_rolling_cols] = self.df[lag_rolling_cols].ffill().bfill()
        logging.info("Filled remaining missing values in lag/rolling features")

    # -------------------------------
    # Interaction features
    # -------------------------------
    def interaction_features(self):
        self.df['Temp_Humidity_FE'] = self.df['Average Temperature (°C)'] * self.df['Relative Humidity (%)']
        self.df['Temp_Wind_FE'] = self.df['Average Temperature (°C)'] * self.df['Wind Speed (km/h)']
        logging.info("Created interaction features with _FE suffix")

    # -------------------------------
    # Extreme / binary features
    # -------------------------------
    def extreme_features(self):
        self.df['HotDay_FE'] = (self.df['Average Temperature (°C)'] > 30).astype(int)
        self.df['ColdDay_FE'] = (self.df['Average Temperature (°C)'] < 0).astype(int)
        self.df['WindyDay_FE'] = (self.df['Wind Speed (km/h)'] > 50).astype(int)
        self.df['RainyDay_FE'] = (self.df['Precipitation (mm)'] > 0).astype(int)
        logging.info("Created extreme/binary features with _FE suffix")

    # -------------------------------
    # Run full pipeline
    # -------------------------------
    def run(self):
        logging.info("=== Feature Engineering Pipeline Started ===")
        self.load_data()
        self.handle_missing()
        self.temporal_features()
        self.lag_rolling_features()
        self.interaction_features()
        self.extreme_features()
        # Save final dataset
        self.df.to_csv(self.output_path, index=False)
        logging.info(f"Feature engineered data saved: {self.output_path}")
        logging.info(f"Final shape: {self.df.shape}")
        logging.info("=== Feature Engineering Pipeline Finished ===")
        return self.df

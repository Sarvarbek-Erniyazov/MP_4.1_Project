# skewness.py
import pandas as pd
import numpy as np
from pathlib import Path
import logging

# -------------------------------
# Logging setup
# -------------------------------
log_path = Path(r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\logs\skewness.log")
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class SkewnessHandler:
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
    # Encode categorical columns
    # -------------------------------
    def encode_categorical(self):
        cat_cols = self.df.select_dtypes(include='object').columns
        for col in cat_cols:
            self.df[col] = self.df[col].astype('category').cat.codes
            logging.info(f"Encoded categorical column: {col}")

    # -------------------------------
    # Handle skewness
    # -------------------------------
    def handle_skewness(self):
        # Select numeric features excluding target
        feature_cols = self.df.drop(columns=['Average Temperature (°C)']).select_dtypes(include=['float64', 'int64']).columns
        
        skewed_features = self.df[feature_cols].skew()
        skewed_features = skewed_features[skewed_features.abs() > 1]
        logging.info(f"Identified highly skewed features: {list(skewed_features.index)}")

        for col in skewed_features.index:
            min_val = self.df[col].min()
            if min_val <= 0:
                shift = abs(min_val) + 1
                self.df[col] = np.log1p(self.df[col] + shift)
                logging.info(f"Applied log1p transform with shift={shift} to column: {col}")
            else:
                self.df[col] = np.log1p(self.df[col])
                logging.info(f"Applied log1p transform to column: {col}")

    # -------------------------------
    # Run full pipeline
    # -------------------------------
    def run(self):
        logging.info("=== Skewness Handling Pipeline Started ===")
        self.load_data()
        self.encode_categorical()
        self.handle_skewness()
        # Save final dataset
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(self.output_path, index=False)
        logging.info(f"Skewness-handled data saved: {self.output_path}")
        logging.info(f"Final shape: {self.df.shape}")
        logging.info("=== Skewness Handling Pipeline Finished ===")
        return self.df

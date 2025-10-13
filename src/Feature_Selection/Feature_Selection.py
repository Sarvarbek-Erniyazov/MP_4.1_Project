# Feature_Selection.py
import pandas as pd
import numpy as np
from pathlib import Path
import logging
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE

# -------------------------------
# Logging setup
# -------------------------------
log_path = Path(r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\logs\Feature_Selection.log")
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class FeatureSelector:
    def __init__(self, input_path, output_path, target='Average Temperature (°C)', n_features_to_select=25, random_state=42):
        self.input_path = Path(input_path)
        self.output_path = Path(output_path)
        self.target = target
        self.df = pd.DataFrame()
        self.n_features_to_select = n_features_to_select
        self.random_state = random_state

    # -------------------------------
    # Load data
    # -------------------------------
    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        logging.info(f"Loaded data: shape {self.df.shape}")

    # -------------------------------
    # Feature Selection with RFE
    # -------------------------------
    def select_features(self):
        # All columns numeric; drop target only
        X = self.df.drop(columns=[self.target])
        y = self.df[self.target]

        # Initialize RandomForestRegressor
        rf = RandomForestRegressor(n_estimators=200, random_state=self.random_state)

        # Recursive Feature Elimination
        rfe = RFE(estimator=rf, n_features_to_select=self.n_features_to_select)
        rfe.fit(X, y)

        # Selected features
        selected_features = X.columns[rfe.support_].tolist()
        logging.info(f"Selected top {self.n_features_to_select} features: {selected_features}")

        # Save selected features
        self.df_selected = self.df[selected_features + [self.target]]
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.df_selected.to_csv(self.output_path, index=False)
        logging.info(f"Selected features saved to {self.output_path}")
        return selected_features

    # -------------------------------
    # Run full pipeline
    # -------------------------------
    def run(self):
        logging.info("=== Feature Selection Pipeline Started ===")
        self.load_data()
        selected_features = self.select_features()
        logging.info(f"Final dataset shape: {self.df_selected.shape}")
        logging.info("=== Feature Selection Pipeline Finished ===")
        return self.df_selected, selected_features

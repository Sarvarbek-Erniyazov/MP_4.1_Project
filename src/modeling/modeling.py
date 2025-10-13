# modeling.py
import pandas as pd
import numpy as np
from pathlib import Path
import logging
import pickle
from math import sqrt  # for RMSE calculation

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Regression models
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

# -------------------------------
# Logging setup
# -------------------------------
log_path = Path(r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\logs\modeling.log")
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class RegressionModeling:
    def __init__(self, input_path, target='Average Temperature (°C)', random_state=42, test_size=0.2):
        self.input_path = Path(input_path)
        self.df = pd.DataFrame()
        self.target = target
        self.random_state = random_state
        self.test_size = test_size
        self.models = {
            'LinearRegression': LinearRegression(),
            'Ridge': Ridge(random_state=random_state),
            'Lasso': Lasso(random_state=random_state),
            'ElasticNet': ElasticNet(random_state=random_state),
            'DecisionTree': DecisionTreeRegressor(random_state=random_state),
            'RandomForest': RandomForestRegressor(n_estimators=200, random_state=random_state),
            'GradientBoosting': GradientBoostingRegressor(n_estimators=200, random_state=random_state),
            'SVR': SVR()
        }
        self.results = {}
        self.best_model = None
        self.best_score = -np.inf

    # -------------------------------
    # Load data
    # -------------------------------
    def load_data(self):
        self.df = pd.read_csv(self.input_path)
        logging.info(f"Data loaded: shape {self.df.shape}")

    # -------------------------------
    # Split features and target
    # -------------------------------
    def prepare_data(self):
        X = self.df.drop(columns=[self.target])
        y = self.df[self.target]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.test_size, random_state=self.random_state
        )
        logging.info(f"Train/Test split: {X_train.shape}/{X_test.shape}")
        return X_train, X_test, y_train, y_test

    # -------------------------------
    # Train and evaluate models
    # -------------------------------
    def train_evaluate(self):
        X_train, X_test, y_train, y_test = self.prepare_data()
        for name, model in self.models.items():
            logging.info(f"Training {name}...")
            model.fit(X_train, y_train)
            preds = model.predict(X_test)

            # Python 3.13 compatible RMSE
            rmse = sqrt(mean_squared_error(y_test, preds))
            r2 = r2_score(y_test, preds)

            self.results[name] = {'RMSE': rmse, 'R2': r2}
            logging.info(f"{name} - RMSE: {rmse:.4f}, R2: {r2:.4f}")

            # Check best model
            if r2 > self.best_score:
                self.best_score = r2
                self.best_model = (name, model)
        logging.info(f"Best model: {self.best_model[0]} with R2={self.best_score:.4f}")

    # -------------------------------
    # Save best model
    # -------------------------------
    def save_best_model(self, output_path):
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f:
            pickle.dump(self.best_model[1], f)
        logging.info(f"Best model saved: {output_path}")
        return output_path

    # -------------------------------
    # Run full pipeline
    # -------------------------------
    def run(self, save_path):
        logging.info("=== Regression Modeling Pipeline Started ===")
        self.load_data()
        self.train_evaluate()
        saved_path = self.save_best_model(save_path)
        logging.info("=== Regression Modeling Pipeline Finished ===")
        return self.results, self.best_model[0], saved_path

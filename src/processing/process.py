# process.py
import pandas as pd
from pathlib import Path
import logging

# -------------------------------
# Logging setup
# -------------------------------
log_path = Path(
    r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\logs\processing.log"
)
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# Pipeline Class
# -------------------------------
class YeosuPipeline:
    def __init__(self, raw_folder, processed_path, years=range(2006, 2026)):
        self.raw_folder = Path(raw_folder)
        self.processed_path = Path(processed_path)
        self.years = years

        # Columns to drop (not useful for numerical modeling)
        self.drop_cols = ["VG", "RA", "SN", "TS", "FG"]

        # Columns to rename — easy to understand names
        self.rename_map = {
            "T": "Average Temperature (°C)",
            "TM": "Maximum Temperature (°C)",
            "Tm": "Minimum Temperature (°C)",
            "SLP": "Atmospheric Pressure (hPa)",
            "H": "Relative Humidity (%)",
            "PP": "Precipitation (mm)",
            "VV": "Visibility (km)",
            "V": "Wind Speed (km/h)",
            "VM": "Max Sustained Wind (km/h)",
        }

    def load_year(self, year):
        """Load a single year's CSV file."""
        path = self.raw_folder / f"yeosu_daily_weather_{year}.csv"
        try:
            df = pd.read_csv(path)
            logging.info(f"Loaded {year}: shape {df.shape}")
            return df
        except FileNotFoundError:
            logging.warning(f"Missing file for year {year}: {path}")
            return pd.DataFrame()

    def clean_and_rename(self, df):
        """Drop unused columns and rename for readability."""
        df = df.drop(columns=self.drop_cols, errors="ignore")
        df = df.rename(columns=self.rename_map)
        return df

    def run(self):
        """Run the full pipeline across all years."""
        logging.info("=== YEOSU Weather Processing Pipeline Started ===")
        all_dfs = []

        for year in self.years:
            df = self.load_year(year)
            if df.empty:
                continue
            df = self.clean_and_rename(df)
            all_dfs.append(df)

        if not all_dfs:
            logging.error("No data was processed. Check raw folder.")
            return pd.DataFrame()

        merged_df = pd.concat(all_dfs, ignore_index=True)
        merged_df.to_csv(self.processed_path, index=False)

        logging.info(f"Processed data saved: {self.processed_path}")
        logging.info(f"Final dataset shape: {merged_df.shape}")
        logging.info("=== Pipeline Finished Successfully ===")
        return merged_df

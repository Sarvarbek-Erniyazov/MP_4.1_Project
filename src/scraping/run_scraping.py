from scraping.climate_scraper import ClimateYeosuScraper
import os
import pandas as pd

# --- Paths ---
project_path = os.path.dirname(os.path.abspath(__file__))
raw_path = os.path.join(project_path, "..", "data", "raw")
processed_path = os.path.join(project_path, "..", "data", "processed")

os.makedirs(raw_path, exist_ok=True)
os.makedirs(processed_path, exist_ok=True)

all_data = []

# --- Years 2006 to August 2025 ---
for year in range(2006, 2026):
    last_month = 8 if year == 2025 else 12
    scraper = ClimateYeosuScraper(year)
    df_year = scraper.scrape_year(last_month=last_month)

    if not df_year.empty:
        raw_file = os.path.join(raw_path, f"yeosu_daily_weather_{year}.csv")
        df_year.to_csv(raw_file, index=False)
        all_data.append(df_year)
        print(f"✅ Year {year} scraped and saved ({len(df_year)} rows)")
    else:
        print(f"⚠️ Year {year} has no data, skipped.")

# --- Merge all years ---
if all_data:
    final_df = pd.concat(all_data, ignore_index=True)
    final_file = os.path.join(processed_path, "yeosu_daily_weather_all_years.csv")
    final_df.to_csv(final_file, index=False)
    print(f"🎉 All years merged. CSV saved at: {final_file}")
else:
    print("⚠️ No data scraped for any year.")

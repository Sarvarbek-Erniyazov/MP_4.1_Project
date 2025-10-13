# run_process.py
from processing.process import YeosuPipeline


raw_folder = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\raw"
processed_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\processed\yeosu_daily_weather_all_years.csv"

if __name__ == "__main__":
    print("Running Yeosu weather data processing pipeline...")
    pipeline = YeosuPipeline(raw_folder, processed_path)
    merged_df = pipeline.run()
    print(f"Pipeline completed. Final data shape: {merged_df.shape}")
    print("Logs saved to /logs/processing.log")

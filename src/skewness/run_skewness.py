# run_skewness.py
from skewness.skewness import SkewnessHandler

input_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\Engineered\yeosu_weather_FE.csv"
output_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\skewness\yeosu_weather_FE_skew.csv"

if __name__ == "__main__":
    print("Running Skewness Handling pipeline...")
    pipeline = SkewnessHandler(input_path, output_path)
    df_skewed = pipeline.run()
    print(f"Skewness handling completed. Final shape: {df_skewed.shape}")
    print("Logs saved to skewness.log")

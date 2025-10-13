# run_FE.py
from Feature_Engineering.Feature_Engineering import YeosuFE

input_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\processed\yeosu_daily_weather_all_years.csv"
output_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\Engineered\yeosu_weather_FE.csv"

if __name__ == "__main__":
    print("Running Yeosu Feature Engineering pipeline...")
    pipeline = YeosuFE(input_path, output_path)
    df_FE = pipeline.run()
    print(f"Feature Engineering completed. Final shape: {df_FE.shape}")
    print("Logs saved to /logs/FE.log")

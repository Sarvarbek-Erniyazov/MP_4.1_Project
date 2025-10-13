# run_FS.py
from Feature_Selection.Feature_Selection import FeatureSelector

input_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\skewness\yeosu_weather_FE_skew.csv"
output_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\Feature_Selection\yeosu_weather_selected.csv"

if __name__ == "__main__":
    print("Running Feature Selection pipeline...")
    pipeline = FeatureSelector(input_path=input_path, output_path=output_path, n_features_to_select=27)
    df_selected, selected_features = pipeline.run()
    print(f"Feature selection completed. Selected {len(selected_features)} features:")
    print(selected_features)
    print(f"Saved selected features to: {output_path}")
    print("Logs saved to Feature_Selection.log")

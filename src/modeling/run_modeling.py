# run_modeling.py
from modeling import RegressionModeling  # import from modeling.py

# Paths
input_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\data\Feature_Selection\yeosu_weather_selected.csv"
model_output_path = r"C:\Users\sharg\Desktop\uyga vazifa\unsupervised learning\3-oy\final\Climate YEOSU\models\best_model\best_model.pkl"

def main():
    print("Running Regression Modeling pipeline...")

    # Initialize pipeline
    pipeline = RegressionModeling(
        input_path=input_path,
        target='Average Temperature (°C)',
        random_state=42
    )

    # Run pipeline and save best model
    results, best_model_name, saved_path = pipeline.run(save_path=str(model_output_path))

    print(f"Best model: {best_model_name}")
    print(f"Saved best model to: {saved_path}")
    print(f"Logs saved to: C:\\Users\\sharg\\Desktop\\uyga vazifa\\unsupervised learning\\3-oy\\final\\Climate YEOSU\\logs\\modeling.log")

if __name__ == "__main__":
    main()

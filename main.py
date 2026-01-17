# ==========================================================
# COGNIPATH ENGINE: MAIN EXECUTION
# ==========================================================
from preprocessing import DataEngineer
from model_engine import EduModel
import pandas as pd

def run_system():
    print("[System Start] Initializing CogniPath Engine...")
    
    # 1. Data Engineering
    engineer = DataEngineer('train.csv')
    raw_data = engineer.load_and_engineer()
    X_train, X_test, y_train, y_test, preprocessor = engineer.build_pipeline()
    print("[Module 1] Data Engineering Complete.")
    
    # 2. Model Training
    model_system = EduModel(preprocessor)
    print("[Module 2] Training Gradient Boosting Ensemble...")
    model_system.train(X_train, y_train)
    
    # 3. Generating Insights
    r2, mae, preds = model_system.evaluate(X_test, y_test)
    print(f"\n[Telemetry] System Accuracy: {r2:.4f} R²")
    
    # 4. SAVE RESULTS FOR DASHBOARD (Important Step)
    results_df = X_test.copy()
    results_df['Actual_Score'] = y_test
    results_df['Predicted_Score'] = preds
    results_df.to_csv('model_results_for_dashboard.csv', index=False)
    
    print("[Storage] Predictions saved to 'model_results_for_dashboard.csv'")
    print("NOW OPEN 'Analytics_Dashboard.ipynb' TO VIEW GRAPHS.")

if __name__ == "__main__":
    run_system()
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class DataEngineer:
    """
    Handles data ingestion, cleaning, and advanced feature engineering 
    for the EduMatrix Cognitive Engine.
    """
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.preprocessor = None

    def load_and_engineer(self):
        """Loads raw data and applies behavioral logic transformations."""
        try:
            self.df = pd.read_csv(self.filepath)
            
            # Feature Engineering: Cognitive Efficiency Ratio
            # Logic: High study hours with low sleep reduces retention.
            self.df['Efficiency_Ratio'] = self.df['study_hours'] / (self.df['sleep_hours'] + 1)
            
            # Feature Engineering: Attendance Risk Segmentation
            self.df['Attendance_Risk'] = np.where(self.df['class_attendance'] < 75, 'High Risk', 'Low Risk')
            
            return self.df
            
        except FileNotFoundError:
            raise Exception(f"CRITICAL ERROR: Data file not found at {self.filepath}")

    def build_pipeline(self, target_col='exam_score'):
        """Constructs the Scikit-Learn transformation pipeline."""
        
        # Define feature groups
        categorical_features = ['gender', 'course', 'sleep_quality', 'study_method', 'exam_difficulty', 'Attendance_Risk']
        numerical_features = ['age', 'study_hours', 'sleep_hours', 'Efficiency_Ratio', 'class_attendance']
        
        # Split Data
        X = self.df[numerical_features + categorical_features]
        y = self.df[target_col]
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Preprocessing Transformers
        numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
        categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])
        
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)
            ])
            
        return self.X_train, self.X_test, self.y_train, self.y_test, self.preprocessor
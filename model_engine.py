from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score, mean_absolute_error

class EduModel:
    """
    Wraps the Gradient Boosting Regressor within a Scikit-Learn Pipeline
    for reproducible training and inference.
    """
    
    def __init__(self, preprocessor):
        self.pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('regressor', GradientBoostingRegressor(
                n_estimators=300,       # Increased for better convergence
                learning_rate=0.05,     # Slow learning for generalization
                max_depth=4,            # Prevent overfitting
                random_state=42
            ))
        ])
        
    def train(self, X_train, y_train):
        """Fits the ensemble model to the training tensors."""
        self.pipeline.fit(X_train, y_train)
        
    def evaluate(self, X_test, y_test):
        """Returns performance telemetry (R2 Score and MAE)."""
        predictions = self.pipeline.predict(X_test)
        
        accuracy = r2_score(y_test, predictions)
        error_margin = mean_absolute_error(y_test, predictions)
        
        return accuracy, error_margin, predictions
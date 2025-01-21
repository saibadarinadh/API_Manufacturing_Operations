import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

class DowntimePredictor:
    def __init__(self):
        self.model = LogisticRegression(random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False

    def train(self, data):
        X = data[['Temperature', 'Run_Time']]
        y = data['Downtime_Flag']

        X_scaled = self.scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)
        self.is_trained = True

        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        return {'accuracy': accuracy, 'f1_score': f1}

    def predict(self, temperature, run_time):
        if not self.is_trained:
            raise Exception("Model not trained yet. Please train the model first.")
        
        X = [[temperature, run_time]]
        X_scaled = self.scaler.transform(X)
        prediction = self.model.predict(X_scaled)[0]
        confidence = self.model.predict_proba(X_scaled)[0][prediction]

        return {'Downtime': 'Yes' if prediction == 1 else 'No', 'Confidence': float(confidence)}
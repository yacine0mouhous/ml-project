import joblib
import pandas as pd
import numpy as np

# Load once
model = joblib.load('./models/fat/fat-model.pkl')
scaler = joblib.load('./models/fat/fat-scaler.pkl')
selected_features = joblib.load('./models/fat/fat-selected_features.pkl')

def predict_fat_percentage(data: dict):
    # Create DataFrame with correct feature order
    df = pd.DataFrame([data])[selected_features]
    
    # Scale features
    scaled_features = scaler.transform(df)
    
    # Predict
    prediction = model.predict(scaled_features)[0]
    
    # Return prediction rounded to 2 decimals
    return {"Predicted_Fat_Percentage": round(float(prediction), 2)}

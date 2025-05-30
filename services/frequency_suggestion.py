import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load('./models/workout-frequency/workout_frequency_model.pkl')
scaler = joblib.load('./models/workout-frequency/workout_frequency_scaler.pkl')

def predict_workout_frequency(data_json):
    try:
        # Convert input JSON to DataFrame with correct columns
        input_df = pd.DataFrame([data_json], columns=['Weight (kg)', 'Session_Duration (hours)', 'Fat_Percentage', 'Experience_Level', 'BMI'])
        
        # Scale input features
        scaled_features = scaler.transform(input_df)
        
        # Predict workout frequency
        prediction = model.predict(scaled_features)[0]
        
        # Round and cast to integer
        return {'Workout_Frequency (days/week)': int(round(prediction))}
    except Exception as e:
        return {'error': str(e)}

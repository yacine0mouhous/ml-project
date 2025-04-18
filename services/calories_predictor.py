import joblib
import numpy as np

# Load model and preprocessing tools
model = joblib.load('./models/calories_burn/calories_model.pkl')
scaler = joblib.load('./models/calories_burn/calories_scaler.pkl')
label_encoders = joblib.load('./models/calories_burn/calories_label_encoders.pkl')

def predict(data):
    # Ensure correct encoding for Workout_Type and Experience_Level
    try:
        workout_type = label_encoders['Workout_Type'].transform([data['Workout_Type']])[0]
        experience_level = label_encoders['Experience_Level'].transform([data['Experience_Level']])[0]
    except KeyError:
        return {'error': 'Invalid categorical values for Workout_Type or Experience_Level'}

    features = [
        workout_type,
        data['Session_Duration'],
        data['Max_BPM'],
        data['Avg_BPM'],
        data['Age'],
        data['Weight'],
        experience_level
    ]

    # Scale features
    features_scaled = scaler.transform([features])

    # Predict
    prediction = model.predict(features_scaled)[0]

    return {'Calories_Burned': round(prediction, 2)}

import joblib
import numpy as np
"""
model = joblib.load('models/workout_type_model.pkl')
scaler = joblib.load('models/workout_type_scaler.pkl')
encoders = joblib.load('models/workout_type_label_encoders.pkl')

def predict(data):
    gender_encoded = 1 if data['Gender'].lower() == 'male' else 0

    features = [
        data['Age'],
        gender_encoded,
        data['BMI'],
        data['Fat%'],
        data['Max_BPM'],
        data['Avg_BPM'],
        data['Experience'],
        data['Frequency']
    ]

    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]

    # Convert numeric class back to label
    workout_type = encoders['Workout_Type'].inverse_transform([prediction])[0]

    return {'Workout_Type': workout_type}
"""
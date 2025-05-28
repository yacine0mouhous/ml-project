import joblib
import pandas as pd
from flask import request, jsonify

# Load model and encoder globally once
model = joblib.load('./models/workout-type/workout_model.pkl')
goal_encoder = joblib.load('./models/workout-type/label_encoder.pkl')

def predict_workout_controller():
    data = request.get_json()

    required_fields = ['Goal', 'Height (m)', 'Weight (kg)', 'Age', 'Experience_Level']
    if not all(field in data for field in required_fields):
        return jsonify({'error': f'Missing fields. Required: {required_fields}'}), 400

    df = pd.DataFrame([data])

    try:
        df['Goal_encoded'] = goal_encoder.transform(df['Goal'])
    except ValueError:
        return jsonify({'error': 'Invalid Goal value'}), 400

    X = df[['Goal_encoded', 'Height (m)', 'Weight (kg)', 'Age', 'Experience_Level']]

    prediction = model.predict(X)[0]

    return jsonify({'predicted_workout_type': prediction})

import joblib
import numpy as np

# Load model, scaler, and label encoder once
loaded_model = joblib.load("./models/bmi/bmi_model.pkl")
loaded_scaler = joblib.load("./models/bmi/bmi_scaler.pkl")
label_encoder = joblib.load("./models/bmi/bmi_label_encoder.pkl")  # Load label encoder

def predict_bmi(data):
    features = np.array([[data['Weight'], data['Height'], data['Experience_Level'], data['Gender_Male']]])
    scaled_features = loaded_scaler.transform(features)
    pred_encoded = loaded_model.predict(scaled_features)[0]
    pred_label = label_encoder.inverse_transform([pred_encoded])[0]  # Decode label using encoder
    return {'BMI_Class': pred_label}

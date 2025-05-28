
import joblib
import pandas as pd

# Load the model and label map
model = joblib.load('./models/experience-level/experience_level_model.joblib')
label_map = joblib.load('./models/experience-level/experience_level_map.joblib')
selected_features = joblib.load('./models/experience-level/selected_features_experience_level.joblib')

def predict_experience_level(data_json):
    try:
        # Convert JSON to DataFrame using selected features
        input_df = pd.DataFrame([data_json], columns=selected_features)

        # Predict class index
        class_index = model.predict(input_df)[0]

        # Map to label
        label = label_map[int(class_index)]
        return {'Predicted Experience Level': label}
    except Exception as e:
        return {'error': str(e)}

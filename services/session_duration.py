import joblib
import numpy as np

# Load the trained model once (recommended at app startup)
duration_model = joblib.load('./models/session-duration/duration.pkl')

# Define the expected feature order
expected_features = ['Age', 'Avg_BPM', 'Calories_Burned', 'Fat_Percentage', 'Gender_Male', 'Experience_Level_original']

def predict_session_duration(data):
    try:
        # Validate and extract features
        features = [data[feat] for feat in expected_features]

        # Reshape for prediction
        features_array = np.array(features).reshape(1, -1)

        # Predict session duration
        prediction = duration_model.predict(features_array)[0]

        # Convert prediction to hours and minutes
        hours = int(prediction)
        minutes = int(round((prediction - hours) * 60))

        return {
            'hours': hours,
            'minutes': minutes
        }

    except KeyError as e:
        return {'error': f'Missing required feature: {str(e)}'}
    except Exception as e:
        return {'error': str(e)}

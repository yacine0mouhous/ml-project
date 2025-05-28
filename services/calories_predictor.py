import joblib
import numpy as np

# Load the trained model
model = joblib.load('./models/calories-burn/calories_bruned_model.pkl')

# Get the required feature names in correct order
model_features = model.feature_names_in_

def predict(data: dict):
    try:
        # Extract and order features as expected by the model
        features = [data[feat] for feat in model_features]

        # Convert to numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)

        # Make prediction
        prediction_log = model.predict(features_array)



        return {'Calories_Burned': float(prediction_log[0])}

    except KeyError as e:
        return {'error': f'Missing required feature: {str(e)}'}
    except Exception as e:
        return {'error': str(e)}

from flask import Flask, request, jsonify
from services import calories_predictor
from services import frequency_suggestion, session_duration, workout_type

app = Flask(__name__)

@app.route('/')
def home():
    return 'Fitness Recommender API is live!'

@app.route('/predict/workout-type', methods=['POST'])
def predict_workout_type():
    try:
        data = request.get_json()
        result = workout_type.predict(data)  # Assuming workout_type.predict is your function
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/predict/calories', methods=['POST'])
def predict_calories():
    try:
        data = request.get_json()
        result = calories_predictor.predict(data)  # Assuming calories_predictor.predict is your function
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to suggest Workout Frequency
@app.route('/predict/suggest_frequency', methods=['POST'])
def suggest_frequency():
    try:
        data = request.json
        result = frequency_suggestion.predict_workout_frequency(data)  # Assuming this function is correctly implemented
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to predict Session Duration
@app.route('/predict/session_duration', methods=['POST'])
def predict_duration():
    try:
        data = request.json
        result = session_duration.predict_session_duration(data)  # Assuming session_duration.predict_session_duration is your function
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

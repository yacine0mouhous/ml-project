from flask import Flask, request, jsonify
from services import calories_predictor
from services import  frequency_suggestion, session_duration,workout_type

app = Flask(__name__)

@app.route('/')
def home():
    return 'Fitness Recommender API is live!'


@app.route('/predict/workout-type', methods=['POST'])
def predict_workout_type():
    try:
        data = request.get_json()
        result = workout_type.predict(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

@app.route('/predict/calories', methods=['POST'])
def predict_calories():
    try:
        data = request.get_json()
        result = calories_predictor.predict(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400    
# Endpoint to suggest Workout Frequency
@app.route('/suggest_frequency', methods=['POST'])
def suggest_frequency():
    data = request.json
    result = frequency_suggestion.suggest_workout_frequency(data)
    return jsonify(result)

# Endpoint to predict Session Duration
@app.route('/predict_session_duration', methods=['POST'])
def predict_duration():
    data = request.json
    result = session_duration.predict_session_duration(data)
    return jsonify(result)    


if __name__ == '__main__':
    app.run(debug=True)

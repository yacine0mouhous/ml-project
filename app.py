from flask import Flask, request, jsonify
from services import calories_predictor
from services import frequency_suggestion, session_duration, workout_type
from services import experience_level
from services import bmi, fat, workout_type

"""
To run the server:
1. pip install flask numpy pandas joblib
2. Run the server: python app.py
"""

app = Flask(__name__)

@app.route('/')
def home():
    return 'Fitness Recommender API is live!'


# Endpoint to predict Workout Type
"""
Endpoint: POST /predict/workout-type
Request Body Example:
{
    "Goal": "Lose weight",
    "Height (m)": 175,
    "Weight (kg)": 73,
    "Age": 20,
    "Experience_Level": 1
}
goals : 
Improve cardiovascular health
Lose weight
Build muscle
Improve flexibility and balance


Description:
Predicts the most suitable workout type based on user goals and physical attributes.
The 'Goal' field must be one of the encoded categories used during training.
Returns the predicted workout type as a string.
"""
@app.route('/predict/workout-type', methods=['POST'])
def predict_workout():
    return workout_type.predict_workout_controller()


# Endpoint to predict Calories Burned
"""
Endpoint: POST /predict/calories-burn
Request Body Example:
{
    "Height (m)": 1.79,
    "Avg_BPM": 180,
    "Session_Duration (hours)": 1.5,
    "Gender_Male": 1,
    "Workout_Type_Code": 1
}

Explanation:
- Gender_Male: 1 if male, 0 if female
- Workout_Type_Code:
  0: Cardio
  1: HIIT
  2: Strength (High-Intensity Interval Training)
  3: Yoga
  Other workout types as coded in training

Returns predicted calories burned during the session.
"""
@app.route('/predict/calories-burn', methods=['POST'])
def predict_calories():
    try:
        data = request.get_json()
        result = calories_predictor.predict(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Endpoint to suggest Workout Frequency
"""
Endpoint: POST /predict/suggest_frequency
Request Body Example:
{
    "Weight (kg)": 70,
    "Session_Duration (hours)": 1.5,
    "Fat_Percentage": 18,
    "Experience_Level": 2,
    "BMI": 22.5
}

Explanation:
- Session_Duration: Duration of the workout session in hours (input from user)
- Experience_Level:
  1 - Beginner: New to working out; limited experience
  2 - Intermediate: Consistent workout experience
  3 - Advanced: Highly experienced, follows structured routines

Returns suggested workout frequency per week.
"""
@app.route('/predict/suggest_frequency', methods=['POST'])
def suggest_frequency():
    try:
        data = request.json
        result = frequency_suggestion.predict_workout_frequency(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Endpoint to predict Session Duration
"""
Endpoint: POST /predict/session_duration
Request Body Example:
{
    "Age": 22,
    "Avg_BPM": 160,
    "Calories_Burned": 700,
    "Fat_Percentage": 15,
    "Gender_Male": 1,
    "Experience_Level_original": 1
}

Explanation:
- Calories_Burned: Target calories to burn in the session
- Experience_Level_original:
  1 - Beginner
  2 - Intermediate
  3 - Advanced

Returns the predicted recommended session duration.
"""
@app.route('/predict/session_duration', methods=['POST'])
def predict_session_duration():
    try:
        data = request.get_json()
        result = session_duration.predict_session_duration(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Endpoint to predict Experience Level
"""
Endpoint: POST /predict/experience_level
Request Body Example:
{
  "Session_Duration (hours)": 1.5,
  "Calories_Burned": 500,
  "Fat_Percentage": 17,
  "Water_Intake (liters)": 2.0,
  "Workout_Frequency (days/week)": 4
}


Description:
Predicts the user's experience level based on physical and workout features.
Returns experience level as Beginner, Intermediate, or Advanced.
"""
@app.route('/predict/experience_level', methods=['POST'])
def predict_level():
    try:
        data = request.get_json()
        result = experience_level.predict_experience_level(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Endpoint to predict BMI
"""
Endpoint: POST /predict/bmi
Request Body Example:
{
    "Weight": 90,
    "Height": 1.9,
    "Experience_Level": 2,
    "Gender_Male": 0
}

Experience_Level:
Beginner: 1
Intermediate: 2
Advanced: 3

Description:
Calculates Body Mass Index (BMI) based on weight and height.
Returns the BMI value and possibly classification.
"""
@app.route('/predict/bmi', methods=['POST'])
def predict_bmi_route():
    try:
        data = request.get_json()
        result = bmi.predict_bmi(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Endpoint to predict Fat Percentage
"""
Endpoint: POST /predict/fat
Request Body Example:

{
  "Session_Duration (hours)": 1.2,
  "Calories_Burned": 800.0,
  "Water_Intake (liters)": 2.5,
  "Workout_Frequency (days/week)": 4.0,
  "Experience_Level": 2.0, 
  "Gender_Male": 1.0
}
Experience_Level:
Beginner: 1
Intermediate: 2
Advanced: 3

Description:
Predicts body fat percentage based on user physical data and experience.
Returns the predicted fat percentage.
"""
@app.route('/predict/fat', methods=['POST'])
def predict_fat():
    try:
        data = request.json
        result = fat.predict_fat_percentage(data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)

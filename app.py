from flask import Flask, request, jsonify
from services import calories_predictor
from services import frequency_suggestion, session_duration, workout_type


""""
 to run the server install flask  using (pip install flask)
 and then run the server using ( python app.py)

"""



app = Flask(__name__)

@app.route('/')
def home():
    return 'Fitness Recommender API is live!'
# Endpoint to predict Workout Type
"""
endpoint : http://127.0.0.1:5000/predict/workout-type
Post request body exemple :


"""
@app.route('/predict/workout-type', methods=['POST'])
def predict_workout_type():
    try:
        data = request.get_json()
        result = workout_type.predict(data)  # Assuming workout_type.predict is your function
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    




# Endpoint to predict Calories Burned
"""
endpoint : http://127.0.0.1:5000/predict/calories-burn
Post request body exemple : 
   {
        'Height (m)': 1.79,
        'Avg_BPM': 180,
        'Session_Duration (hours)': 1.5,
        'Gender_Male': 1,
        'Workout_Type_Code': 1
    },
explanation : 
gender_male : 1 if male 0 if women 
workout_type_code:
Cardio  : 0 
HIIT    :    1 
Strength ( High-Intensity Interval Training)  :  2 
Yoga :   3 
all others are input from users

"""
@app.route('/predict/calories-burn', methods=['POST'])
def predict_calories():
    try:
        data = request.get_json()
        result = calories_predictor.predict(data)  # Assuming calories_predictor.predict is your function
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    


"""
endpoint : http://127.0.0.1:5000/predict/suggest_frequency
Post request body exemple :
  {
    "Weight (kg)": 70,
    "Session_Duration (hours)": 1.5,
    "Fat_Percentage": 18,
    "Experience_Level": 2,
    "BMI": 22.5
  },
explanation :
session-duration : duration of the session in hours (input from user of how many hours they want to work out)
experience-level  :
Level	Name	Description
1	Beginner	New to working out; limited experience with exercises and routines.
2	Intermediate	Has consistent workout experience; understands form and various exercises.
3	Advanced	Highly experienced; follows structured routines and handles high intensity.
all others are input from users 

"""
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
"""
endpoint : http://127.0.0.1:5000/predict/session_duration
Post request body exemple :
    {
        'Age': 22,
        'Avg_BPM': 160,
        'Calories_Burned': 700,
        'Fat_Percentage': 15,
        'Gender_Male': 1,
        'Experience_Level_original': 1
    },
    explanation :
calories_burned : calories burned target for the session
experience-level-original  :
Level	Name	Description
1	Beginner	New to working out; limited experience with exercises and routines.
2	Intermediate	Has consistent workout experience; understands form and various exercises.
3	Advanced	Highly experienced; follows structured routines and handles high intensity.
all others are input from users 
"""
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

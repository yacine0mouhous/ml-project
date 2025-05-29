# Fitness Recommender API

## Overview

This API provides personalized fitness and health recommendations using multiple machine learning models trained on user data. It supports predictions including workout type, calories burned, workout frequency, session duration, experience level, BMI, and body fat percentage.

---

## Model Performance Summary

| Model               | Training Score / Accuracy | Testing Score / Accuracy | Cross-Validation Score / Accuracy        | Notes                   |
|---------------------|---------------------------|--------------------------|------------------------------------------|-------------------------|
| Calories Predictor   | R²: 0.9935, MAE: 17.74    | R²: 0.9528, MAE: 51.83   | R² CV (5 folds): 0.9526                   | Regression              |
| Frequency Suggestion | R²: 0.7441, MAE: 0.4457   | R²: 0.7141, MAE: 0.5063  | R² CV (5 folds mean): 0.6738              | Regression              |
| Session Duration     | R²: 0.9713, MAE: 0.0440   | R²: 0.9566, MAE: 0.0606  | R² CV (5 folds mean): 0.9525 ± 0.0080    | Regression              |
| Workout Type         | Accuracy: 92.54%           | Accuracy: 86.67%         | —                                        | Classification          |
| Experience Level     | Accuracy: 90.95%           | Accuracy: 91.39%         | CV Accuracy (5 folds): 89.93% ± 2.45%    | Classification          |
| BMI                 | Accuracy: 94.51%           | Accuracy: 95.90%         | CV Accuracy (5 folds): 94.66%             | Classification          |
| Fat Percentage       | R²: 0.8207, RMSE: 7.02    | R²: 0.8059, RMSE: 7.59   | R² CV (5 folds): 0.7977 ± 0.0298          | Regression              |

---

## API Endpoints Documentation

### 1. Home Route

- **URL:** `/`  
- **Method:** `GET`  
- **Description:** API health check. Returns a simple confirmation message.

---

### 2. Predict Workout Type

- **URL:** `/predict/workout-type`  
- **Method:** `POST`  
- **Input Example:**

```json
{
  "Goal": "Lose weight",
  "Height (m)": 1.75,
  "Weight (kg)": 73,
  "Age": 20,
  "Experience_Level": 1
}
```

- **Input Description:**  
  - `Goal`: User's fitness goal. One of:  
    - "Improve cardiovascular health"  
    - "Lose weight"  
    - "Build muscle"  
    - "Improve flexibility and balance"  
  - `Height (m)`: Height in meters (e.g., 1.75)  
  - `Weight (kg)`: Weight in kilograms  
  - `Age`: Age in years  
  - `Experience_Level`: Encoded as integer (1: Beginner, 2: Intermediate, 3: Advanced)

- **Output:** Predicted workout type best suited for the user.

---

### 3. Predict Calories Burned

- **URL:** `/predict/calories-burn`  
- **Method:** `POST`  
- **Input Example:**

```json
{
  "Height (m)": 1.79,
  "Avg_BPM": 180,
  "Session_Duration (hours)": 1.5,
  "Gender_Male": 1,
  "Workout_Type_Code": 1
}
```

- **Input Description:**  
  - `Height (m)`: Height in meters  
  - `Avg_BPM`: Average heart beats per minute during workout  
  - `Session_Duration (hours)`: Workout duration in hours  
  - `Gender_Male`: 1 for male, 0 for female  
  - `Workout_Type_Code`: Encoded workout type (e.g., 0=Cardio, 1=HIIT, 2=Strength, 3=Yoga)

- **Output:** Predicted calories burned.

---

### 4. Suggest Workout Frequency

- **URL:** `/predict/suggest_frequency`  
- **Method:** `POST`  
- **Input Example:**

```json
{
  "Weight (kg)": 70,
  "Session_Duration (hours)": 1.5,
  "Fat_Percentage": 18,
  "Experience_Level": 2,
  "BMI": 22.5
}
```

- **Input Description:**  
  - `Weight (kg)`: User’s weight  
  - `Session_Duration (hours)`: Duration of workout session  
  - `Fat_Percentage`: Body fat percentage  
  - `Experience_Level`: 1 (Beginner), 2 (Intermediate), 3 (Advanced)  
  - `BMI`: Body Mass Index

- **Output:** Recommended number of workout sessions per week.

---

### 5. Predict Session Duration

- **URL:** `/predict/session_duration`  
- **Method:** `POST`  
- **Input Example:**

```json
{
  "Age": 22,
  "Avg_BPM": 160,
  "Calories_Burned": 700,
  "Fat_Percentage": 15,
  "Gender_Male": 1,
  "Experience_Level_original": 1
}
```

- **Input Description:**  
  - `Age`: Age in years  
  - `Avg_BPM`: Average heart rate during workout  
  - `Calories_Burned`: Calories target for session  
  - `Fat_Percentage`: Body fat percentage  
  - `Gender_Male`: 1 for male, 0 for female  
  - `Experience_Level_original`: 1=Beginner, 2=Intermediate, 3=Advanced

- **Output:** Suggested session duration.

---

### 6. Predict Experience Level

- **URL:** `/predict/experience_level`  
- **Method:** `POST`  
- **Input Example:**

```json
{
  "Session_Duration (hours)": 1.5,
  "Calories_Burned": 500,
  "Fat_Percentage": 17,
  "Water_Intake (liters)": 2.0,
  "Workout_Frequency (days/week)": 4
}
```

- **Input Description:**  
  - `Session_Duration (hours)`: Length of workout session  
  - `Calories_Burned`: Calories burned per session  
  - `Fat_Percentage`: Body fat percentage  
  - `Water_Intake (liters)`: Daily water intake  
  - `Workout_Frequency (days/week)`: Number of sessions per week

- **Output:** Predicted experience level category.

---

### 7. Predict BMI

- **URL:** `/predict/bmi`  
- **Method:** `POST`  
- **Input Example:**

```json
{
  "Weight": 90,
  "Height": 1.9,
  "Experience_Level": 2,
  "Gender_Male": 0
}
```

- **Input Description:**  
  - `Weight`: Weight in kilograms  
  - `Height`: Height in meters  
  - `Experience_Level`: 1=Beginner, 2=Intermediate, 3=Advanced  
  - `Gender_Male`: 1=Male, 0=Female

- **Output:** Predicted BMI value.

---

### 8. Predict Fat Percentage

- **URL:** `/predict/fat`  
- **Method:** `POST`  
- **Input Example:**

```json
{
  "Session_Duration (hours)": 1.2,
  "Calories_Burned": 800.0,
  "Water_Intake (liters)": 2.5,
  "Workout_Frequency (days/week)": 4.0,
  "Experience_Level": 2.0,
  "Gender_Male": 1.0
}
```

- **Input Description:**  
  - `Session_Duration (hours)`: Duration of workout session  
  - `Calories_Burned`: Calories burned  
  - `Water_Intake (liters)`: Daily water intake  
  - `Workout_Frequency (days/week)`: Sessions per week  
  - `Experience_Level`: 1=Beginner, 2=Intermediate, 3=Advanced  
  - `Gender_Male`: 1=Male, 0=Female

- **Output:** Predicted body fat percentage.

---

## Usage Notes

- All POST requests expect a JSON body matching the input examples above.  
- Outputs are JSON responses with predicted values or classifications.  
- Feature encodings (like `Experience_Level` or `Workout_Type_Code`) should match the documented values for correct predictions.

---
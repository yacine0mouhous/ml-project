
# 🏋️‍♂️ Fitness Recommender API

## 🚀 Overview

The **Fitness Recommender API** provides smart, personalized fitness and health recommendations using advanced machine learning models trained on user data. It supports predictions for:

✅ Workout Type  
🔥 Calories Burned  
📅 Workout Frequency  
⏱️ Session Duration  
🎯 Experience Level  
📊 BMI  
💪 Body Fat Percentage

---

## 📈 Model Performance Summary

| 🧠 Model              | 🏋️ Training Score / Accuracy | 🧪 Testing Score / Accuracy | 🔁 Cross-Validation Score / Accuracy | 📌 Notes          |
|----------------------|------------------------------|-----------------------------|-------------------------------------|-------------------|
| **Calories Predictor**   | R²: 0.9935, MAE: 17.74       | R²: 0.9528, MAE: 51.83      | R² CV (5 folds): 0.9526              | 🔢 Regression     |
| **Frequency Suggestion** | R²: 0.7441, MAE: 0.4457      | R²: 0.7141, MAE: 0.5063     | R² CV (5 folds): 0.6738              | 🔢 Regression     |
| **Session Duration**     | R²: 0.9713, MAE: 0.0440      | R²: 0.9566, MAE: 0.0606     | R² CV (5 folds): 0.9525 ± 0.0080     | 🔢 Regression     |
| **Workout Type**         | Accuracy: 92.54%             | Accuracy: 86.67%            | —                                    | 🧩 Classification |
| **Experience Level**     | Accuracy: 90.95%             | Accuracy: 91.39%            | CV: 89.93% ± 2.45%                    | 🧩 Classification |
| **BMI**                  | Accuracy: 94.51%             | Accuracy: 95.90%            | CV: 94.66%                            | 🧩 Classification |
| **Fat Percentage**       | R²: 0.8207, RMSE: 7.02       | R²: 0.8059, RMSE: 7.59      | R² CV: 0.7977 ± 0.0298                | 🔢 Regression     |

---

## 📚 API Endpoints

### 🏠 1. Home Route
- **URL:** `/`
- **Method:** `GET`
- **Description:** Health check — confirms that the API is running.

---

### 🧠 2. Predict Workout Type

- **URL:** `/predict/workout-type`  
- **Method:** `POST`  
- **Input:**
```json
{
  "Goal": "Lose weight",
  "Height (m)": 1.75,
  "Weight (kg)": 73,
  "Age": 20,
  "Experience_Level": 1
}
```
- **Output:** Suggested workout type (e.g., Cardio, Strength, HIIT)

---

### 🔥 3. Predict Calories Burned

- **URL:** `/predict/calories-burn`  
- **Method:** `POST`  
- **Input:**
```json
{
  "Height (m)": 1.79,
  "Avg_BPM": 180,
  "Session_Duration (hours)": 1.5,
  "Gender_Male": 1,
  "Workout_Type_Code": 1
}
```
- **Output:** Estimated calories burned.

---

### 📅 4. Suggest Workout Frequency

- **URL:** `/predict/suggest_frequency`  
- **Method:** `POST`  
- **Input:**
```json
{
  "Weight (kg)": 70,
  "Session_Duration (hours)": 1.5,
  "Fat_Percentage": 18,
  "Experience_Level": 2,
  "BMI": 22.5
}
```
- **Output:** Recommended workouts per week.

---

### ⏱️ 5. Predict Session Duration

- **URL:** `/predict/session_duration`  
- **Method:** `POST`  
- **Input:**
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
- **Output:** Estimated session duration.

---

### 🎯 6. Predict Experience Level

- **URL:** `/predict/experience_level`  
- **Method:** `POST`  
- **Input:**
```json
{
  "Session_Duration (hours)": 1.5,
  "Calories_Burned": 500,
  "Fat_Percentage": 17,
  "Water_Intake (liters)": 2.0,
  "Workout_Frequency (days/week)": 4
}
```
- **Output:** Predicted fitness experience level.

---

### 📊 7. Predict BMI

- **URL:** `/predict/bmi`  
- **Method:** `POST`  
- **Input:**
```json
{
  "Weight": 90,
  "Height": 1.9,
  "Experience_Level": 2,
  "Gender_Male": 0
}
```
- **Output:** Predicted BMI classification.

---

### 💪 8. Predict Fat Percentage

- **URL:** `/predict/fat`  
- **Method:** `POST`  
- **Input:**
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
- **Output:** Estimated body fat percentage.

---

## 🛠️ Usage Notes

- All endpoints use `POST` requests (except `/`).
- Inputs must follow the documented schema.
- Fields like `Experience_Level`, `Workout_Type_Code`, and `Gender_Male` must use correct encoded values.
- Output is returned in JSON format.

---

## 📬 Contact

For questions, issues, or suggestions, feel free to reach out or open an issue. Happy training! 💥

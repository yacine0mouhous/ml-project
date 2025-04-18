# Basic packages
import pandas as pd
import numpy as np

# Data Preprocessing
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# Evaluation
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset into a DataFrame
df = pd.read_csv('./data/data.csv')
# Handle missing values if any
df = df.dropna()  # Or fill missing values: df.fillna(df.mean(), inplace=True)

# Encoding categorical columns (like 'Workout_Type' and 'Experience_Level')
label_encoders = {}
for col in ['Workout_Type', 'Experience_Level']:  # Adjust column names as needed
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Save encoder for later if necessary
    # Encode categorical columns using LabelEncoder


# Features (X) and Target (y)
X = df[['Workout_Type', 'Session_Duration (hours)', 'Max_BPM', 'Avg_BPM', 'Age', 'Weight (kg)', 'Experience_Level']]
y = df['Calories_Burned']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (important for models like Gradient Boosting, Linear Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
from sklearn.model_selection import train_test_split

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.preprocessing import StandardScaler

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor

# Linear Regression
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

# Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# XGBoost Regressor
xgb = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)

# LightGBM Regressor
lgb = LGBMRegressor(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42)
lgb.fit(X_train, y_train)
y_pred_lgb = lgb.predict(X_test)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mae, mse, r2

# Evaluating each model
mae_lr, mse_lr, r2_lr = evaluate_model(y_test, y_pred_lr)
print(f"Linear Regression - MAE: {mae_lr:.4f}, MSE: {mse_lr:.4f}, R2: {r2_lr:.4f}")

mae_rf, mse_rf, r2_rf = evaluate_model(y_test, y_pred_rf)
print(f"Random Forest - MAE: {mae_rf:.4f}, MSE: {mse_rf:.4f}, R2: {r2_rf:.4f}")

mae_xgb, mse_xgb, r2_xgb = evaluate_model(y_test, y_pred_xgb)
print(f"XGBoost - MAE: {mae_xgb:.4f}, MSE: {mse_xgb:.4f}, R2: {r2_xgb:.4f}")

mae_lgb, mse_lgb, r2_lgb = evaluate_model(y_test, y_pred_lgb)
print(f"LightGBM - MAE: {mae_lgb:.4f}, MSE: {mse_lgb:.4f}, R2: {r2_lgb:.4f}")
import joblib
import os



# Save the best model (choose the best one; here using Random Forest as an example)
joblib.dump(rf, "./models/calories_burn/calories_model.pkl")

# Save the scaler
joblib.dump(scaler, "./models/calories_burn/calories_scaler.pkl")

# Save label encoders (for Workout_Type and Experience_Level)
joblib.dump(label_encoders, "./models/calories_burn/calories_label_encoders.pkl")

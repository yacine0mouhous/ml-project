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

# Display the first 5 rows of the DataFrame
print(df.head())
print(df.info)
label_encoders = {}
for col in ['Gender', 'Experience_Level', 'Workout_Type']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
    # Rename the column
df.rename(columns={'Workout_Frequency (days/week)': 'Workout_Frequency'}, inplace=True)

# Check the column names to confirm the change
print(df.columns)


print(df.columns)

"""
X = df[['Age', 'Gender', 'BMI', 'Fat_Percentage', 'Max_BPM', 'Avg_BPM', 'Experience_Level', 'Workout_Frequency']]
y = df['Workout_Type']"""
# Define features (X) and target (y)
X = df[['Age', 'Gender', 'BMI', 'Fat_Percentage', 'Max_BPM', 'Avg_BPM', 'Experience_Level', 'Workout_Frequency']]
y = df['Workout_Type']
# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
# Feature Scaling: Standardize numerical values
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Logistic Regression (Baseline Model)
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

# Print classification report for Logistic Regression
print("Logistic Regression:\n")
print(classification_report(y_test, y_pred_lr))
# Evaluate accuracy for each model
accuracy_lr = accuracy_score(y_test, y_pred_lr)
import joblib
import os

# Create a models directory if it doesn't exist
os.makedirs('./models', exist_ok=True)

# Save the trained model
joblib.dump(lr, './models/workout_type_model.pkl')

# Save the scaler
joblib.dump(scaler, './models/workout_type_scaler.pkl')

# Save label encoders
joblib.dump(label_encoders, './models/workout_type_label_encoders.pkl')

print("Model, scaler, and label encoders saved successfully.")




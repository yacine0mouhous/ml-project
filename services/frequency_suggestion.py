# Mock function for workout frequency suggestion
def suggest_workout_frequency(data):
    # Simulating a prediction for frequency based on mock logic
    if data['Experience_Level'] == 1:
        return 3
    elif data['Experience_Level'] == 2:
        return 4
    else:
        return 5

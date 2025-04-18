# Mock function for session duration prediction
def predict_session_duration(data):
    # Simulating a prediction based on some basic logic
    if data['Experience_Level'] == 1:
        return {'Session_Duration': 45}  # Beginner level
    elif data['Experience_Level'] == 2:
        return {'Session_Duration': 60}  # Intermediate level
    else:
        return {'Session_Duration': 90}  # Advanced level

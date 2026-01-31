import joblib
import pandas as pd

# Load trained model
model = joblib.load("student_score_model.pkl")

# New student data (sample of one student)
student = pd.DataFrame([{
    "study_hours": 8,
    "attendance": 85,
    "prev_grade": 78,
    "sleep_hours": 7,
    "practice": 4
}])

# Make prediction
prediction = model.predict(student)
# predicted final score
print("Predicted Final Score:", round(prediction[0], 2))

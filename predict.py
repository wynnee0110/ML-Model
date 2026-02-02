import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/binary_model_V1.pkl")

# New student data (sample of one student)
student = pd.DataFrame([{
    "study_hours": 4,
    "attendance": 100,
    "prev_grade": 75,
    "sleep_hours": 3,
    "practice": 3
}])

# Make prediction
prediction = model.predict(student)
# predicted final score
print("Predicted Final Score:", round(prediction[0], 2))

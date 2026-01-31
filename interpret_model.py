import joblib
import pandas as pd

# Load trained model
model = joblib.load("student_score_model.pkl")

# Feature names (same order as training)
features = [
    "study_hours",
    "attendance",
    "prev_grade",
    "sleep_hours",
    "practice"
]

# Create table of coefficients
coefficients = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_
})

print(coefficients)
print("\nIntercept (bias):", model.intercept_)

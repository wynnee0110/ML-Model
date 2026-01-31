import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load data
data = pd.read_csv("data/data.csv")

# Separate features and target
X = data.drop("final_score", axis=1)
y = data["final_score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error (MAE):", round(mae, 2))
print("R² Score:", round(r2, 2))

# Save the trained model
joblib.dump(model, "student_score_model.pkl")
print("Model saved as student_score_model.pkl")

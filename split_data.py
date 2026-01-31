import pandas as pd
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv("data/data.csv")

# Separate features and target
X = data.drop("final_score", axis=1)
y = data["final_score"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

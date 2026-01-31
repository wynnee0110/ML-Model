
import pandas as pd

# Load data
data = pd.read_csv("data/data.csv")

# Separate features and target
X = data.drop("final_score", axis=1)
y = data["final_score"]

# print features and target
print("FEATURES (X):")
print(X.head())

print("\nTARGET (y):")
print(y.head())

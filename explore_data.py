import pandas as pd

# Load data 
data = pd.read_csv("data/data.csv")
# print first 10 rows of the dataset
print("FIRST 10 ROWS:")
print(data.head(10))

# prints data info and statistical summary
print("\nDATA INFO:")
print(data.info())

print("\nSTATISTICAL SUMMARY:")
print(data.describe())


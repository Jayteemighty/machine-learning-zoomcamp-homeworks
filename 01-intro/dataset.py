import pandas as pd

# Load the dataset
url = "https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv"
df = pd.read_csv(url)

# Check the number of records (rows)
num_records = len(df)
print(f"The dataset contains {num_records} records")

# You can also use shape to see both rows and columns
print(f"Dataset shape: {df.shape} (rows, columns)")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

print("\nFirst few rows of the dataset:")
print(df.head())
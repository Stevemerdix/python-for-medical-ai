import pandas as pd

df = pd.read_csv("data/healthcare_dataset.csv")

print(df.head())
import pandas as pd

df = pd.read_csv("data/healthcare_dataset.csv")

print(df.head())

# -------------------------
# BASIC ANALYSIS
# -------------------------

print("\n--- Column Info ---")
print(df.info())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Age Statistics ---")
print(df["Age"].describe())

print("\n--- Test Results Count ---")
print(df["Test Results"].value_counts())
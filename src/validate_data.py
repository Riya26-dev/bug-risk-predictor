import pandas as pd

df = pd.read_csv("data/commits.csv")

print("Total commits:", len(df))

print("\nMissing values:\n", df.isnull().sum())

print("\nDuplicate commits:", df.duplicated().sum())

print("\nColumns:", df.columns.tolist())
import pandas as pd

# Load dataset
df = pd.read_csv("data/commits.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows: {duplicates}")

df.drop_duplicates(inplace=True)

print(f"Shape after removing duplicates: {df.shape}")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], utc=True)

print("\nUpdated Data Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("data/cleaned_commits.csv", index=False)

print("\n✅ cleaned_commits.csv created successfully!")
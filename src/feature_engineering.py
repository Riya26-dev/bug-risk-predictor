import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load cleaned dataset
df = pd.read_csv("data/cleaned_commits.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------
# Feature 1: Commit Size
# -----------------------------
df["commit_size"] = df["lines_added"] + df["lines_deleted"]

# -----------------------------
# Feature 2: Message Length
# -----------------------------
df["message_length"] = df["message"].astype(str).apply(len)

# -----------------------------
# Feature 3: Risk Label
# -----------------------------
keywords = [
    "fix",
    "bug",
    "patch",
    "hotfix",
    "issue",
    "error",
    "resolve"
]

df["risk"] = df["message"].str.lower().apply(
    lambda msg: 1 if any(word in msg for word in keywords) else 0
)

# -----------------------------
# Feature 4: Encode Author
# -----------------------------
encoder = LabelEncoder()
df["author"] = encoder.fit_transform(df["author"])

print("\nFeatures Created Successfully!")

print(df.head())

print("\nRisk Distribution:")
print(df["risk"].value_counts())

# Save processed dataset
df.to_csv("data/processed_commits.csv", index=False)

print("\nprocessed_commits.csv created successfully!")
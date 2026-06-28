import pandas as pd

df = pd.read_csv("data/commits.csv")

print("===== DATASET STATS =====")

print("Total commits:", len(df))
print("Total authors:", df['author'].nunique())

print("Average files changed:", df['files_changed'].mean())
print("Average lines added:", df['lines_added'].mean())
print("Average lines deleted:", df['lines_deleted'].mean())

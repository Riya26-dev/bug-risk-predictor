from pydriller import Repository
import pandas as pd
import os

REPO_PATH = "flask"

commit_data = []

print("Mining repository (FAST MODE)...")

count = 0

# LIMIT commits for demo (VERY IMPORTANT)
for commit in Repository(REPO_PATH).traverse_commits():

    count += 1

    # SAFETY LIMIT (prevents freezing)
    if count > 500:
        break

    files_changed = len(commit.modified_files)

    lines_added = commit.insertions
    lines_deleted = commit.deletions

    commit_data.append({
        "commit_hash": commit.hash,
        "author": commit.author.name,
        "date": commit.author_date,
        "message": commit.msg,
        "files_changed": files_changed,
        "lines_added": lines_added,
        "lines_deleted": lines_deleted
    })

    if count % 50 == 0:
        print(f"Processed {count} commits...")

print(f"Done! Total commits processed: {len(commit_data)}")

# Save CSV
os.makedirs("data", exist_ok=True)

df = pd.DataFrame(commit_data)
df.to_csv("data/commits.csv", index=False)

print("Saved: data/commits.csv")
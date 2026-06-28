import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/processed_commits.csv")

print("Dataset Loaded Successfully!")
print(df.head())

# -----------------------------
# Select Features
# -----------------------------
X = df[
    [
        "files_changed",
        "lines_added",
        "lines_deleted",
        "commit_size",
        "message_length",
        "author"
    ]
]

# Target
y = df["risk"]

# -----------------------------
# Feature Scaling
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Logistic Regression
# -----------------------------
lr = LogisticRegression()

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

# -----------------------------
# Random Forest
# -----------------------------
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# -----------------------------
# Evaluation Function
# -----------------------------
def evaluate(name, y_true, y_pred):

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print(f"\n{name}")
    print("-" * 30)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    return accuracy, precision, recall, f1

# -----------------------------
# Compare Models
# -----------------------------
lr_scores = evaluate("Logistic Regression", y_test, lr_pred)

rf_scores = evaluate("Random Forest", y_test, rf_pred)

# -----------------------------
# Select Best Model
# -----------------------------
if rf_scores[0] >= lr_scores[0]:
    best_model = rf
    best_name = "Random Forest"
    best_scores = rf_scores
else:
    best_model = lr
    best_name = "Logistic Regression"
    best_scores = lr_scores

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(best_model, "models/model.pkl")

print(f"\nBest Model Saved: {best_name}")

# -----------------------------
# Save Scaler
# -----------------------------
joblib.dump(scaler, "models/scaler.pkl")

print("Scaler Saved Successfully!")

# -----------------------------
# Write Report
# -----------------------------
with open("reports/model_report.txt", "w") as f:

    f.write("AI Code Review / Bug Risk Predictor\n")
    f.write("=" * 40 + "\n\n")

    f.write(f"Dataset Size : {len(df)}\n\n")

    f.write(f"Selected Model : {best_name}\n\n")

    f.write(f"Accuracy : {best_scores[0]:.4f}\n")
    f.write(f"Precision: {best_scores[1]:.4f}\n")
    f.write(f"Recall   : {best_scores[2]:.4f}\n")
    f.write(f"F1 Score : {best_scores[3]:.4f}\n")

print("\nModel Report Generated Successfully!")
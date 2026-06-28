import joblib
import numpy as np
import os

# -----------------------------
# Load Model and Scaler
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# -----------------------------
# Prediction Function
# -----------------------------

def predict_risk(files_changed,
                 lines_added,
                 lines_deleted,
                 commit_size,
                 message_length,
                 author_id):
    """
    Predict bug risk of a commit.

    Parameters
    ----------
    files_changed : int
    lines_added : int
    lines_deleted : int
    commit_size : int
    message_length : int
    author_id : int

    Returns
    -------
    risk : str
    probability : float
    """

    features = np.array([[
        files_changed,
        lines_added,
        lines_deleted,
        commit_size,
        message_length,
        author_id
    ]])

    # Scale features
    features = scaler.transform(features)

    # Predict class
    prediction = model.predict(features)[0]

    # Predict probability
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        risk = "HIGH RISK"
    else:
        risk = "LOW RISK"

    return risk, probability


# -----------------------------
# Test the Predictor
# -----------------------------

if __name__ == "__main__":

    risk, probability = predict_risk(
        files_changed=5,
        lines_added=120,
        lines_deleted=30,
        commit_size=150,
        message_length=25,
        author_id=2
    )

    print("\n==============================")
    print(" AI Bug Risk Prediction")
    print("==============================")
    print(f"Prediction : {risk}")
    print(f"Risk Score : {probability*100:.2f}%")
    print("==============================")
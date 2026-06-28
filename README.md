# 🔍 Bug Risk Predictor — AI Code Review Tool

An ML-powered tool that analyzes Git commit patterns
and predicts which commits are likely to introduce bugs.

---

## ✨ Features
- ✅ Mines real Git commit history
- ✅ Feature engineering on commit metadata
- ✅ Logistic Regression + Random Forest ML models
- ✅ Predicts HIGH / LOW bug risk
- ✅ AI-generated code review comments
- ✅ GitHub Actions CI/CD pipeline
- ✅ Unit tested

---

## 🛠️ Tech Stack
Python | Pandas | Scikit-learn | GitHub Actions | Joblib

---

## 📁 Project Structure

bug-risk-predictor/
├── data/
│   ├── commits.csv
│   └── processed_commits.csv
├── models/
│   ├── model.pkl
│   └── scaler.pkl
├── src/
│   ├── mine_repo.py
│   ├── preprocess.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── predictor.py
│   └── comment_generator.py
├── tests/
│   └── test_predictor.py
├── .github/
│   └── workflows/
│       └── bug-risk.yml
├── reports/
├── README.md
└── requirements.txt

---

## 🚀 How to Run

git clone https://github.com/Riya26-dev/bug-risk-predictor.git
cd bug-risk-predictor
pip install -r requirements.txt
python src/train_model.py
python src/predictor.py

---

## 📊 How It Works

Git Commits
    ↓
Feature Engineering
    ↓
ML Model Training (Logistic Regression / Random Forest)
    ↓
Bug Risk Prediction (HIGH / LOW)
    ↓
AI Review Comment Generated

---

## 🤖 CI/CD Pipeline

Every push triggers GitHub Actions which:
- Installs dependencies
- Trains the ML model
- Runs unit tests automatically

---

## 👥 Team Contributions

| Member | Role | Work Done |
|--------|------|-----------|
| Person 1 | Data Engineer | Git mining, commits.csv |
| Person 2 | ML Engineer | Preprocessing, model training |
| Person 3 | Backend Dev | Flask app, predictor API |
| Person 4 | DevOps & QA | CI/CD, testing, documentation |

---

## 🔮 Future Scope
- CodeBERT for semantic code analysis
- XGBoost model for better accuracy
- SHAP for model explainability
- FastAPI backend
- Dashboard for visualization
# 🛡️ CyberSieve: AI-Powered Two-Stage Spam & Phishing Threat Detector

CyberSieve is a robust machine learning-based security pipeline designed to detect deceptive SMS spam messages and malicious web links (phishing URLs) in real time.

## 🚀 Project Architecture
The system uses a **Two-Stage Pipeline**:
1. **Stage 1 (Spam Classification):** Analyzes text semantics using **TF-IDF Vectorization** and a trained **Linear SVM** model (trained on SMS datasets with ~94% F1-score).
2. **Stage 2 (Phishing URL Analysis):** Extracts structural URL properties (such as domain length, IP presence, HTTPS validity, and subdomains) and evaluates them via a **Random Forest** classifier (~97% F1-score).

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3.11+
- **Machine Learning:** Scikit-Learn, Pandas, NumPy, NLTK, Joblib
- **Frontend / UI:** Streamlit

## 📂 Project Structure
```text
spam-phishing-detector/
├── data/                  # Dataset storage (spam.csv, PhishingData.csv)
├── models/                # Saved model checkpoints (.pkl files)
├── notebooks/             # Exploratory Data Analysis & training notebooks
├── src/                   # Core preprocessing, feature extraction, and pipeline logic
├── app.py                 # Interactive Streamlit Web App
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
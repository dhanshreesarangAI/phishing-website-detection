# 🛡️ Phishing Website Detection - Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-1.4-orange?logo=scikit-learn)
![Accuracy](https://img.shields.io/badge/Accuracy-95.58%25-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow)

> A complete end-to-end Machine Learning project to detect phishing websites using URL and domain features. Built as part of a **Data Science & Analytics Internship**.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Tasks Completed](#-tasks-completed)
- [Model Performance](#-model-performance)
- [How to Run Locally](#-how-to-run-locally)
- [Docker Deployment](#-docker-deployment)
- [API Endpoints](#-api-endpoints)
- [Tech Stack](#-tech-stack)
- [Key Insights](#-key-insights)
- [Author](#-author)

---

## 🔍 Project Overview

Phishing attacks are one of the most common cybersecurity threats. This project builds a machine learning model that automatically classifies websites as **Legitimate** or **Phishing** based on URL structure and domain characteristics.

**What this project does:**
- Performs complete Exploratory Data Analysis (EDA)
- Cleans and preprocesses data
- Engineers new features using domain knowledge
- Trains and compares 7 machine learning models
- Explains predictions using SHAP and LIME
- Deploys the model as a REST API using Flask

---

## 📊 Dataset

| Property | Value |
|----------|-------|
| Total Samples | 11,430 |
| Total Features | 87 |
| Target Classes | Legitimate (0), Phishing (1) |
| Class Balance | 50% - 50% (Perfectly Balanced) |
| Missing Values | None |

**Key Features include:**
- URL length, number of dots, hyphens, special characters
- Domain age, DNS record, WHOIS information
- Page rank, web traffic, Google index
- HTTPS token, number of hyperlinks, redirections

---

## 📁 Project Structure

```
phishing-website-detection/
│
├── 📂 phishing_app/              # Flask Web Application
│   ├── app.py                    # Main Flask app
│   ├── best_model.pkl            # Trained Random Forest model
│   ├── X_train.csv               # Training data reference
│   ├── requirements.txt          # Python dependencies
│   ├── Dockerfile                # Docker configuration
│   └── templates/
│       └── index.html            # Web interface
│
├── 📂 notebooks/                 # Jupyter Notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Training.ipynb
│   └── 05_Explainability.ipynb
│
├── 📂 reports/                   # PDF & Word Reports
│   ├── EDA_Report.pdf
│   ├── Data_Preprocessing_Report.docx
│   ├── Feature_Selection_Report.docx
│   └── Explainability_Deployment_Report.docx
│
├── 📂 visualizations/            # Charts & Graphs
│   ├── shap_summary_beeswarm.png
│   ├── shap_waterfall.png
│   ├── lime_explanations.png
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── model_comparison_chart.png
│
├── 📂 data/                      # Datasets
│   ├── phishing_data.csv         # Original dataset
│   ├── X_train.csv               # Training features
│   ├── X_test.csv                # Testing features
│   ├── y_train.csv               # Training labels
│   └── y_test.csv                # Testing labels
│
└── README.md                     # This file
```

---

## ✅ Tasks Completed

### Task 1 — Exploratory Data Analysis (EDA)
- Descriptive statistics for all 87 features
- Histograms, pair plots, correlation heatmaps
- Missing values, outlier detection, class balance analysis
- **Finding:** Zero missing values, perfectly balanced dataset

### Task 2 — Data Preprocessing
- Handled missing values (none found)
- Removed duplicates (none found)
- Label encoded categorical features
- Applied StandardScaler normalization
- 80-20 stratified train-test split

### Task 3 — Feature Engineering
- Correlation analysis (14 highly correlated pairs found)
- Random Forest + Mutual Information feature importance
- Created **10 new domain-knowledge features:**

| New Feature | Description |
|-------------|-------------|
| `url_complexity_score` | Weighted sum of special characters |
| `suspicious_char_ratio` | Ratio of @, %, $, _ to URL length |
| `domain_trust_score` | Combined web traffic + page rank + google index |
| `has_ip_address` | Binary flag for IP in URL |
| `special_char_density` | Density of special characters |
| `external_links_ratio` | External to internal links ratio |
| `redirection_chain` | Total number of redirections |
| `security_score` | HTTPS + DNS + domain indicators |
| `url_hostname_ratio` | URL length to hostname ratio |
| `digits_dominance` | Product of digit ratios |

- **Result:** Reduced from 87 → 58 optimized features (33% reduction)

### Task 4 — Model Training & Evaluation
- Trained and compared **7 machine learning algorithms**
- Evaluated using Accuracy, Precision, Recall, F1-Score, ROC-AUC
- **Best Model: Random Forest with 95.58% accuracy**

### Task 5 — Model Explainability & Deployment
- SHAP analysis for global feature importance
- LIME analysis for local per-prediction explanations
- Flask REST API with 6 endpoints
- Docker containerization
- Web interface for non-technical users

---

## 🏆 Model Performance

### Comparison of All Models

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| **Random Forest** ⭐ | **95.58%** | **95.72%** | **95.45%** | **95.58%** | **99.12%** |
| XGBoost | 94.84% | 94.97% | 94.71% | 94.84% | 98.87% |
| Gradient Boosting | 93.96% | 94.10% | 93.83% | 93.96% | 98.54% |
| Decision Tree | 92.13% | 92.26% | 91.99% | 92.13% | 92.13% |
| Logistic Regression | 89.54% | 89.67% | 89.41% | 89.54% | 95.23% |
| K-Nearest Neighbors | 88.72% | 88.85% | 88.60% | 88.72% | 94.61% |
| Naive Bayes | 73.45% | 73.58% | 73.32% | 73.45% | 81.23% |

### Best Model Confusion Matrix

```
                  Predicted
              Legit    Phishing
Actual Legit   1089       54
       Phish    47       1096

Accuracy:  95.58%
Precision: 95.29%
Recall:    95.89%
F1-Score:  95.59%
ROC-AUC:   99.12%
```

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.11+
- pip

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/phishing-website-detection.git
cd phishing-website-detection
```

### Step 2: Install Dependencies
```bash
pip install -r phishing_app/requirements.txt
```

### Step 3: Run the App
```bash
cd phishing_app
python app.py
```

### Step 4: Open Browser
```
http://localhost:5000
```

That's it! 🎉

---

## 🐳 Docker Deployment

### Build and Run with Docker
```bash
# Build the image
docker build -t phishing-detector ./phishing_app

# Run the container
docker run -p 5000:5000 phishing-detector

# Open browser at http://localhost:5000
```

---

## 🔌 API Endpoints

### Base URL: `http://localhost:5000`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web interface |
| GET | `/health` | Health check |
| GET | `/features` | List all 87 features |
| POST | `/predict` | Get phishing prediction |
| POST | `/explain` | LIME explanation |
| POST | `/shap_explain` | SHAP explanation |

### Example: Make a Prediction

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "google_index": 0,
    "page_rank": 0,
    "ip": 1,
    "phish_hints": 3,
    "https_token": 0,
    "dns_record": 0,
    "web_traffic": 0
  }'
```

**Response:**
```json
{
  "status": "success",
  "prediction": 1,
  "label": "Phishing",
  "confidence": 56.18,
  "prob_legitimate": 43.82,
  "prob_phishing": 56.18
}
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.11 |
| ML Library | Scikit-Learn, XGBoost |
| Explainability | SHAP, LIME |
| Web Framework | Flask |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Deployment | Docker, Gunicorn |
| Documentation | Word, PDF |

---

## 💡 Key Insights

1. **google_index** is the most important feature (SHAP: 0.132) — sites not indexed by Google are highly suspicious
2. **page_rank** and **web_traffic** confirm domain legitimacy
3. **Phishing URLs** are longer with more special characters
4. **IP addresses in URLs** strongly indicate phishing
5. **phish_hints** (keywords like 'login', 'secure', 'verify') are red flags
6. **Domain age** matters — newly registered domains are suspicious
7. Random Forest outperformed all other models with **95.58% accuracy**

---

## 📈 SHAP Feature Importance

```
Feature                    Mean SHAP Value
─────────────────────────────────────────
google_index               0.13183  ████████████
page_rank                  0.06842  ███████
nb_hyperlinks              0.06256  ██████
web_traffic                0.05088  █████
nb_www                     0.04071  ████
phish_hints                0.02500  ███
domain_age                 0.02088  ██
ratio_digits_url           0.01847  ██
safe_anchor                0.01521  █
ratio_extRedirection       0.01424  █
```

---

## 👤 Author

**Data Science & Analytics Intern**

- 📧 Internship Submission Project
- 🏫 Data Science & Analytics Program
- 📅 2024-2025

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- Dataset: Phishing Website Detection Dataset
- Libraries: Scikit-Learn, XGBoost, SHAP, LIME, Flask
- Tools: Python, Docker, Matplotlib, Seaborn

---

> ⭐ If you found this project helpful, please give it a star on GitHub!

## 🌐 Live Demo
👉 **[Click here to try the live website!](https://phishing-website-detection-sqbm.onrender.com)**

---
# 🛡️ Phishing Website Detection - Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask)
![Accuracy](https://img.shields.io/badge/Accuracy-95.58%25-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow)

> A complete end-to-end Machine Learning project 
> to detect phishing websites using URL and domain 
> features. Built during Data Science & Analytics 
> Internship at Code-B Solutions Pvt Ltd.

---

## 📌 Project Overview

Phishing attacks steal billions annually. This project 
builds an ML model that automatically classifies 
websites as Legitimate or Phishing based on URL 
structure and domain characteristics.

---

## 📊 Dataset

| Property | Value |
|----------|-------|
| Total Samples | 11,430 |
| Total Features | 87 |
| Target Classes | Legitimate / Phishing |
| Class Balance | 50% - 50% |
| Missing Values | None |

---

## 🏆 Best Model Results

| Metric | Score |
|--------|-------|
| Accuracy | 95.58% |
| Precision | 95.29% |
| Recall | 95.89% |
| F1-Score | 95.59% |
| ROC-AUC | 99.12% |

---

## 📈 Visualizations

### Model Performance Comparison
![Model Comparison](visualizations/linkedin_1_model_comparison.png)

### Confusion Matrix
![Confusion Matrix](visualizations/linkedin_2_confusion_matrix.png)

### ROC Curve
![ROC Curve](visualizations/linkedin_3_roc_curve.png)

### Feature Importance
![Feature Importance](visualizations/linkedin_4_feature_importance.png)

---

## ✅ Tasks Completed

| Task | Description |
|------|-------------|
| Task 2 | Exploratory Data Analysis (EDA) |
| Task 3 | Data Preprocessing |
| Task 4 | Feature Engineering |
| Task 5 | Model Training & Evaluation |
| Task 6 | Explainability & Deployment |
| Task 7 | Final Presentation |

---

## 🔧 10 New Features Engineered

| Feature | Description |
|---------|-------------|
| url_complexity_score | Weighted special characters |
| suspicious_char_ratio | Ratio of @, %, $, _ |
| domain_trust_score | Traffic + rank + index |
| has_ip_address | Binary IP flag |
| special_char_density | Overall char density |
| external_links_ratio | External/internal links |
| redirection_chain | Total redirections |
| security_score | HTTPS + DNS indicators |
| url_hostname_ratio | Path complexity |
| digits_dominance | Digit ratio product |

---

## 🚀 How to Run Locally

### Step 1: Clone Repository
```bash
git clone https://github.com/dhanshreesarangAI/phishing-website-detection.git
cd phishing-website-detection
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Flask App
```bash
cd phishing_flask_app
python app.py
```

### Step 4: Open Browser---

http://localhost:5000

## 🐳 Docker Deployment

```bash
docker build -t phishing-detector .
docker run -p 5000:5000 phishing-detector
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Web interface |
| GET | /health | Health check |
| POST | /predict | Get prediction |
| POST | /explain | LIME explanation |
| POST | /shap_explain | SHAP explanation |

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.11 |
| ML | Scikit-Learn, XGBoost |
| Explainability | SHAP, LIME |
| Deployment | Flask, Docker |
| Visualization | Matplotlib, Seaborn |

---

## 💡 Key Insights

1. **google_index** is the strongest phishing indicator
2. **page_rank** and **web_traffic** confirm legitimacy
3. Phishing URLs are longer with more special characters
4. IP addresses in URLs strongly indicate phishing
5. Random Forest outperformed all 6 other algorithms

---

## 👤 Author

**Dhanshree Sarang**
- 📧 sarangdhanshree6@gmail.com
- 🔗 linkedin.com/in/dhanshreesarang
- 📍 Pune, Maharashtra, India

---

## 🏢 Internship

**Code-B Solutions Pvt Ltd**
Mumbai, Maharashtra
March 2026 – May 2026

---

⭐ If you found this helpful, please star this repo!

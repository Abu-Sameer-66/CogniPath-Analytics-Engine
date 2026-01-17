# 🎓 CogniPath Analytics Engine

> **An AI-powered predictive system designed to forecast academic performance by analyzing student behavioral metrics like sleep efficiency and attendance risk.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/AI_Engine-Scikit--Learn-orange?logo=scikitlearn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production_Ready-success)

---

## 🚀 Project Mission
Traditional education systems are **reactive**—they wait for a student to fail. **CogniPath** is **proactive**. 

This engine uses **Ensemble Machine Learning** to correlate lifestyle habits (Sleep, Study Efficiency, Attendance) with future academic outcomes. It identifies "At-Risk" students *before* exams, allowing for timely intervention.

---

## ⚙️ Engineering Architecture

The system follows a strict **Modular Object-Oriented Design**:

### 1. Data Engineering (`preprocessing.py`)
This module handles raw data ingestion and advanced feature extraction:
* **Cognitive Efficiency Ratio:** Calculates `Study Hours / (Sleep Hours + 1)` to measure effective learning vs. burnout.
* **Dynamic Risk Segmentation:** Automatically flags students as "High Risk" if `class_attendance` drops below 75%.

### 2. AI Model Engine (`model_engine.py`)
Instead of a simple linear model, we utilize **Gradient Boosting Regressor**:
* **Pipeline Integration:** Wraps scaling and One-Hot Encoding within a Scikit-Learn Pipeline to prevent data leakage.
* **Error Correction:** Uses an ensemble of decision trees to correct prediction errors sequentially.

### 3. Orchestration (`main.py`)
The central controller that:
1.  Initiates the Data Pipeline.
2.  Trains the Model on `train.csv`.
3.  Evaluates performance (R² Score).
4.  Exports predictions to `model_results_for_dashboard.csv` for analysis.

---

## 🛠️ Tech Stack

| Component | Technology | Usage |
| :--- | :--- | :--- |
| **Language** | `Python` | Core Application Logic |
| **ML Library** | `Scikit-Learn` | Gradient Boosting, Pipelines, ColumnTransformer |
| **Data Processing** | `Pandas / NumPy` | Vectorized Data Manipulation |
| **Data Source** | `CSV` | Structured Student Data |

---

## ⚡ How to Run This Project

Follow these steps to deploy the engine on your local machine:

**1. Clone the Repository**
```bash
git clone [https://github.com/Abu-Sameer-66/CogniPath-Analytics-Engine.git](https://github.com/Abu-Sameer-66/CogniPath-Analytics-Engine.git)
cd CogniPath-Analytics-Engine

<div align="center">

  <a href="https://github.com/YourUsername/CogniPath">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=00D2FF&background=00000000&center=true&vCenter=true&width=435&lines=COGNIPATH+ENGINE;EduMatrix+Cognitive+Analytics;Predicting+Student+Success;AI-Driven+Risk+Assessment" alt="Typing SVG" />
  </a>

  <br />

  <img src="https://img.shields.io/badge/Python-3.8%2B-3a7bd5?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Scikit--Learn-Ensemble-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Sklearn" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Engineering-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Status-Pro--Active-00d2ff?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />

  <br />
  <br />

  <img src="https://via.placeholder.com/1000x400/0f172a/00d2ff?text=COGNIPATH+ANALYTICS+DASHBOARD" alt="Project Banner" width="100%" />

  <h3 align="center">🚀 Architecting the Future of Educational Intelligence</h3>

  <p align="center">
    CogniPath is a high-performance <b>Gradient Boosting Machine (GBM)</b> pipeline designed to analyze student behavioral patterns, predict academic performance, and identify at-risk individuals with surgical precision.
  </p>

</div>

---

## ⚡ Executive Summary

**CogniPath Engine** (formerly EduMatrix) is not just a predictive model; it is a full-stack data science solution. By ingesting raw behavioral data—ranging from study habits to sleep efficiency—it engineer's high-dimensional features to train a robust ensemble regressor. The system culminates in an interactive `Seaborn` dashboard that visualizes the "Academic Future" of student cohorts.

### 🌟 Key Features

* **🧠 Cognitive Efficiency Metrics**: Automatically calculates `Efficiency_Ratio` (Study Hours / Sleep Hours) to measure retention probability.
* **🛡️ Dynamic Risk Segmentation**: Classifies students into `High Risk` vs. `Low Risk` categories based on attendance thresholds (<75%).
* **📈 Ensemble Gradient Boosting**: Utilizes a tuned `GradientBoostingRegressor` (300 estimators, depth 4) for high-fidelity score prediction.
* **🎨 Academic Future Dashboard**: A pro-grade visualization suite using a custom Cyan/Slate color theory (`#00d2ff` & `#3a7bd5`).

---

## 🛠️ System Architecture

The system follows a strict **ETL-Model-Visualize** pipeline pattern.

```mermaid
graph LR
    A[Raw Data (train.csv)] -->|Ingest & Clean| B(DataEngineer Class)
    B -->|Feature Engineering| C{Preprocessing Pipeline}
    C -->|OneHot & Scaling| D[Transformed Tensors]
    D -->|Train| E[EduModel (Gradient Boosting)]
    E -->|Predict| F[Results CSV]
    F -->|Visualize| G[Analytics_Dashboard.ipynb]
    
    style A fill:#3a7bd5,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#00d2ff,stroke:#fff,stroke-width:2px,color:#000
    style G fill:#fff,stroke:#00d2ff,stroke-width:4px,color:#000

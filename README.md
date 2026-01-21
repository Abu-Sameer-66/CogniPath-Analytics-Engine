<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&ColorList=00c6ff,0072ff,8F246A,814B32,337064&height=280&section=header&text=CogniPath%20Analytics&fontSize=45&fontColor=C2BAB3&animation=fadeIn&fontAlignY=35&desc=Next-Gen%20Academic%20Prediction%20Engine&descAlignY=60&descAlign=50" width="100%"/>

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=C2BAB3&center=true&vCenter=true&width=600&lines=Initializing+Cognitive+Pipeline...;Analyzing+Sleep+vs+Study+Efficiency...;Detecting+Academic+Burnout...;Gradient+Boosting+Model+DEPLOYED." />
  </a>
  
  <br/>

  <img src="https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/EDA-895343?style=for-the-badge&logo=EDA&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Architecture-Modular_OOP-000000?style=for-the-badge&logo=github&logoColor=cyan" />
  <img src="https://img.shields.io/badge/Matplotlib-45876A?style=for-the-badge&logo=matplotlib&logoColor=white" />
</div>

---

## 🚀 Mission: Decoding Student Success
> **"Grades are not just numbers; they are the output of a lifestyle algorithm."**

Traditional systems wait for failure. **CogniPath** predicts it.
By engineering a custom **Cognitive Efficiency Ratio**, this engine correlates a student's biological habits (Sleep, Attendance) with their academic trajectory, identifying "Burnout Risk" before exam day.

---

## ⚡ Key Algorithmic Innovations
*The engineering logic behind the predictions:*

| Feature | The Science Behind It |
| :--- | :--- |
| **🧠 Cognitive Efficiency** | Custom Metric: $\frac{\text{Study Hours}}{(\text{Sleep Hours} + 1)}$ <br> *Detects students who study hard but retain less due to sleep deprivation.* |
| **🛡️ Risk Segmentation** | **Dynamic Vectorization:** Automatically flags students as `High Risk` if attendance $< 75\%$ using NumPy vectorized operations. |
| **🌲 Ensemble Learning** | **Gradient Boosting Regressor:** Uses a sequence of decision trees where each tree corrects the errors of the previous one. |
| **⚙️ Pipeline Automation** | **Scikit-Learn Pipelines:** Encapsulates Scaling (`StandardScaler`) and Encoding (`OneHotEncoder`) to prevent data leakage. |

---

## 🛠️ System AND Architecture
*Live Data Flow Visualization (Auto-Generated):*

```mermaid
graph LR
    subgraph Data Ingestion
        A[📂 train.csv] -->|Load| B(DataEngineer Class)
    end
    
    subgraph Feature Engineering
        B -->|Calc| C{Efficiency Ratio}
        B -->|Segment| D{Attendance Risk}
        C & D -->|Transform| E[Preprocessing Pipeline]
    end
    
    subgraph AI Core
        E -->|Train| F[Gradient Boosting Model]
        F -->|Predict| G[🎯 Exam Score Forecast]
    end
    
    style F fill:#0072ff,stroke:#00c6ff,stroke-width:2px,color:#fff
    style C fill:#00c6ff,stroke:#0072ff,stroke-width:2px,color:#000
    style D fill:#ff5252,stroke:#333,stroke-width:2px,color:#fff

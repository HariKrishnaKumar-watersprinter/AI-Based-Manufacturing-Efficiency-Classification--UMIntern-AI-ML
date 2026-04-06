# 🏭 AI-Based Manufacturing Efficiency Classification
Deployed link : https://ai-based-manufacturing-efficiency-classification.streamlit.app/

### Using Sensor, Production, and 6G Network Data

---

## 📌 Project Overview

This project builds an **AI-powered intelligent monitoring system** for smart manufacturing environments. It classifies real-time machine efficiency into:

* ✅ High Efficiency
* ⚠️ Medium Efficiency
* ❌ Low Efficiency

By leveraging **sensor data, production metrics, and 6G network signals**, the system enables:

* Real-time decision-making
* Early detection of inefficiencies
* Data-driven operational optimization

---

## 🎯 Problem Statement

Modern smart factories face challenges such as:

* Delayed detection of efficiency degradation
* Complex interpretation of multiple sensor/network signals
* Lack of automated efficiency classification

Without AI:

* Production losses increase
* Downtime goes unnoticed
* Manual monitoring becomes inefficient

---

## 🚀 Solution Approach

We developed an **end-to-end AI system** that:

1. Collects and processes manufacturing data
2. Performs advanced EDA and validation
3. Trains ML models for efficiency classification
4. Explains predictions using AI explainability
5. Deploys insights via an interactive Streamlit dashboard

---

## 📊 Dataset Description

| Feature                       | Description              |
| ----------------------------- | ------------------------ |
| Temperature_C                 | Machine temperature      |
| Vibration_Hz                  | Vibration frequency      |
| Power_Consumption_kW          | Energy usage             |
| Network_Latency_ms            | 6G latency               |
| Packet_Loss_%                 | Network reliability      |
| Production_Speed_units_per_hr | Output rate              |
| Error_Rate_%                  | Operational errors       |
| Predictive_Maintenance_Score  | Maintenance readiness    |
| Efficiency_Status             | Target (High/Medium/Low) |

---

## 🧠 Key Features

### 🔍 Data Validation

* Schema validation
* Range checks
* Missing values detection
* Outlier identification

### 📊 Exploratory Data Analysis (EDA)

* Univariate, Bivariate, Multivariate analysis
* Correlation insights
* Statistical testing

### 🤖 Machine Learning Models

* Logistic Regression (baseline)
* Random Forest
* Gradient Boosting / XGBoost

### 🧠 Explainability (Critical Feature)

* Feature Importance
* SHAP-based explanations
* Local prediction reasoning

### ⚙️ Operational Insights

* Network vs Sensor impact comparison
* Machine-level efficiency trends
* Efficiency distribution per machine

### ⚠️ Low Efficiency Intelligence

* Root cause analysis
* Recommended actions
* Proactive strategies

### 📄 Executive Summary

* KPI-driven insights
* Policy recommendations
* Government-ready output

---

## 🖥️ Streamlit Dashboard Modules

### 1️⃣ Data Validation Dashboard

* Detect errors, anomalies, inconsistencies

### 2️⃣ EDA Dashboard

* Interactive visualization of patterns

### 3️⃣ Efficiency Prediction

* Real-time classification
* Confidence score

### 4️⃣ Explainability Panel

* Why predictions happen

### 5️⃣ Operational Insights

* Network vs sensor influence
* Machine performance trends

### 6️⃣ Low Efficiency Analysis

* Root causes
* Action recommendations

### 7️⃣ Executive Summary

* High-level insights for stakeholders

---

## 🏗️ Project Structure

```
AI-Based Manufacturing Efficiency Classification/
├── Authentication/
│   ├── config.py                  # Logic for loading authentication settings
│   ├── config.yaml                # Encrypted user credentials and configuration
│   ├── main.py                    # Primary authentication UI (Login/Forgot Password)
│   └── signup.py                  # User registration and validation logic
├── database/
│   ├── database_content.py        # UI logic for viewing prediction history
│   ├── database_create.py         # SQLAlchemy models and DB connection setup
│   └── manufacturing_efficiency.db # Local SQLite storage for prediction logs
├── model_tracking/
│   └── mlflow_track.py            # MLflow integration for experiment tracking
├── pages/
│   ├── Data_Quality.py            # Data health and outlier detection reports
│   ├── Data_Validation.py         # Statistical data validation reports
│   ├── Digital_Twin_Simulation.py # Digital Twin simulation interface
│   ├── EDA_Dashboard.py           # Exploratory Data Analysis visuals
│   ├── Explainability.py          # SHAP-based feature importance visuals
│   ├── Machine_insights.py        # Individual machine performance insights
│   ├── MACHINE_Efficiency_TRENDS.py # Temporal efficiency trend analysis
│   ├── model_comparision_and_metrics.py # Model evaluation and selection
│   ├── Network_vs_Sensor_Impact_Comparison.py # Impact correlation analysis
│   ├── Operational_Monitoring.py  # Real-time operational oversight
│   ├── Risk_Alerts.py             # Anomaly detection and risk alerts
│   └── ThresholdOptimization.py   # Classification threshold tuning
├── prediction/
│   └── Efficiency_Prediction.py   # Inference logic for efficiency classification
├── src/
│   ├── data_loader.py             # Dataset ingestion logic
│   ├── data_quality.py            # Statistical quality check utilities
│   ├── data_validation.py         # valiate the dataset
│   ├── low_efficiency_analysis.py # low efficieny analysis 
│   ├── Machine_EfficiencyTrends.py # idendify per Machine Efficiency Trends
│   ├── eda.py                     # Backend functions for EDA dashboards
│   ├── explainability.py          # Logic for SHAP value generation
│   ├── feature_engineering.py     # Manufacturing-specific feature creation
│   ├── model_training.py         # Core ML training pipeline
│   ├── model_training1.py         # Core ML training pipeline
│   ├── Network_vs_Sensor_Impact.py # Network VS Sensor Comparision
│   ├── preprocessing.py           # Data cleaning and scaling utilities
│   └── simulate_machine.py        # simulate the sensor value to predict the machine
├── utils/
│   └── threshold.py               # Metric calculations for various thresholds
├── best model/               # Directory containing production-ready .pkl model files
├── data/
│   └── results.csv           #Model Result Data  
│   └── Thales_Group_Manufacturing.csv # orginal data set
│   └── sample.csv            # sample data set for prediction
├── app.py                   # Main application entry point
└── requirements.txt          # List of project dependencies
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/AI-Manufacturing-Efficiency.git
cd AI-Manufacturing-Efficiency

pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run dashboard/app.py
```

---

## 📈 Key Insights

* ⚠️ High **error rate** strongly reduces efficiency
* 📡 Network latency & packet loss significantly impact production
* ⚙️ Sensor stability (temperature, vibration) affects consistency
* 🚀 Production speed is a strong indicator of high efficiency

---

## 🧠 Business & Government Impact

### 🏭 Industrial Impact

* Reduce downtime
* Improve productivity
* Enable predictive maintenance

### 🌐 Infrastructure Impact

* Highlights importance of **6G network reliability**

### 🏛️ Policy Relevance

* Supports smart manufacturing initiatives
* Enables AI-driven industrial governance

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* SHAP
* Matplotlib, Seaborn
* Streamlit

---

## 🔮 Future Enhancements

* Real-time streaming (Kafka)
* Predictive maintenance AI models
* Digital twin simulation
* Cost impact analysis
* Anomaly detection system

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork and improve.

---
---

## 🎤 Author

**Hari Krishna Kumar -AI,ML,Data Science & Analytics Enthusiast**

---
## 📬 Contact

For collaboration or queries:

* LinkedIn: *[www.linkedin.com/in/hari-668364112]*
* Email: *[harikrishnakumar368@gmail.com]*

---

## ⭐ Acknowledgment

Inspired by smart manufacturing initiatives and industrial AI advancements.

---

## 📌 Conclusion

This project demonstrates how **AI + IoT + 6G** can transform traditional manufacturing into:

> 🚀 Intelligent, autonomous, and efficient industrial ecosystems

# 🏦 Bank Churn Prediction System

An end-to-end Machine Learning solution designed to predict customer churn, provide explainable AI insights, and suggest retention strategies.

## 📁 Project Structure

```text
├── Authentication/           # Security & User Management
│   ├── config.py             # Authentication configuration & YAML loader
│   ├── config.yaml           # Hashed credentials and session settings
│   ├── main.py               # Authentication entry point (Login/Signup/Forgot PW)
│   └── signup.py             # New user registration logic
│
├── data/                     # Data Storage
│   ├── European_Bank.csv     # Raw dataset
│   └── results.csv           # Performance metrics from the training pipeline
│
├── database/                 # Persistence Layer
│   ├── bank_data.db          # SQLite database (Local storage)
│   ├── database_content.py   # Streamlit view for exploring saved records
│   └── database_create.py    # SQLAlchemy models and DB connection logic
│
├── model_tracking/           # Experiment Tracking
│   └── mlflow_tracking.py    # Integration with MLflow for logging runs and models
│
├── pages/                    # Streamlit Multi-page UI
│   ├── Churn_Risk_Distribution_Dashboard.py # Risk segmentation & Geo-analysis
│   ├── Cost_Analysis.py      # Business cost vs. threshold optimization
│   ├── Data_Quality.py       # Data health and outlier detection reports
│   ├── Dependency_Risk.py    # Customer dependency risk metrics
│   ├── EDA_Dashboard.py      # Tabbed Exploratory Data Analysis
│   ├── Executive Summary for Government Stakeholders.py # High-level summary & PDF export
│   ├── Model_Explainability.py # SHAP-based feature importance visuals
│   ├── ModelComparison.py    # Model selection and retraining interface
│   ├── ThresholdOptimization.py # Precision-Recall curve analysis
│   └── What_If_Simulator.py  # Interactive churn probability calculator
│
├── src/                      # Core Machine Learning Pipeline
│   ├── data_loader.py        # Dataset ingestion
│   ├── data_quality.py       # Statistical checks and quality reporting
│   ├── eda.py                # Analytical functions for dashboards
│   ├── executive_summary.py  # Business logic for the executive report
│   ├── explainability.py     # SHAP value generation logic
│   ├── feature_engineering.py # Derived metrics (BalanceSalaryRatio, etc.)
│   ├── model_training.py     # GridSearch & Hyperparameter tuning pipeline
│   ├── model_training1.py    # Optimized training loop with sampling techniques
│   ├── preprocessing.py      # Scaling, Encoding, and Train-Test splitting
│   └── segmentation.py       # KMeans clustering for customer segmentation
│
├── utils/                    # Helper Utilities & Business Logic
│   ├── cost.py               # Financial cost function for predictions
│   ├── helpers.py            # General risk mapping helpers
│   ├── recommendation.py     # Retention action logic
│   ├── report_generator.py   # PDF generation using ReportLab
│   ├── retention_engine.py   # Personalized strategy logic
│   ├── risk_metrics.py       # Customer risk scoring algorithms
│   └── threshold.py          # Metric calculations across various thresholds
│
├── best model/               # Production-ready .pkl model artifacts
├── app.py                    # Main Streamlit application entry point
└── requirements.txt          # Project dependencies
```

## 🚀 Key Modules

*   **Core Pipeline (`src/`):** Contains the modularized steps for the ML lifecycle, from raw data to a trained model.
*   **Intelligent Dashboard (`pages/`):** A comprehensive UI providing insights into data quality, model performance, and business impact.
*   **Explainable AI (`src/explainability.py`):** Uses SHAP to provide transparency into why specific customers are flagged as high risk.
*   **Business Optimization (`utils/cost.py`):** Translates technical metrics (Accuracy/AUC) into financial impact, helping stakeholders choose the best decision threshold.

## 🛠️ Tech Stack

*   **Frontend:** Streamlit
*   **ML Frameworks:** Scikit-Learn, XGBoost, Imbalanced-Learn
*   **Tracking:** MLflow
*   **Database:** SQLAlchemy (PostgreSQL / SQLite)
*   **Explainability:** SHAP
*   **Visualization:** Plotly, Matplotlib
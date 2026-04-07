import streamlit as st
from src.data_quality import data_quality_preprocessing
from prediction import Efficiency_Prediction
from database import database_content
from Authentication import main

st.set_page_config(
    page_title="AI Manufacturing Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_data

def load_data():
    df=data_quality_preprocessing()
    return df

def home_page():
    
    st.title(" 🏭 AI-Based Manufacturing Efficiency Intelligence System")
    st.markdown("""
### 🚀 Predict • Analyze • Explain • Manufacturing Efficiency
""")

    high = (df['Efficiency_Status'] == "High").mean()
    medium = (df['Efficiency_Status'] == "Medium").mean()
    low = (df['Efficiency_Status'] == "Low").mean()
    No_of_machines=df['Machine_ID'].nunique()
    st.markdown("## 📊 Overview")
    col1,col2, col3, col4 = st.columns(4)
    col1.metric("No of Machines", No_of_machines)
    col2.metric("High Efficiency", f"{high:.2%}")
    col3.metric("Medium Efficiency", f"{medium:.2%}")
    col4.metric("Low Efficiency", f"{low:.2%}")
    st.markdown("""
    ### 🎯 Objective
    Real-time classification and monitoring of manufacturing efficiency using:
    - Sensor Data
    - Production Metrics
    - 6G Network Performance
    """)

def pred_page():
    Efficiency_Prediction.pred()

def database_page():
    database_content.database_content_view()

pages = {
    "Main": [
        st.Page(home_page, title="Home", icon="🏠", default=True),
        st.Page(pred_page, title="Efficiency Prediction", icon="🔮"),
        st.Page(database_page, title="Database Content", icon="💾"),
    ],
    "Data Insights": [
        st.Page("pages/Data_Quality.py", title="Data Quality", icon="🧹"),
        st.Page("pages/Data_Validation.py", title="Data Validation", icon="📋"),
        st.Page("pages/EDA_Dashboard.py", title="Exploratory Analysis", icon="📊"),
        #st.Page("pages/Churn_Risk_Distribution_Dashboard.py", title="churn Risk Distribution", icon="📈"),
    ],
    "Model Analysis": [
        st.Page("pages/model_comparision_and_metrics.py", title="Model Comparision and Metrics", icon="⚖️"),
        st.Page("pages/ThresholdOptimization.py", title="Thresholds", icon="🎯"),
        st.Page("pages/Explainability.py", title="Explainability", icon="🧠"),
        #st.Page('pages/model')
    ],
    "Strategy & Risk": [
        st.Page("pages/Risk_Alerts.py", title="RISK & ALERT DASHBOARD", icon="🚨"),
        st.Page("pages/Machine_Insights.py", title="Machine Insights", icon="💡"),
        st.Page("pages/Operational_Monitoring.py", title="Operation Monitoring", icon="⚙️"),
        st.Page("pages/Digital_Twin_Simulation.py", title="Digital Twin Simulation", icon="🏭"),
        st.Page("pages/Network_vs_Sensor_Impact_Comparison.py", title="Network VS Sensor Comparision", icon="📡"),
        st.Page("pages/MACHINE_Efficiency_TRENDS.py", title="Machine Efficiency Trends", icon="📈"),
    ],
    "Government": [
    # st.Page("pages/Executive Summary for Government Stakeholders.py", title="Executive Summary", icon="🏛️"),
    ]
}


if __name__ == "__main__":
    #auth_status = main.user_auth()
    #if auth_status:
        df=load_data()
        
        pg = st.navigation(pages)
        pg.run()

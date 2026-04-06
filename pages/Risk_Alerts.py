import streamlit as st
import pandas as pd
from src.data_quality import data_quality_preprocessing
st.title("⚠️ Risk & Alerts Dashboard")

df = data_quality_preprocessing()

# Risk Score
df['Risk_Score'] = (
    df['Error_Rate_%'] +
    df['Packet_Loss_%'] +df['Quality_Control_Defect_Rate_%']+
    df['Network_Latency_ms'] /200* 100
)

# Risk Classification
def classify_risk(x):
    if x > 80:
        return "High"
    elif x > 40:
        return "Medium"
    else:
        return "Low"

df['Risk_Level'] = df['Risk_Score'].apply(classify_risk)

st.subheader("Risk Distribution")
st.bar_chart(df['Risk_Level'].value_counts())

# Alerts
st.subheader("🚨 High Risk Machines")
alerts = df[df['Risk_Level']=="High"]

st.dataframe(alerts[['Machine_ID','Risk_Score']].head(20))
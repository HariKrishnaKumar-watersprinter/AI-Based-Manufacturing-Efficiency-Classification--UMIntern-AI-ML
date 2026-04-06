import streamlit as st
import pandas as pd
from src.data_quality import data_quality_preprocessing

st.title("📊 Machine-Level Insights")

df = data_quality_preprocessing()

machine_id = st.selectbox("Select Machine", df['Machine_ID'].unique())

filtered = df[df['Machine_ID'] == machine_id]

st.subheader("Production Speed Trend")
st.line_chart(filtered['Production_Speed_units_per_hr'])

st.subheader("Error Rate Trend")
st.line_chart(filtered['Error_Rate_%'])

st.subheader("Network Latency Trend")
st.line_chart(filtered['Network_Latency_ms'])

# Derived Insight
st.subheader("Efficiency Score")
filtered['Efficiency_Score'] = (
    filtered['Production_Speed_units_per_hr']
    - filtered['Error_Rate_%']
)

st.line_chart(filtered['Efficiency_Score'])
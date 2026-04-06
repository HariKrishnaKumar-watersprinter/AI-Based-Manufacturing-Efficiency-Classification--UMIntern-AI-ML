import streamlit as st
import pandas as pd
from src.data_quality import data_quality_preprocessing
st.title("📡 Operational Monitoring")
df = data_quality_preprocessing()
st.subheader("Network vs Error Impact")
st.scatter_chart(df[['Network_Latency_ms', 'Error_Rate_%']])
st.subheader("Packet Loss vs Efficiency Proxy")
df['Efficiency_Score'] = df['Production_Speed_units_per_hr'] - df['Error_Rate_%']
st.scatter_chart(df[['Packet_Loss_%', 'Efficiency_Score']])
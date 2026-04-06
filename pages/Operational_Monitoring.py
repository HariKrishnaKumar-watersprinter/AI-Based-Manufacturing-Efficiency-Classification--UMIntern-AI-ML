import streamlit as st
import pandas as pd
from src.data_quality import data_quality_preprocessing
import plotly.express as px
st.title("📡 Operational Monitoring")
df = data_quality_preprocessing()
st.subheader("Network vs Error Impact")
fig=px.scatter(df,x='Network_Latency_ms',y='Error_Rate_%',color='Efficiency_Status',title='Network vs Error Impact')
st.plotly_chart(fig)
st.subheader("Packet Loss vs Efficiency Proxy")
df['Efficiency_Score'] = df['Production_Speed_units_per_hr'] - df['Error_Rate_%']
fig=px.scatter(df,x='Packet_Loss_%',y='Efficiency_Score',color='Efficiency_Status',title='Packet Loss vs Efficiency Proxy')
st.plotly_chart(fig)

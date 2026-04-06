import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.Machine_EfficiencyTrends import machine_efficiency_distribution,machine_trends
import plotly.express as px
# -------------------------
# 2. PER-MACHINE TRENDS
# -------------------------
st.subheader("🏭 Per-Machine Efficiency Trends")

trend_df = machine_trends()

machine_selected=st.selectbox("Select Machine",trend_df['Machine_ID'].unique())

machine_data = trend_df[trend_df['Machine_ID'] == machine_selected]

# Encode efficiency for visualization
mapping = {'Low': 0, 'Medium': 1, 'High': 2}
machine_data['Efficiency_Num'] = machine_data['Efficiency_Status'].map(mapping)
dist = machine_efficiency_distribution()
fig = px.bar(
    dist.loc[machine_selected],
    title=f"Efficiency Distribution (Machine-{machine_selected})",color=dist.loc[machine_selected].index,
    color_discrete_map={'Low': 'red', 'Medium': 'orange', 'High': 'green'})
fig.update_traces(texttemplate='%{y:.2f}', textposition='auto')
st.plotly_chart(fig)
# -------------------------
# 3. MACHINE DISTRIBUTION
# -------------------------
st.subheader("📊 Machine Efficiency Distribution")

st.dataframe(dist)



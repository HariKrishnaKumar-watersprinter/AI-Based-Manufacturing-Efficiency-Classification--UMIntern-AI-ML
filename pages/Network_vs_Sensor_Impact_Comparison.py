import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.Network_vs_Sensor_Impact import network_vs_sensor_impact
import plotly.express as px

st.subheader("📡 Network vs Sensor Impact Comparison")

impact = network_vs_sensor_impact()

impact_df = pd.DataFrame({
    "Category": list(impact.keys()),
    "Impact Score": list(impact.values())
})

fig = px.bar(
    impact_df,
    x="Category",
    y="Impact Score",
    title="Network vs Sensor Impact Comparison",
    color="Impact Score",
    color_continuous_scale="Viridis"
)
fig.update_traces(texttemplate='%{y}', textposition='auto')
st.plotly_chart(fig)

st.write("""
**Interpretation:**
- Higher score indicates stronger influence on efficiency
- Helps prioritize infrastructure vs machine optimization
""")
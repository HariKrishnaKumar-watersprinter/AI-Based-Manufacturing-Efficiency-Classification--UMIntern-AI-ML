import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_quality import data_quality_preprocessing
def show():
    df=data_quality_preprocessing()
    st.header("📊 Bivariate Analysis")

    col1 = st.selectbox("Feature", df.columns)
    col2 = 'Efficiency_Status'
    col3=df.groupby(col1)[col2].value_counts().reset_index(name='Count')
    
   
    if df[col1].dtype != 'object':
        fig = px.box(df, x=col2, y=col1, title=f"{col1} vs Efficiency_Status")
    else:
        fig = px.bar(col3, x=col1,y="Count",color=col2,barmode="group",title=f"{col1} vs Efficiency_Status")
        fig.update_traces(texttemplate='%{y:,.0f}', textposition='auto',textfont_size=50)

    st.plotly_chart(fig, width='stretch')
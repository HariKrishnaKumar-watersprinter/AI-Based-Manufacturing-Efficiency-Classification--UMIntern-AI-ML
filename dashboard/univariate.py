import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_quality import data_quality_preprocessing

def show():
    df=data_quality_preprocessing()
    st.header("📊 Univariate Analysis")

    column = st.selectbox("Select Column", df.columns)


    if df[column].dtype != 'object':
        fig = px.histogram(df, x=column, title=f"{column} Distribution",color_discrete_sequence=px.colors.qualitative.Pastel1)
        fig.update_traces(texttemplate='%{y:,.0f}', textposition='inside')
        
    else:
        fig = px.bar(df[column].value_counts(), title=f"{column} Counts",color_discrete_sequence=px.colors.qualitative.Pastel1)
        fig.update_traces(texttemplate='%{y:,.0f}', textposition='auto',textfont_size=50)

    st.plotly_chart(fig)
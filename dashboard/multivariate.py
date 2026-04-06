import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_quality import data_quality_preprocessing
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def show():
    df = data_quality_preprocessing()
    st.header("📊 Multivariate Analysis")

    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f',center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8},
            vmin=-1, vmax=1,mask=np.triu(np.ones_like(corr, dtype=bool)))
    plt.title('Correlation Heatmap of Numerical Features',fontweight='bold')
    st.pyplot(plt)

    

    

    #fig = px.scatter_matrix(df,
        #dimensions=["Age", "Balance", "EstimatedSalary"], color="Exited")
    #st.plotly_chart(fig)



import streamlit as st
import pandas as pd
import plotly.express as px
from src.eda import numerical_stats
from src.data_quality import data_quality_preprocessing
def show():
    df=data_quality_preprocessing()
    st.header("📊 Numerical Analysis")


    stats = numerical_stats()
    st.dataframe(stats)     
    st.write("""The above table shows the summary statistics of the numerical features in the dataset.
        The mean, median, mode, standard deviation, minimum, and maximum values are provided for each feature. 
        This information can be useful for understanding the distribution and central tendency of the data, as well as for identifying any potential outliers or anomalies.""")
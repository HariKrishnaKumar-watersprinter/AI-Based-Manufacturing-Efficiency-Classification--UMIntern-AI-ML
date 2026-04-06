import streamlit as st
import pandas as pd
import plotly.express as px
from dashboard import univariate
from dashboard import bivariate
from dashboard import multivariate
from dashboard import numerical
from src.data_quality import data_quality_preprocessing

#if not st.session_state.get('authentication_status'):
#    st.switch_page("app.py")

df=data_quality_preprocessing()
st.header("📊 Exploratory Data Analysis")
tabs = st.tabs([
        "Univariate",
        "Bivariate",
        "Multivariate",
        "Numerical"
    ])

    # -------------------------
    # UNIVARIATE
    # -------------------------
with tabs[0]:
        univariate.show()

    # -------------------------
    # BIVARIATE
    # -------------------------
with tabs[1]:
        bivariate.show()

       

    # -------------------------
    # MULTIVARIATE
    # -------------------------
with tabs[2]:
        multivariate.show()

    # -------------------------
    # NUMERICAL
    # -------------------------
with tabs[3]:
        numerical.show()
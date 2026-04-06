import streamlit as st
import pandas as pd
from src.data_validation import DataValidator
from src.data_quality import data_quality_preprocessing
st.title("✅ Data Validation Dashboard")


df=data_quality_preprocessing()
validator = DataValidator(df)
report = validator.run_all_checks()

st.subheader("🚨 Errors")
if report['errors']:
    for err in report['errors']:
        st.error(err)
else:
    st.success("No critical errors found")

st.subheader("⚠️ Warnings")
if report['warnings']:
    for warn in report['warnings']:
        st.warning(warn)
else:
    st.success("No warnings")
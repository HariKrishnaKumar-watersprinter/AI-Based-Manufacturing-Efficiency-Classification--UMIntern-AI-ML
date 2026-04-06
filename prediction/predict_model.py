import joblib
import pandas as pd
from src.preprocessing import scale_features
import streamlit as st
import os

@st.cache_resource
def load_prediction_model():
    model_path = os.path.join(os.getcwd(), "best model", "GradientBoosting_OverSampling.pkl")
    return joblib.load(model_path)

def predict_eff(input_df):
    model = load_prediction_model()
    numeric_pipeline, _,_= scale_features() 
    
    # Transform and reconstruct DataFrame to preserve feature names for the model
    cols = input_df.columns
    transformed_data = numeric_pipeline.transform(input_df)
    input_df_scaled = pd.DataFrame(transformed_data, columns=cols)
    
    prob = model.predict_proba(input_df_scaled)
    pred = model.predict(input_df_scaled)
    return prob, pred, model
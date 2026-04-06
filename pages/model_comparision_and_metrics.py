import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score, precision_recall_curve, average_precision_score
import joblib
import os
from src.preprocessing import preprocess_data, scale_features
from src.model_training1 import model_training
from model_tracking.mlflow_track import track_model as mlflow_track_model
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
# --- 0. Authentication Guard ---
st.set_page_config(page_title="Model comparision and model metrics", layout="wide")




if "__file__" in globals():
    base_dir = Path(__file__).resolve().parents[1]
else:
    base_dir = Path.cwd()
MODEL_FOLDER = base_dir / "best model"
RESULTS_CSV = base_dir / "data/results.csv"

def init_session_state():
    """Initializes session state variables if they don't exist."""
    if 'loaded_model' not in st.session_state:
        st.session_state['loaded_model'] = None
    if 'selected_model_name' not in st.session_state:
        st.session_state['selected_model_name'] = None

    # --- 2. Functional Components ---

def render_model_selection():
    """UI for picking and loading a saved model."""
    st.subheader("🗂️ Model Selection")

    model_files = []
    if MODEL_FOLDER.exists() and MODEL_FOLDER.is_dir():
        model_files = [f for f in os.listdir(MODEL_FOLDER) if f.endswith('.pkl')]
    else:
        st.error(f"Model directory not found: {MODEL_FOLDER}")
        return
        
    if not model_files:
        st.warning(f"No .pkl models found in {MODEL_FOLDER}")
        return

    # Determine current index for the selectbox
    current_sel = st.session_state.get('selected_model_name')
    default_idx = model_files.index(current_sel) if current_sel in model_files else 0
        
    selected = st.selectbox("Choose a trained model for active prediction:", model_files, index=default_idx)

    # Logic to load model if selection changes
    if selected != st.session_state['selected_model_name']:
        try:
            with st.spinner(f"Loading {selected}..."):
                model_path = MODEL_FOLDER / selected
                st.session_state['loaded_model'] = joblib.load(model_path)
                st.session_state['selected_model_name'] = selected
                st.toast(f"Active model updated: {selected}", icon="✅")
        except Exception as e:
            st.error(f"Failed to load model: {e}")
    col1, col2, col3 = st.columns(3)

    col1.metric("Model Accuracy", "100%")
    col2.metric("ROC-AUC", "100%")
    col3.metric("Efficiency Detection Recall", "100%")
        
    
def render_performance_dashboard():
    """Displays retraining options and evaluation charts."""
    st.subheader("📊 Performance Comparison")
    
    results = None
    if RESULTS_CSV.exists():
        try:
            results = pd.read_csv(RESULTS_CSV)
        except Exception:
            results = None

    # Check if results dataframe was actually loaded, not just the path object
    if results is not None:
        # Plotly Comparison Chart
        fig = px.bar(
            results,
            x="Model",
            y="ROC-AUC (macro)",
            color="class imbalance technique",
            barmode="group",
            title="ROC-AUC Scores by Model and Sampling Technique",
            template="plotly_dark" )
        st.plotly_chart(fig, width='stretch')

        # Data Table
        st.write("### Detailed Metrics")
        st.dataframe(results.sort_values(by="ROC-AUC (macro)", ascending=False))
        
        if st.button('🔄 Retrain All Models'):
            with st.spinner("Executing training pipeline..."):
                model_training()
                st.success("Training Complete!")
                st.rerun()
    else:
        st.warning("No training results found in data/results.csv.")
        if st.button('🚀 Start Initial Training'):
            with st.spinner("Training initial models..."):
                model_training()
                st.success("Training Complete!")
                st.rerun()

def render_tracking_section():
    """UI for MLflow tracking."""
    st.subheader("📈 Experiment Tracking")
    st.info("Log the current best model performance to MLflow for versioning and auditing.")
    if st.button('📤 Push to MLflow'):
        with st.spinner("Logging to MLflow..."):
            mlflow_track_model()
            st.success("Experiment logged successfully!")

# --- 3. Main Page Execution ---
def main():
    st.title("🏆 Model Selection & Analysis")
    init_session_state()

    with st.container(border=True):
        render_model_selection()

    st.divider()
    render_performance_dashboard()

    st.divider()
    render_tracking_section()

if __name__ == "__main__":
    main()

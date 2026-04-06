import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt
from src.data_quality import data_quality_preprocessing
from src.preprocessing import scale_features
from prediction.predict_model import load_prediction_model
st.title("🧠 Explainability Panel")

model = load_prediction_model()
df = data_quality_preprocessing()
_,x_train_scaled,_= scale_features()
sample = x_train_scaled.sample(200)

# Using the generic Explainer to support multi-class GradientBoosting
explainer = shap.Explainer(model.named_steps['model'].predict, sample)
shap_values = explainer(sample)
importance = pd.Series(model.named_steps['model'].feature_importances_,index=sample.columns).sort_values(ascending=False)

st.subheader("Feature Importance")
fig = shap.plots.bar(shap_values, show=False)
fig = plt.gcf()
st.pyplot(fig)
plt.clf()
st.subheader("Global Feature Importance")

fig, ax = plt.subplots()
shap.summary_plot(shap_values, sample, show=False, class_names=model.classes_)
st.pyplot(fig)
plt.clf()


st.subheader("🔍 Explain Single Prediction")

index = st.slider("Select Row", 0, len(sample)-1, 0)

samples= sample.iloc[[index]]

prediction = model.predict(samples)[0]
proba = model.predict_proba(samples).max()

st.write(f"### Prediction: {prediction}")
st.write(f"### Confidence: {proba:.2f}")

st.write("### Feature Contributions:")

sample_shap = shap_values[index].values

contrib_df = pd.DataFrame({
    "Feature": sample.columns,
    "Contribution": sample_shap
}).sort_values(by="Contribution", ascending=False)

st.dataframe(contrib_df)
st.progress(int(proba * 100))
def generate_reason(contrib_df):

    top_positive = contrib_df.head(3)
    top_negative = contrib_df.tail(3)

    reason = "Efficiency decision based on:\n"

    reason += "\n🔺 Increasing Factors:\n"
    for _, row in top_positive.iterrows():
        reason += f"- {row['Feature']}\n"

    reason += "\n🔻 Decreasing Factors:\n"
    for _, row in top_negative.iterrows():
        reason += f"- {row['Feature']}\n"

    return reason
st.subheader("🧾 Explanation (Human Readable)")

reason = generate_reason(contrib_df)
st.text(reason)
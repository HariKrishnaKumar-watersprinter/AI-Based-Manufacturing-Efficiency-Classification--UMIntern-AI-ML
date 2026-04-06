import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, f1_score,classification_report
from sklearn.metrics import roc_auc_score
from src.preprocessing import preprocess_data,scale_features
from src.model_training1 import model_training
from prediction.predict_model import load_prediction_model
import os
model_path = os.path.join(os.getcwd(), "best model", "GradientBoosting_OverSampling.pkl")
def track_model():
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Manufacturing efficiency prediction")
    with mlflow.start_run():
        x_train,x_test,y_train,y_test = preprocess_data()
        numeric_pipeline,x_train_scaled,x_test_scaled= scale_features()
        model = load_prediction_model()
        _,_,_,grad_params,_=model_training()
        y_pred = model.predict(x_test_scaled)
        y_pred_prob = model.predict_proba(x_test_scaled)
        auc = roc_auc_score(y_test, y_pred_prob, multi_class='ovr', average='macro')
        recall_sc = recall_score(y_test, y_pred, average='macro')
        precision_sc = precision_score(y_test, y_pred, average='macro')
        f1_sc = f1_score(y_test, y_pred, average='macro')
        acc=accuracy_score(y_test, y_pred)
        

        mlflow.log_params(grad_params)
        mlflow.log_metric("Accuracy", acc)
        mlflow.log_metric("Recall macro", recall_sc)
        mlflow.log_metric("Precision macro", precision_sc)
        mlflow.log_metric("F1 Score macro", f1_sc)
        mlflow.log_metric("ROC-AUC macro", auc)
        mlflow.log_artifact(model_path)
        mlflow.set_tag('Training Info', 'Gradient boosting model for manufacturing efficiency prediction')
        signature = infer_signature(x_test_scaled, model.predict(x_test_scaled))
        mlflow.sklearn.log_model(sk_model=model, artifact_path="manufacturing_efficiency_model", 
                          signature=signature,input_example=x_test_scaled,registered_model_name="Manufacturing efficiency model")
        print("Model logged in MLflow")

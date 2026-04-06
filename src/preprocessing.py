import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from src.data_quality import data_quality_preprocessing
from sklearn.pipeline import Pipeline

def preprocess_data():
    df = data_quality_preprocessing()
    # Drop irrelevant columns
    df.drop(['Machine_ID', 'Timestamp','Date','Datetime'], axis=1, inplace=True)

    # One-hot encoding
    df = pd.get_dummies(df, columns=['Operation_Mode'],dtype=int)
    #Targetencoding
    df['Efficiency_Status'] = df['Efficiency_Status'].map({'High': 2, 'Low': 0, 'Medium': 1})
    #splitting the data
    x=df.drop('Efficiency_Status',axis=1)
    y=df['Efficiency_Status']
    #train_test split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
    return x_train,x_test,y_train,y_test


def scale_features():
    # Scaling
    x_train,x_test,y_train,y_test=preprocess_data()
    numeric_pipeline = Pipeline([("scaler", RobustScaler())])
    x_train_scaled = numeric_pipeline.fit_transform(x_train)
    x_test_scaled = numeric_pipeline.transform(x_test)
    x_train_scaled=pd.DataFrame(x_train_scaled,columns=x_train.columns)
    x_test_scaled=pd.DataFrame(x_test_scaled,columns=x_test.columns)
    return (numeric_pipeline,x_train_scaled,x_test_scaled)
import pandas as pd
import os

def load_data():
    os.chdir(r'https://raw.github.com/HariKrishnaKumar-watersprinter/AI-Based-Manufacturing-Efficiency-Classification--UMIntern-AI-ML/main/data/Thales_Group_Manufacturing.csv')
    path = os.path.join(os.getcwd(), "data", "Thales_Group_Manufacturing.csv")
    
    df = pd.read_csv(path)
    
    return df

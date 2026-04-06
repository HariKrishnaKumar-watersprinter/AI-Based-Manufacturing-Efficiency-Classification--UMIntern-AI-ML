import pandas as pd
import os

def load_data():
    os.chdir('F:\\Project\\unified mentor\\AI-Based Manufacturing Efficiency Classification')
    path = os.path.join(os.getcwd(), "data", "Thales_Group_Manufacturing.csv")
    
    df = pd.read_csv(path)
    
    return df
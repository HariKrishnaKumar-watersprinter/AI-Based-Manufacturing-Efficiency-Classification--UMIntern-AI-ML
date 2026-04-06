import pandas as pd
from src.data_loader import load_data

def create_features():
    df=load_data()
    df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Timestamp'],format='%d-%m-%Y %H:%M:%S')
    # Sensor Stability (rolling std)
    df['Temp_Stability'] = df['Temperature_C'].rolling(window=5).std()
    df['Vibration_Stability'] = df['Vibration_Hz'].rolling(window=5).std()

    # Energy Efficiency
    df['Energy_per_Unit'] = df['Power_Consumption_kW'] / (df['Production_Speed_units_per_hr'] + 1)

    # Error-to-output ratio
    df['Error_to_Output'] = df['Error_Rate_%'] / (df['Production_Speed_units_per_hr'] + 1)

    # Network reliability score
    df['Network_Reliability'] = 100 - (df['Packet_Loss_%'] + df['Network_Latency_ms'] * 0.1)
    
    df1=df.copy()
    
    return df1
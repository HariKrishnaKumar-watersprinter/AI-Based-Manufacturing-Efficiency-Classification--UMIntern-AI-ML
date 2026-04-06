import pandas as pd
from src.data_quality import data_quality_preprocessing

df=data_quality_preprocessing()
def network_vs_sensor_impact():

        network_features = [
            'Network_Latency_ms',
            'Packet_Loss_%'
        ]

        sensor_features = [
            'Temperature_C',
            'Vibration_Hz',
            'Power_Consumption_kW'
        ]

        # Encode target
        df_temp = df.copy()
        mapping = {'Low': 0, 'Medium': 1, 'High': 2}
        df_temp['Efficiency_Num'] = df_temp['Efficiency_Status'].map(mapping)

        # Correlation-based impact
        network_impact = df_temp[network_features + ['Efficiency_Num']].corr()['Efficiency_Num'][:-1].abs().mean()
        sensor_impact = df_temp[sensor_features + ['Efficiency_Num']].corr()['Efficiency_Num'][:-1].abs().mean()

        return {
            "Network Impact": round(network_impact, 3),
            "Sensor Impact": round(sensor_impact, 3)
        }
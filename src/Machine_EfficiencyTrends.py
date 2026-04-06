import pandas as pd
from src.data_quality import data_quality_preprocessing
df=data_quality_preprocessing()

    # -------------------------
    # 2. Per-Machine Efficiency Trends
    # -------------------------
def machine_trends():

        df_temp = df.copy()

        # Combine Date + Time
        df_temp['Datetime'] = pd.to_datetime(df_temp['Date'] + " " + df_temp['Timestamp'],format='%d-%m-%Y %H:%M:%S')

        trend_df = df_temp.groupby(['Machine_ID', 'Datetime'])['Efficiency_Status'].first().reset_index()

        return trend_df

    # -------------------------
    # 3. Machine Efficiency Distribution
    # -------------------------
def machine_efficiency_distribution():

        dist = df.groupby('Machine_ID')['Efficiency_Status'].value_counts(normalize=True).unstack().fillna(0)*100

        return dist

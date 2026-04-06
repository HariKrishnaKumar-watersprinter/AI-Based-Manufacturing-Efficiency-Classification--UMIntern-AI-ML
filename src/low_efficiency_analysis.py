import pandas as pd
import numpy as np
from src.data_quality import data_quality_preprocessing
class LowEfficiencyAnalyzer:

    def __init__(self):
        self.df = data_quality_preprocessing()

    # -------------------------
    # 1. FILTER LOW EFFICIENCY
    # -------------------------
    def get_low_efficiency_data(self):
        return self.df[self.df['Efficiency_Status'] == 'Low']

    # -------------------------
    # 2. ROOT CAUSE ANALYSIS
    # -------------------------
    def root_cause_analysis(self):

        low_df = self.get_low_efficiency_data()
        overall_df = self.df

        insights = {}

        numeric_cols = [
            'Temperature_C','Vibration_Hz','Power_Consumption_kW',
            'Network_Latency_ms','Packet_Loss_%',
            'Quality_Control_Defect_Rate_%',
            'Production_Speed_units_per_hr',
            'Predictive_Maintenance_Score','Error_Rate_%'
        ]

        for col in numeric_cols:
            low_mean = low_df[col].mean()
            overall_mean = overall_df[col].mean()

            diff = round(low_mean - overall_mean, 2)

            insights[col] = {
                "Low Mean": round(low_mean, 2),
                "Overall Mean": round(overall_mean, 2),
                "Difference": diff
            }

        return pd.DataFrame(insights).T.sort_values(by="Difference", ascending=False)

    # -------------------------
    # 3. TOP CAUSES
    # -------------------------
    def identify_top_causes(self, threshold_high=5, threshold_low=-5):

        df_analysis = self.root_cause_analysis()

        # High positive difference → bad factors
        top_issues = df_analysis[(df_analysis['Difference'] > threshold_high) | (df_analysis['Difference'] < threshold_low)]

        return top_issues

    # -------------------------
    # 4. RECOMMENDED ACTIONS
    # -------------------------
    def recommended_actions(self):

        causes = self.identify_top_causes()

        actions = []

        for feature in causes.index:

            if "Error_Rate" in feature:
                actions.append("Reduce operational errors via process optimization")

            elif "Packet_Loss" in feature:
                actions.append("Improve network reliability and reduce packet loss")

            elif "Latency" in feature:
                actions.append("Upgrade 6G infrastructure to reduce latency")

            elif "Temperature" in feature:
                actions.append("Implement temperature control systems")

            elif "Vibration" in feature:
                actions.append("Inspect mechanical components for wear and imbalance")

            elif "Power_Consumption" in feature:
                actions.append("Optimize energy usage and detect inefficiencies")

            elif "Production_Speed" in feature:
                actions.append("Improve throughput via workflow optimization")

            elif "Defect_Rate" in feature:
                actions.append("Enhance quality control mechanisms")

            elif "Predictive_Maintenance" in feature:
                actions.append("Schedule immediate maintenance checks")

        return list(set(actions))

    # -------------------------
    # 5. PROACTIVE ACTIONS
    # -------------------------
    def proactive_actions(self):

        return [
            "Deploy real-time monitoring dashboards for early anomaly detection",
            "Implement predictive maintenance models to prevent failures",
            "Set automated alerts for threshold breaches (latency, error rate)",
            "Continuously optimize network performance (6G infrastructure)",
            "Use AI-based scheduling to balance machine load",
            "Conduct periodic sensor calibration",
            "Introduce adaptive control systems for dynamic optimization"
        ]
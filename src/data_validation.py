import pandas as pd
import numpy as np

class DataValidator:

    def __init__(self, df):
        self.df = df
        self.errors = []
        self.warnings = []

    # -------------------------
    # 1. Schema Validation
    # -------------------------
    def validate_schema(self):

        expected_columns = [
            'Date', 'Timestamp', 'Machine_ID', 'Operation_Mode', 'Temperature_C',
       'Vibration_Hz', 'Power_Consumption_kW', 'Network_Latency_ms',
       'Packet_Loss_%', 'Quality_Control_Defect_Rate_%',
       'Production_Speed_units_per_hr', 'Predictive_Maintenance_Score',
       'Error_Rate_%', 'Efficiency_Status'
        ]

        missing_cols = set(expected_columns) - set(self.df.columns)

        if missing_cols:
            self.errors.append(f"Missing Columns: {missing_cols}")

    # -------------------------
    # 2. Data Type Validation
    # -------------------------
    def validate_dtypes(self):

        numeric_cols = [
            'Temperature_C','Vibration_Hz','Power_Consumption_kW',
            'Network_Latency_ms','Packet_Loss_%',
            'Quality_Control_Defect_Rate_%',
            'Production_Speed_units_per_hr',
            'Predictive_Maintenance_Score','Error_Rate_%'
        ]

        for col in numeric_cols:
            if not pd.api.types.is_numeric_dtype(self.df[col]):
                self.errors.append(f"{col} should be numeric")

    # -------------------------
    # 3. Missing Values
    # -------------------------
    def validate_missing(self):

        missing = self.df.isnull().sum()

        for col, val in missing.items():
            if val > 0:
                self.warnings.append(f"{col} has {val} missing values")

    # -------------------------
    # 4. Range Checks (DOMAIN RULES)
    # -------------------------
    def validate_ranges(self):

        rules = {
            'Temperature_C': (0, 150),
            'Vibration_Hz': (0, 1000),
            'Power_Consumption_kW': (0, 1000),
            'Network_Latency_ms': (0, 200),
            'Packet_Loss_%': (0,5),
            'Quality_Control_Defect_Rate_%': (0, 5),
            'Error_Rate_%': (0, 5),
            'Production_Speed_units_per_hr': (0, 1000)
        }

        for col, (min_val, max_val) in rules.items():
            invalid = self.df[(self.df[col] < min_val) | (self.df[col] > max_val)]
            if not invalid.empty:
                self.errors.append(f"{col} out of range")

    # -------------------------
    # 5. Categorical Validation
    # -------------------------
    def validate_categories(self):

        valid_modes = ['Idle', 'Active', 'Maintenance']

        invalid_modes = self.df[~self.df['Operation_Mode'].isin(valid_modes)]

        if not invalid_modes.empty:
            self.warnings.append("Invalid Operation_Mode values found")

    # -------------------------
    # 6. Time Validation
    # -------------------------
    def validate_datetime(self):

        try:
            self.df['Datetime'] = pd.to_datetime(
                self.df['Date'] + " " + self.df['Timestamp'],format='%d-%m-%Y %H:%M:%S')
        except:
            self.errors.append("Invalid Date/Time format")

    # -------------------------
    # 7. Duplicate Check
    # -------------------------
    def validate_duplicates(self):

        dup = self.df.duplicated().sum()
        if dup > 0:
            self.warnings.append(f"{dup} duplicate rows found")

    # -------------------------
    # 8. Outlier Detection (IQR)
    # -------------------------
    def detect_outliers(self):

        for col in self.df.select_dtypes(include=np.number).columns:

            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1

            outliers = self.df[
                (self.df[col] < q1 - 1.5 * iqr) |
                (self.df[col] > q3 + 1.5 * iqr)
            ]

            if len(outliers) > 0:
                self.warnings.append(f"{col} has {len(outliers)} outliers")

    # -------------------------
    # FINAL REPORT
    # -------------------------
    def run_all_checks(self):

        self.validate_schema()
        self.validate_dtypes()
        self.validate_missing()
        self.validate_ranges()
        self.validate_categories()
        self.validate_datetime()
        self.validate_duplicates()
        self.detect_outliers()

        return {
            "errors": self.errors,
            "warnings": self.warnings}
import streamlit as st
import pandas as pd
import joblib
from prediction.predict_model import predict_eff,load_prediction_model
from database.database_create import save_data
from datetime import datetime
from src.low_efficiency_analysis import LowEfficiencyAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
def pred():
    st.title("🔮 Efficiency Prediction")

    tab1,tab2=st.tabs(["Prediction with csv","Prediction with manual input"])
    with tab1:
        uploaded_file = st.file_uploader("Upload new machine data CSV")
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            df1=df.copy()
            #df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Timestamp'],format='%d-%m-%Y %H:%M:%S')
            # Sensor Stability (rolling std)
            df['Temp_Stability'] = df['Temperature_C'].rolling(window=5).std()
            df['Vibration_Stability'] = df['Vibration_Hz'].rolling(window=5).std()

            # Energy Efficiency
            df['Energy_per_Unit'] = df['Power_Consumption_kW'] / (df['Production_Speed_units_per_hr'] + 1)

            # Error-to-output ratio
            df['Error_to_Output'] = df['Error_Rate_%'] / (df['Production_Speed_units_per_hr'] + 1)

            # Network reliability score
            df['Network_Reliability'] = 100 - (df['Packet_Loss_%'] + df['Network_Latency_ms'] * 0.1)
            
           # One-hot encoding
            df = pd.get_dummies(df, columns=['Operation_Mode'],dtype=int)
            #Targetencoding
            #df['Efficiency_Status'] = df['Efficiency_Status'].map({'High': 2, 'Low': 0, 'Medium': 1})
            
            df.drop(['Machine_ID', 'Timestamp','Date'], axis=1, inplace=True)
            df.fillna(df.isnull().sum().mean(), inplace=True)
            possible_cols = [
                'Temperature_C', 'Vibration_Hz', 'Power_Consumption_kW',
               'Network_Latency_ms', 'Packet_Loss_%', 'Quality_Control_Defect_Rate_%',
               'Production_Speed_units_per_hr', 'Predictive_Maintenance_Score',
               'Error_Rate_%', 'Temp_Stability', 'Vibration_Stability',
               'Energy_per_Unit', 'Error_to_Output', 'Network_Reliability',
               'Operation_Mode_Active', 'Operation_Mode_Idle',
               'Operation_Mode_Maintenance']
            df = df.reindex(columns=possible_cols)
            prob, pred, model = predict_eff(df)
                    
            # Vectorized mapping for multi-row predictions
            label_map = {0: 'Low', 1: 'Medium', 2: 'High'}
            df1['Predicted_Efficiency'] = pd.Series(pred).map(label_map).values
            df1['Confidence'] = prob.max(axis=1)

            st.dataframe(df1)
            csv = df1.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Prediction History (CSV)",
                data=csv,
                file_name="efficiency_prediction_history.csv",
                mime="text/csv",
                help="Click to download all saved prediction records as a CSV file.")
            
            st.subheader("📊 Prediction Distribution")
            st.bar_chart(df1['Predicted_Efficiency'].value_counts(ascending=False))
            st.subheader("📉 Low Efficiency Data")
            low_eff = df1[df1['Predicted_Efficiency']=="Low"]
            st.dataframe(low_eff)

            st.title("⚠️ Low Efficiency Analysis & Action Center")


            analyzer = LowEfficiencyAnalyzer()

# -------------------------
# 1. ROOT CAUSE ANALYSIS
# -------------------------
            st.subheader("🔍 Root Cause Analysis")

            analysis_df = analyzer.root_cause_analysis()

            st.dataframe(analysis_df)

# Visualization
            if not low_eff.empty:
                
                st.write("Top contributing factors for LOW efficiency:")
                
                st.bar_chart(analysis_df['Difference'])

# -------------------------
# 2. TOP CAUSES
# -------------------------
            st.subheader("🚨 Top Contributing Factors")

            top_causes = analyzer.identify_top_causes()

            st.dataframe(top_causes)

# -------------------------
# 3. RECOMMENDED ACTIONS
# -------------------------
            st.subheader("🛠️ Recommended Actions")

            actions = analyzer.recommended_actions()

            for act in actions:
                st.warning(act)

# -------------------------
# 4. PROACTIVE ACTIONS
# -------------------------
            st.subheader("🚀 Proactive Strategies")

            proactive = analyzer.proactive_actions()

            for p in proactive:
                st.success(p)   
            for _, row in df1.iterrows():
                save_data(
                    Date=row['Date'],
                    Timestamp=row['Timestamp'],
                    MachineID=row['Machine_ID'],
                    Operation_Mode=row['Operation_Mode'],
                    Temperature_C=row['Temperature_C'],
                    Vibration_Hz=row['Vibration_Hz'],
                    Power_Consumption_kW=row['Power_Consumption_kW'],
                    Network_Latency_ms=row['Network_Latency_ms'],
                    Packet_Loss=row['Packet_Loss_%'],
                    Quality_Control_Defect_Rate=row['Quality_Control_Defect_Rate_%'],
                    Production_Speed_units_per_hr=row['Production_Speed_units_per_hr'],
                    Predictive_Maintenance_Score=row['Predictive_Maintenance_Score'],
                    Error_Rate=row['Error_Rate_%'],
                    prediction_Efficiency=row['Predicted_Efficiency'],
                    prediction_Confidence=row['Confidence']
                )
            st.success("Data saved successfully")
        
    with tab2:
        
        st.markdown("### Enter the machine details to predict efficiency")
        col1, col2 = st.columns(2)
    

        with col1:
            MachineID=st.number_input('MachineID',0,16000000,0)
            Operation_Mode = st.selectbox("Operation Mode", ["Idle","Active",'Maintenance'])
            Temperature_C = st.number_input("Temperature_C", 0.000, 150.000, 00.000)
            Vibration_Hz = st.number_input("Vibration_Hz", 0.000, 1000.000, 0.000)
            Power_Consumption_kW = st.number_input("Power_Consumption_kW", 0.000, 1000.000, 00.000)
            Network_Latency_ms = st.number_input("Network_Latency_ms", 0.000, 500.000, 00.000)
        
  
        with col2:
            Packet_Loss = st.number_input("Packet_Loss_%", 0.000,100.000,00.000)
            Quality_Control_Defect_Rate = st.number_input("Quality_Control_Defect_Rate_%", 0.000,100.000,00.000)
            Production_Speed_units_per_hr = st.number_input('Production_Speed_units_per_hr',0.000,10000.000,00.000)
            Predictive_Maintenance_Score = st.number_input("Predictive_Maintenance_Score", 0.000, 100.000, 00.000)
            Error_Rate = st.number_input("Error_Rate_%", 0.000, 100.000, 00.000)
        
        

        input_df = pd.DataFrame([{
            "MachineID": MachineID,
            "Operation_Mode": Operation_Mode,
            "Temperature_C": Temperature_C,
            "Vibration_Hz": Vibration_Hz,
            "Power_Consumption_kW": Power_Consumption_kW,
            "Network_Latency_ms": Network_Latency_ms,
            "Packet_Loss_%": Packet_Loss,   
            "Quality_Control_Defect_Rate_%": Quality_Control_Defect_Rate,   
            "Production_Speed_units_per_hr": Production_Speed_units_per_hr,
            "Predictive_Maintenance_Score": Predictive_Maintenance_Score,
            "Error_Rate_%": Error_Rate}])
    
        # Avoid division by zero
        input_df['Temp_Stability'] = input_df['Temperature_C'].rolling(window=5).std()
        input_df['Vibration_Stability'] = input_df['Vibration_Hz'].rolling(window=5).std()

        # Energy Efficiency
        input_df['Energy_per_Unit'] = input_df['Power_Consumption_kW'] / (input_df['Production_Speed_units_per_hr'] + 1)

        # Error-to-output ratio
        input_df['Error_to_Output'] = input_df['Error_Rate_%'] / (input_df['Production_Speed_units_per_hr'] + 1)

        # Network reliability score
        input_df['Network_Reliability'] = 100 - (input_df['Packet_Loss_%'] + input_df['Network_Latency_ms'] * 0.1)
        input_df1=input_df.copy()
    
        input_df = pd.get_dummies(input_df, columns=['Operation_Mode'], dtype=int)
        expected_columns = ['Operation_Mode_Idle', 'Operation_Mode_Active', 'Operation_Mode_Maintenance']
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df.fillna(input_df.isnull().sum().mean(), inplace=True)
        possible_cols = [
            'Temperature_C', 'Vibration_Hz', 'Power_Consumption_kW',
            'Network_Latency_ms', 'Packet_Loss_%', 'Quality_Control_Defect_Rate_%',
            'Production_Speed_units_per_hr', 'Predictive_Maintenance_Score',
            'Error_Rate_%', 'Temp_Stability', 'Vibration_Stability',
            'Energy_per_Unit', 'Error_to_Output', 'Network_Reliability',
            'Operation_Mode_Active', 'Operation_Mode_Idle',
            'Operation_Mode_Maintenance']
        input_df = input_df.reindex(columns=possible_cols)
   
    
        if st.button("Predict"):
            prob,pred,_ = predict_eff(input_df)
            st.write(f"# Machine ID: {int(MachineID)}")
            # Access individual element [0] and use correct training labels
            if pred[0] == 2:
                st.write(f"#### Efficiency Prediction: High")
            elif pred[0] == 1:
                st.write(f"#### Efficiency Prediction: Medium")
            else:
                st.write(f"#### Efficiency Prediction: Low")
            
            st.write(f"#### Efficiency Probability: {prob[0].max():.2f}")
            if pred[0] == 0 and prob[0].max() > 0.5:
                st.error("⚠️ machine is not efficient")
            else:
                st.success("✅ machine is efficient")
            #save_data(CustomerId,credit,geography,gender,age,tenure,balance,products,HasCrCard,active,salary)
            #st.success("Data saved successfully")
            
            # Save manual prediction data
            from datetime import datetime
            now = datetime.now()
            efficiency_label = "High" if pred[0] == 2 else ("Medium" if pred[0] == 1 else "Low")
            
            save_data(
                Date=now.strftime("%d-%m-%Y"),
                Timestamp=now.strftime("%H:%M:%S"),
                MachineID=MachineID,
                Operation_Mode=Operation_Mode,
                Temperature_C=Temperature_C,
                Vibration_Hz=Vibration_Hz,
                Power_Consumption_kW=Power_Consumption_kW,
                Network_Latency_ms=Network_Latency_ms,
                Packet_Loss=Packet_Loss,
                Quality_Control_Defect_Rate=Quality_Control_Defect_Rate,
                Production_Speed_units_per_hr=Production_Speed_units_per_hr,
                Predictive_Maintenance_Score=Predictive_Maintenance_Score,
                Error_Rate=Error_Rate,
                prediction_Efficiency=efficiency_label,
                prediction_Confidence=float(f"{prob[0].max():.2f}"))
            st.success("Data saved successfully")
            return input_df

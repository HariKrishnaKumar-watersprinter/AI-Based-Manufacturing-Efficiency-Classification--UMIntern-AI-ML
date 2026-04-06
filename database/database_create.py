import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, and_,or_,update,delete
from sqlalchemy.orm import declarative_base
import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

Base = declarative_base()


if "database" in st.secrets:
    DATABASE_URL = st.secrets['database']["url"]
    engine = sa.create_engine(DATABASE_URL, pool_pre_ping=True)
    st.info("✅ Connected to Supabase PostgreSQL")
else:
    model_path = os.path.join(os.getcwd(), "database", "manufacturing_efficiency.db")
    engine = sa.create_engine(f'sqlite:///{model_path}',connect_args={"check_same_thread": False})

    with engine.connect() as conn:
        conn.execute(sa.text("PRAGMA journal_mode=WAL;"))
        conn.commit()

class Effciencypred(Base):
    __tablename__ = 'Efficiency_Prediction_History'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    Date= sa.Column(sa.String, nullable=False)
    Timestamp = sa.Column(sa.String, nullable=False)
    MachineID = sa.Column(sa.Integer, nullable=False)
    Operation_Mode = sa.Column(sa.String, nullable=False)
    Temperature_C = sa.Column(sa.Float, nullable=False)
    Vibration_Hz = sa.Column(sa.Float, nullable=False)
    Power_Consumption_kW = sa.Column(sa.Float, nullable=False)
    Network_Latency_ms = sa.Column(sa.Float, nullable=False)
    Packet_Loss = sa.Column(sa.Float, nullable=False)
    Quality_Control_Defect_Rate = sa.Column(sa.Float, nullable=False)
    Production_Speed_units_per_hr = sa.Column(sa.Float, nullable=False)
    Predictive_Maintenance_Score = sa.Column(sa.Float, nullable=False)
    Error_Rate = sa.Column(sa.Float, nullable=False)
    prediction_Efficiency = sa.Column(sa.String, nullable=False)
    prediction_Confidence = sa.Column(sa.Float, nullable=False)
    

    
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

def save_data(Date,Timestamp,MachineID,Operation_Mode,Temperature_C,Vibration_Hz,Power_Consumption_kW,Network_Latency_ms,Packet_Loss,Quality_Control_Defect_Rate,Production_Speed_units_per_hr,Predictive_Maintenance_Score,Error_Rate,prediction_Efficiency,prediction_Confidence):
    
    Base.metadata.create_all(engine)
    # Insert new record
    new_prediction = Effciencypred(
                 Date=Date, Timestamp=Timestamp, MachineID=MachineID,
                Operation_Mode=Operation_Mode, Temperature_C=Temperature_C, 
                Vibration_Hz=Vibration_Hz, Power_Consumption_kW=Power_Consumption_kW, 
                Network_Latency_ms=Network_Latency_ms, Packet_Loss = Packet_Loss, 
                Quality_Control_Defect_Rate = Quality_Control_Defect_Rate, 
                Production_Speed_units_per_hr = Production_Speed_units_per_hr, 
                Predictive_Maintenance_Score = Predictive_Maintenance_Score, 
                Error_Rate = Error_Rate, prediction_Efficiency = prediction_Efficiency, 
                prediction_Confidence = prediction_Confidence)
    session = SessionLocal()
    try:
        session.add(new_prediction)
        session.commit()
    except Exception as e:
        session.rollback()  # This fixes the PendingRollbackError for future attempts
        raise e
    finally:
        session.close()

def get_all_data():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    try:
        return session.query(Effciencypred).all()
    finally:
        session.close()

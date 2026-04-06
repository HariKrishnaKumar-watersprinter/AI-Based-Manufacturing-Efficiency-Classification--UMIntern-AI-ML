import streamlit as st
from src.simulate_machine import simulate_machine


st.subheader("🏭 Digital Twin Simulation")

temp = st.slider("Temperature", 0, 200, 50)
vibration = st.slider("Vibration", 0, 200, 50)
latency = st.slider("Latency", 0, 200, 50)

result = simulate_machine(temp, vibration, latency)

st.success(f"Simulated Efficiency: {result}")
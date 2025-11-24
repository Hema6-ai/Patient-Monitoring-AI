import streamlit as st
import numpy as np
from patient_monitoring.monitor import PatientMonitor

st.title("Patient Health Monitoring AI")

monitor = PatientMonitor()

hr = st.number_input("Heart Rate (bpm)", 40, 180, 72)
spo2 = st.number_input("SpO2 (%)", 70, 100, 98)
temp = st.number_input("Body Temperature (°C)", 30.0, 42.0, 36.8)

if st.button("Analyze"):
    arr = monitor.preprocess(hr, spo2, temp)
    result = monitor.analyze(arr)

    st.subheader("Result:")
    st.write(result)

    st.subheader("History:")
    st.write(np.array(monitor.history))

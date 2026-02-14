import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

st.set_page_config(page_title="Pill-Sync Healthcare", page_icon="💊", layout="wide")

st.title("💊 Medication Adherence Dashboard")

if 'pill_log' not in st.session_state:
    st.session_state.pill_log = pd.DataFrame([
        {'Dose_Time': '08:00', 'Status': 'Taken', 'Delay_Min': 5},
        {'Dose_Time': '14:00', 'Status': 'Missed', 'Delay_Min': 0},
        {'Dose_Time': '20:00', 'Status': 'Scheduled', 'Delay_Min': 0}
    ])

placeholder = st.empty()

for _ in range(1): # Static display for setup
    with placeholder.container():
        c1, c2, c3 = st.columns(3)
        
        adherence = (st.session_state.pill_log['Status'] == 'Taken').mean() * 100
        c1.metric("Adherence Rate", f"{round(adherence)}%")
        c2.metric("Next Dose", "20:00")
        c3.metric("Device Status", "Online", delta="Secured")

        st.subheader("Daily Schedule")
        st.table(st.session_state.pill_log)

        if any(st.session_state.pill_log['Status'] == 'Missed'):
            st.error("🚨 ALERT: Afternoon dose was missed. Caregiver notified.")

        fig = px.pie(st.session_state.pill_log, names='Status', title="Patient Compliance Overview",
                     color_discrete_map={'Taken':'#2ecc71', 'Missed':'#e74c3c', 'Scheduled':'#95a5a6'})
    st.plotly_chart(fig, use_container_width=True)

"""
Panel de Control (Streamlit).
Lee continuamente la base de datos CSV generada por la API y visualiza
las métricas en tiempo real y el historial de los sensores en un dashboard interactivo.
"""
import streamlit as st
import pandas as pd
import time
import os

st.set_page_config(page_title="Centro de Control", layout="wide")
st.title("🛢️ Centro de Control - Pozo Alfa")
ARCHIVO_BD = "C:\\Users\\andre\\IA-PYTORCH-N8N-ETC\\data\\base_de_datos_pozo.csv"

if not os.path.exists(ARCHIVO_BD):
    st.warning("Esperando conexión con los sensores y la API...")
else:
    df = pd.read_csv(ARCHIVO_BD)
    
    if len(df) > 0:
        ultimo_dato = df.iloc[-1]
        
        st.subheader("Estado en Tiempo Real")
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperatura", f"{ultimo_dato['Temperatura']} °C")
        col2.metric("Vibracion", f"{ultimo_dato['Vibracion']} Hz")
        
        if ultimo_dato['Estado_IA'] == -1:
            col3.error("🚨 ALARMA DE FALLA MECÁNICA")
        else:
            col3.success("✅ Operación Normal")

        st.subheader("📈 Monitoreo de Sensores")
        df_reciente = df.tail(30)
        st.line_chart(df_reciente[["Temperatura", "Vibracion"]])

time.sleep(3)
st.rerun()

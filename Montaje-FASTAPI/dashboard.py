import streamlit as st
import pandas as pd
import numpy as np

# 1. Títulos y diseño de la página
st.set_page_config(page_title="Panel Petrolero", layout="wide")
st.title("🛢️ Panel de Control de Mantenimiento - Pozo Alfa")
st.write("Monitoreo en tiempo real de sensores y predicciones de IA.")

# 2. Barra lateral interactiva para que el gerente juegue con los valores
st.sidebar.header("🎛️ Simulador de Sensores")
temp_actual = st.sidebar.slider("Temperatura (°C)", min_value=50.0, max_value=120.0, value=80.0)
vib_actual = st.sidebar.slider("Vibración (Hz)", min_value=10.0, max_value=100.0, value=50.0)

# 3. Lógica (Aquí llamaríamos a la API o al modelo, simulamos la respuesta por ahora)
st.subheader("Estado Actual del Motor")
if temp_actual > 100 or vib_actual > 80:
    st.error(f"🚨 ALARMA DE FALLA PREDICTIVA: La IA detecta anomalías severas.")
else:
    st.success(f"✅ NORMAL: Los sensores indican que la máquina opera correctamente.")

# 4. Crear un gráfico falso de producción histórica para el Dashboard
st.subheader("📊 Historial de Producción (Últimos 30 días)")
fechas = pd.date_range(start="2024-01-01", periods=30)
produccion_simulada = np.random.normal(500, 20, size=30) # 500 barriles +- 20
df_grafico = pd.DataFrame({"Producción (bbl)": produccion_simulada}, index=fechas)

# Renderizar el gráfico con una sola línea de código
st.line_chart(df_grafico)
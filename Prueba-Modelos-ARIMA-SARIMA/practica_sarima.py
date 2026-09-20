"""
Modelo SARIMA para Series Temporales.
Extensión de ARIMA que incluye patrones estacionales (Seasonality) para predicciones cíclicas.
"""

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# 1. Creamos 14 días de historia (2 semanas)
# Fíjate en los números: 100 los días normales, 50 cada séptimo día.
datos = {
    "Fecha": pd.date_range(start="2024-01-01", periods=14, freq='D'),
    "Produccion_bbl": [
        100, 102, 99, 101, 100, 98, 50,  # Semana 1 (Día 7 es 50)
        101, 99, 100, 102, 98, 100, 50   # Semana 2 (Día 14 es 50)
    ]
}
df = pd.DataFrame(datos)
df.set_index("Fecha", inplace=True)

# 2. Creamos el modelo SARIMA
# Le decimos que el ciclo se repite cada 7 días (s=7)
modelo_sarima = SARIMAX(
    df["Produccion_bbl"], 
    order=(1, 0, 0),             # Tendencia diaria (básica)
    seasonal_order=(1, 0, 0, 7)  # El "7" le avisa del ciclo semanal
)

# 3. Entrenamos la IA
resultado = modelo_sarima.fit(disp=False)  # disp=False apaga textos innecesarios en la consola

# 4. Predecimos la próxima semana entera (7 días)
prediccion_semana_3 = resultado.forecast(steps=7)

print("=== PREDICCIÓN DE PRODUCCIÓN (SEMANA 3) ===")
print(prediccion_semana_3)
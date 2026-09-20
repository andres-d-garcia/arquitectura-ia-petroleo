"""
Modelo de Mantenimiento Predictivo.
Utiliza Isolation Forest (Aprendizaje No Supervisado) para detectar anomalías
en vibración y temperatura de maquinaria pesada.
"""

import pandas as pd
from sklearn.ensemble import IsolationForest

datos = {
    "Dia": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Temperatura_C": [80.1, 80.5, 79.8, 81.0, 80.2, 80.6, 79.9, 80.1, 80.4, 80.0,  105.5, 108.2],
    "Vibracion_Hz":  [50.2, 49.8, 50.1, 50.5, 49.9, 50.0, 50.2, 49.7, 50.3, 50.0,   85.0,  88.5]
}

df = pd.DataFrame(datos)
df.set_index("Dia", inplace=True)

print("=== ENTRENANDO SISTEMA DE DETECCIÓN DE ANOMALÍAS ===\n")


modelo_anomalias = IsolationForest(contamination=0.15, random_state=35)

# 3. Entrenamos la IA (¡Solo le damos la X! No hay variables 'y')
modelo_anomalias.fit(df[["Temperatura_C", "Vibracion_Hz"]])

# 4. Le pedimos a la IA que clasifique cada día del 1 al 12
# Devolverá 1 si es Normal, y -1 si detecta una Falla (Anomalía)
df["Prediccion_IA"] = modelo_anomalias.predict(df[["Temperatura_C", "Vibracion_Hz"]])

# 5. Traducimos el -1 y el 1 a palabras para que el panel de control se vea bien
df["Panel_Control"] = df["Prediccion_IA"].apply(lambda x: "🚨 ALARMA DE FALLA" if x == -1 else "✅ Normal")

print("=== RESULTADO DEL MONITOREO DE LA BOMBA ===")
print(df[["Temperatura_C", "Vibracion_Hz", "Panel_Control"]])
"""
Análisis Exploratorio de Series Temporales.
Manipulación y visualización de datos históricos ordenados cronológicamente usando Pandas.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
pd.set_option('display.max_columns', None)

datos_historicos = {
    "Fecha": pd.date_range(start="2024-01-01", periods=7, freq='D'),
    "Produccion_Petroleo_bbl": [300, 320, 310, 330, 340, 350, 360]
}

df = pd.DataFrame(datos_historicos)
df.set_index("Fecha", inplace=True)


df["Promedio_Movil_3dias"] = df["Produccion_Petroleo_bbl"].rolling(window=3).mean()
df["Produccion_Ayer"] = df["Produccion_Petroleo_bbl"].shift(1)
df["Produccion_2Dias_Atras"] = df["Produccion_Petroleo_bbl"].shift(2)


df_limpio = df.dropna()


print("=== TABLA LIMPIA PARA ENTRENAR LA IA ===")
print(df_limpio)

X = df_limpio[["Produccion_Ayer", "Produccion_2Dias_Atras"]]
y = df_limpio["Produccion_Petroleo_bbl"]

model = LinearRegression()
model.fit(X, y)

dia_siguiente = pd.DataFrame({
    "Produccion_Ayer": [360],
    "Produccion_2Dias_Atras": [350]
})

prediccion_futura = model.predict(dia_siguiente)
print(f'Predicción de producción para el día siguiente: {prediccion_futura[0]:.2f} bbl')
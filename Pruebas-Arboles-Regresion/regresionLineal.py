"""
Modelo de Regresión Lineal.
Entrenamiento de un algoritmo básico de Machine Learning para predecir tendencias numéricas.
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
from sklearn.linear_model import LinearRegression

datos = {
    'Presion_PSI': [3100, 3300, 3400, 3500, 3600],
    'Produccion_bbls': [100, 150, 200, 250, 300]
}

df = pd.DataFrame(datos)

X = df[['Presion_PSI']]
y = df['Produccion_bbls']

modelo = LinearRegression()
modelo.fit(X, y)

nueva_presion = pd.DataFrame({'Presion_PSI': [3700]})
prediccion = modelo.predict(nueva_presion)

print(f'Predicción de producción para una presión de 3700 PSI: {prediccion[0]} bbls')

"""
Análisis de Curva de Declinación (DCA).
Simula datos de producción histórica de un yacimiento y utiliza Regresión Lineal
con transformaciones logarítmicas para predecir el momento en que se cruzará el límite económico.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

meses_historia = np.arange(1, 61).reshape(-1, 1)
produccion_real = 1000 * np.exp(-0.03 * meses_historia.flatten()) + np.random.normal(0, 15, 60)

produccion_log = np.log(produccion_real)

modelo = LinearRegression()
modelo.fit(meses_historia, produccion_log)

meses_futuros = np.arange(61, 97).reshape(-1, 1)
prediccion_log = modelo.predict(meses_futuros)
prediccion_real = np.exp(prediccion_log) 

plt.figure(figsize=(10, 5))
plt.style.use('dark_background')
plt.scatter(meses_historia, produccion_real, color='white', label='Historia (5 años)', s=15)
plt.plot(meses_futuros, prediccion_real, color='red', linestyle='dashed', linewidth=3, label='Predicción IA')
plt.axhline(y=100, color='gray', linestyle='-', label='Límite Económico (100 bbl)')
plt.title("Análisis de Curva de Declinación de Yacimiento (IA)")
plt.xlabel("Meses de Operación")
plt.ylabel("Barriles de Petróleo por Día")
plt.legend()
plt.show()

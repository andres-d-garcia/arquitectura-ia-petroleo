import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. SIMULACIÓN DEL YACIMIENTO (5 Años de historia)
meses_historia = np.arange(1, 61).reshape(-1, 1) # 60 meses
# El pozo arranca en 1000 barriles diarios y cae 3% cada mes, más algo de ruido normal
produccion_real = 1000 * np.exp(-0.03 * meses_historia.flatten()) + np.random.normal(0, 15, 60)

# 2. EL TRUCO DE LA IA (Transformación Logarítmica)
# Aplastamos la curva para que la Regresión Lineal la pueda entender
produccion_log = np.log(produccion_real)

# 3. ENTRENAMIENTO DEL MODELO
modelo = LinearRegression()
modelo.fit(meses_historia, produccion_log)

# 4. PREDICCIÓN HACIA EL FUTURO (Próximos 3 años)
meses_futuros = np.arange(61, 97).reshape(-1, 1) # Del mes 61 al 96
prediccion_log = modelo.predict(meses_futuros)
# Deshacemos el truco logarítmico para volver a ver barriles reales
prediccion_real = np.exp(prediccion_log) 

# 5. DIBUJAR EL ANÁLISIS DEL YACIMIENTO
plt.figure(figsize=(10, 5))
plt.style.use('dark_background') # Un estilo oscuro y elegante

# Dibujamos el pasado (Puntos blancos)
plt.scatter(meses_historia, produccion_real, color='white', label='Historia (5 años)', s=15)

# Dibujamos el futuro de la IA (Línea roja)
plt.plot(meses_futuros, prediccion_real, color='red', linestyle='dashed', linewidth=3, label='Predicción IA (Próximos 3 años)')

# Dibujamos el Límite Económico (Ej. Menos de 100 barriles ya no da ganancias)
plt.axhline(y=100, color='gray', linestyle='-', label='Límite Económico (100 bbl)')

plt.title("Análisis de Curva de Declinación de Yacimiento (IA)")
plt.xlabel("Meses de Operación")
plt.ylabel("Barriles de Petróleo por Día")
plt.legend()
plt.show()
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


# 1. Nuestros datos históricos de producción (con una leve caída natural)
datos = {
    "Fecha": pd.date_range(start="2024-01-01", periods=6, freq='D'),
    "Produccion_bbl": [1000, 980, 950, 930, 900, 880]
}
df = pd.DataFrame(datos)
df.set_index("Fecha", inplace=True)

# 2. Inicializar y Entrenar la IA (ARIMA)
# Le pasamos toda la columna histórica, y la receta (p=1, d=1, q=1)
modelo_arima = ARIMA(df["Produccion_bbl"], order=(1, 1, 1))


resultado = modelo_arima.fit()


prediccion_futura = resultado.forecast(steps=2)

print("=== PREDICCIÓN DE PRODUCCIÓN (PRÓXIMOS 2 DÍAS) ===")
print(prediccion_futura)
"""
Pruebas iniciales de Machine Learning.
Script de exploración y manipulación básica de datos (Pandas) y modelos de Scikit-Learn.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text



dataset = {
    "Inyeccion_Agua_bbls": [100, 150, 200, 250, 300],
    "Presion_Yacimiento": [3100, 3300, 3400, 3500, 3600],
    "Produccion_Petroleo_bbl": [300, 450, 650, 800, 1000]
}

df = pd.DataFrame(dataset)
df["Es_Rentable"] = (df["Produccion_Petroleo_bbl"] > 600).astype(int)
X = df[["Inyeccion_Agua_bbls", "Presion_Yacimiento"]]
y = df["Produccion_Petroleo_bbl"]

modelo = LinearRegression()
modelo.fit(X, y)

pozo_nuevo = pd.DataFrame({"Inyeccion_Agua_bbls": [275], "Presion_Yacimiento": [3550]})
prediccion = modelo.predict(pozo_nuevo)
print(f'Predicción de producción para el nuevo pozo: {prediccion[0]} bbl')

X_clasif = df[["Inyeccion_Agua_bbls", "Presion_Yacimiento"]]
y_clasif = df["Es_Rentable"]

arbol = DecisionTreeClassifier()
arbol.fit(X_clasif, y_clasif)

categoria = arbol.predict(pozo_nuevo)
if categoria[0] == 1:
    print("El nuevo pozo es rentable.")
else:
    print("El nuevo pozo no es rentable.")

# Imprime las reglas de Sí/No en texto
reglas = export_text(arbol, feature_names=["Inyeccion_Agua_bbls", "Presion_Yacimiento"])
print(reglas)
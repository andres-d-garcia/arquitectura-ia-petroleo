"""
API del Pozo Petrolero (FastAPI).
Recibe datos de sensores IoT mediante peticiones POST, aplica una regla de negocio
para detectar anomalías (Mantenimiento Predictivo) y guarda el registro en un archivo CSV.
"""
from fastapi import FastAPI
import uvicorn
import pandas as pd
import os
from datetime import datetime

app = FastAPI()
ARCHIVO_BD = "C:\\Users\\andre\\IA-PYTORCH-N8N-ETC\\data\\base_de_datos_pozo.csv"

if not os.path.exists(ARCHIVO_BD):
    df_vacio = pd.DataFrame(columns=["Timestamp", "Temperatura", "Vibracion", "Estado_IA"])
    df_vacio.to_csv(ARCHIVO_BD, index=False)

@app.post("/sensor")
def recibir_datos(temperatura: float, vibracion: float):
    estado = -1 if (vibracion > 75.0 or temperatura > 100.0) else 1
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nuevo_dato = pd.DataFrame([{
        "Timestamp": hora_actual, 
        "Temperatura": temperatura, 
        "Vibracion": vibracion, 
        "Estado_IA": estado
    }])
    nuevo_dato.to_csv(ARCHIVO_BD, mode='a', header=False, index=False)
    
    return {"mensaje": "Dato guardado", "estado_detectado": estado}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

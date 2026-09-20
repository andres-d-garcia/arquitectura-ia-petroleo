"""
Servidor API Básico (FastAPI).
Introducción a la creación de endpoints web para exponer modelos de Machine Learning.
"""

from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def bienvenida():
    return {"mensaje": "Bienvenido al Servidor de Inteligencia Artificial de Chevron"}


@app.get("/predecir")
def predecir_estado(temperatura: float):
    # Por ahora es una simple regla de código, luego conectaremos la IA real
    if temperatura > 100:
        return {"estado": "🚨 ALARMA", "temperatura_recibida": temperatura}
    else:
        return {"estado": "✅ Normal", "temperatura_recibida": temperatura}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
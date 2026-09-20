"""
Simulador de Sensores IoT.
Genera lecturas aleatorias de temperatura y vibración (simulando una bomba física),
inyecta anomalías periódicamente y envía los datos a la API mediante HTTP POST.
"""
import time
import random
import requests

URL_API = "http://127.0.0.1:8000/sensor"
contador = 0

while True:
    contador += 1
    
    if contador % 10 != 0:
        temp = round(random.uniform(78.0, 82.0), 1)
        vib = round(random.uniform(48.0, 52.0), 1)
    else:
        temp = round(random.uniform(105.0, 115.0), 1)
        vib = round(random.uniform(80.0, 95.0), 1)

    parametros = {"temperatura": temp, "vibracion": vib}
    
    try:
        respuesta = requests.post(URL_API, params=parametros)
        resultado = respuesta.json()
        
        if resultado["estado_detectado"] == -1:
            print(f"[{contador}] Temp: {temp}°C, Vib: {vib}Hz --> 🚨 ALARMA")
        else:
            print(f"[{contador}] Temp: {temp}°C, Vib: {vib}Hz --> ✅ Normal")
    except Exception:
        print("❌ Error de conexión.")
        
    time.sleep(3)
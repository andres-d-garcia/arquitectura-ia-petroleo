import time
import random
import requests

# La dirección donde nuestro servidor FastAPI está escuchando
URL_API = "http://127.0.0.1:8000/sensor"

print("📡 Iniciando Simulador de Sensores IoT (Pozo Alfa)...")
print("Presiona Ctrl+C para detenerlo.\n")

contador = 0

while True:
    contador += 1
    
    # El 90% del tiempo, los sensores envían datos normales
    if contador % 10 != 0:
        temp = round(random.uniform(78.0, 82.0), 1)
        vib = round(random.uniform(48.0, 52.0), 1)
    else:
        # Cada 10 ciclos, inyectamos una FALLA MECÁNICA (Anomalía)
        print("\n⚠️ LA BOMBA ESTÁ EMPEZANDO A SOBRECALENTARSE...")
        temp = round(random.uniform(105.0, 115.0), 1)
        vib = round(random.uniform(80.0, 95.0), 1)

    # Empaquetamos los datos para enviarlos por URL
    parametros = {"temperatura": temp, "vibracion": vib}
    
    try:
        # Disparamos la petición POST a nuestra API
        respuesta = requests.post(URL_API, params=parametros)
        
        # Leemos lo que nos devolvió la IA desde el servidor
        resultado = respuesta.json()
        
        if resultado["estado_detectado"] == -1:
            print(f"[{contador}] Temp: {temp}°C, Vib: {vib}Hz --> 🚨 Servidor ordenó ALARMA")
        else:
            print(f"[{contador}] Temp: {temp}°C, Vib: {vib}Hz --> ✅ Servidor dice Normal")
            
    except Exception as e:
        print("❌ Error de conexión. ¿El servidor FastAPI (api_pozo.py) está encendido?")
        
    # Pausa de 3 segundos antes de tomar la siguiente lectura
    time.sleep(3)
import torch
import torch.nn as nn
import torch.optim as optim

# ==========================================
# 1. LA ARQUITECTURA (El Cerebro)
# ==========================================
class CerebroPetrolero(nn.Module):
    def __init__(self):
        super().__init__()
        # batch_first=True hace que el orden de los datos sea más fácil de leer
        self.memoria_lstm = nn.LSTM(input_size=1, hidden_size=50, batch_first=True)
        self.puerta_salida = nn.Linear(50, 1)

    def forward(self, datos):
        # La LSTM procesa la secuencia. Extraemos la memoria del ÚLTIMO día.
        salida_lstm, _ = self.memoria_lstm(datos)
        ultimo_paso = salida_lstm[:, -1, :] 
        prediccion = self.puerta_salida(ultimo_paso)
        return prediccion

mi_ia = CerebroPetrolero()

# ==========================================
# 2. LOS DATOS (Tensores)
# ==========================================
# Pistas (X): 4 días seguidos donde la producción cae (100, 90, 80, 70)
X_entrenamiento = torch.tensor([[[100.0], [90.0], [80.0], [70.0]]])

# Respuesta Correcta (y): Lo que pasó el Día 5 (Produjo 60)
y_correcto = torch.tensor([[60.0]])

# ==========================================
# 3. LAS HERRAMIENTAS DEL PROFESOR
# ==========================================
funcion_error = nn.MSELoss() 
optimizador = optim.Adam(mi_ia.parameters(), lr=0.05) # lr es la velocidad de aprendizaje

# ==========================================
# 4. EL BUCLE DE ENTRENAMIENTO (ÉPOCAS)
# ==========================================
print("=== INICIANDO ENTRENAMIENTO DE LA RED NEURONAL ===")

# Le haremos leer el mismo historial 100 veces (100 épocas)
for epoca in range(100): 
    
    # PASO A: La IA intenta adivinar usando la X
    prediccion = mi_ia(X_entrenamiento)
    
    # PASO B: Medimos qué tan equivocada está comparando con la 'y' real
    error = funcion_error(prediccion, y_correcto)
    
    # PASO C: El Optimizador ajusta las 50 neuronas para mejorar
    optimizador.zero_grad() # Limpia la pizarra
    error.backward()        # Calcula quién tuvo la culpa del error
    optimizador.step()      # Aplica la corrección matemática
    
    # Imprimimos en pantalla cada 20 épocas para ver cómo aprende en vivo
    if (epoca + 1) % 20 == 0:
        print(f"Época {epoca+1}/100 | Predicción de la IA: {prediccion.item():.2f} bbl (Meta: 60) | Error: {error.item():.2f}")

print("=== ENTRENAMIENTO FINALIZADO ===")
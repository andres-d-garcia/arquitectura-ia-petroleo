import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

# 1. SIMULAR UN MAPA SÍSMICO DEL SUBSUELO
# Creamos un fondo con "ruido" (rocas normales)
imagen_sismica = np.random.rand(100, 100) * 0.2

# Dibujamos matemáticamente un "Domo de Sal" (Una trampa donde se esconde el petróleo)
for x in range(100):
    y = int(50 - 20 * np.sin(x / 15.0))
    if 0 <= y < 100:
        imagen_sismica[y:y+5, x] = 1.0  # El eco sísmico rebota muy fuerte aquí

# 2. CONVERTIR LA IMAGEN A TENSOR DE PYTORCH
# A PyTorch le gustan las imágenes en formato: [Lote, CanalesDeColor, Alto, Ancho]
tensor_sismico = torch.tensor(imagen_sismica, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

# 3. LA ARQUITECTURA VISUAL (CNN)
class OjoGeologico(nn.Module):
    def __init__(self):
        super().__init__()
        # nn.Conv2d es nuestra "Lupa". Un filtro de 3x3 pixeles que escanea la imagen
        self.lupa = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=1)
        
    def forward(self, imagen):
        # La imagen pasa por la lupa
        mapa_de_caracteristicas = self.lupa(imagen)
        # Usamos ReLU (una función matemática) para apagar los pixeles irrelevantes
        return torch.relu(mapa_de_caracteristicas)

# 4. INSTANCIAR LA IA Y HACERLE "MIRAR" LA IMAGEN
mi_ia_visual = OjoGeologico()

with torch.no_grad(): # (Apagamos el entrenamiento, solo queremos ver cómo funciona su ojo)
    lo_que_ve_la_ia = mi_ia_visual(tensor_sismico)

# Convertir el tensor de vuelta a formato de imagen para poder imprimirlo
imagen_procesada = lo_que_ve_la_ia.squeeze().numpy()

# 5. DIBUJAR LOS RESULTADOS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(imagen_sismica, cmap='gray')
ax1.set_title("1. Mapa Sísmico (Lo que ve el humano)")
ax1.axis('off')

# El mapa 'magma' resalta los puntos de calor
ax2.imshow(imagen_procesada, cmap='magma')
ax2.set_title("2. Mapa de Características (Lo que 've' la IA)")
ax2.axis('off')

plt.suptitle("Inteligencia Artificial Escaneando el Subsuelo", fontsize=16)
plt.show()
"""
Visión por Computadora Sísmica (PyTorch CNN).
Genera un mapa sísmico sintético con un domo de sal y aplica una capa convolucional (Conv2d)
para demostrar cómo una red neuronal actúa como un detector automático de bordes y anomalías geológicas.
"""
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

imagen_sismica = np.random.rand(100, 100) * 0.2
for x in range(100):
    y = int(50 - 20 * np.sin(x / 15.0))
    if 0 <= y < 100:
        imagen_sismica[y:y+5, x] = 1.0

tensor_sismico = torch.tensor(imagen_sismica, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

class OjoGeologico(nn.Module):
    def __init__(self):
        super().__init__()
        self.lupa = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=1)
        
    def forward(self, imagen):
        return torch.relu(self.lupa(imagen))

mi_ia_visual = OjoGeologico()
with torch.no_grad():
    lo_que_ve_la_ia = mi_ia_visual(tensor_sismico)

imagen_procesada = lo_que_ve_la_ia.squeeze().numpy()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.imshow(imagen_sismica, cmap='gray')
ax1.set_title("Mapa Sísmico Original")
ax1.axis('off')
ax2.imshow(imagen_procesada, cmap='magma')
ax2.set_title("Capa Convolucional (IA)")
ax2.axis('off')
plt.suptitle("Inteligencia Artificial Escaneando el Subsuelo", fontsize=16)
plt.show()

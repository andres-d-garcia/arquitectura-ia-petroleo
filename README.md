# 🛢️ Arquitectura de IA para Campo Petrolero Autónomo (PoC)

Este repositorio contiene una Prueba de Concepto (Proof of Concept) de una arquitectura completa de **Inteligencia Artificial y MLOps** aplicada a la industria del Oil & Gas (Petróleo y Gas). 

El proyecto simula el ciclo de vida completo de los datos: desde la generación en sensores físicos (IoT), pasando por la inferencia de Machine Learning en un servidor web, hasta la visualización en tiempo real para la toma de decisiones gerenciales.

## 🚀 Tecnologías Utilizadas
*   **Machine Learning / Deep Learning:** `Scikit-Learn`, `PyTorch`, `Statsmodels`
*   **Backend / API:** `FastAPI`, `Uvicorn`
*   **Frontend / Dashboard:** `Streamlit`
*   **Data Science:** `Pandas`, `Matplotlib`, `Numpy`

## 📁 Estructura del Proyecto

1.  **`simulador_sensores.py`**: Actúa como una bomba física. Genera datos de temperatura y vibración en tiempo real y los envía a la API mediante peticiones HTTP POST, inyectando anomalías periódicamente.
2.  **`api_pozo.py`**: Servidor FastAPI que recibe los datos IoT, ejecuta la lógica de Detección de Anomalías (Mantenimiento Predictivo) y guarda el historial en una base de datos local.
3.  **`dashboard_final.py`**: Panel de control interactivo en Streamlit que lee la base de datos en tiempo real, mostrando métricas en vivo y alertas predictivas.
4.  **`curva_declinacion.py`**: Modelo de Análisis de Curva de Declinación (DCA) que utiliza transformaciones logarítmicas y regresión para predecir la vida útil económica de un yacimiento.

## ⚙️ Cómo Ejecutar el Clúster Local
Para ver el sistema distribuido en funcionamiento, debes abrir 3 terminales separadas y ejecutar:

1.  **Terminal 1 (El Servidor):** `python api_pozo.py`
2.  **Terminal 2 (El Dashboard):** `python -m streamlit run dashboard_final.py`
3.  **Terminal 3 (Los Sensores):** `python simulador_sensores.py`

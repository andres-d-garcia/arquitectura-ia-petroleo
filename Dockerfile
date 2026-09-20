# 1. Traer un mini-sistema operativo que ya tenga Python preinstalado
FROM python:3.11-slim

# 2. Crear una carpeta dentro de la caja donde vivirá nuestro código
WORKDIR /app

# 3. Instalar las librerías necesarias dentro de la caja
# (Normalmente se usa un archivo requirements.txt, pero aquí lo hacemos directo para ilustrar)
RUN pip install fastapi uvicorn torch scikit-learn pandas

# 4. Copiar tu archivo mi_api.py desde tu Windows hacia adentro de la caja
COPY mi_api.py /app/mi_api.py

# 5. El comando automático que se ejecutará cuando Amazon presione "Play" a la caja
CMD ["uvicorn", "mi_api:app", "--host", "0.0.0.0", "--port", "8000"]
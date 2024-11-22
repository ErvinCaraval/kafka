# Usar una imagen base de Node.js
FROM node:18-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios: package.json y producer.js
COPY package.json .
COPY producer.js .  

# Instalar las dependencias de Node.js
RUN npm install

# Ejecutar el productor usando npm start, que invoca el script "start" del package.json
# y mantener el contenedor en ejecución con "tail -f /dev/null"
CMD ["sh", "-c", "npm start && tail -f /dev/null"]


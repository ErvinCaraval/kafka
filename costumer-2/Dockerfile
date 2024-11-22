# Usar una imagen base de Node.js
FROM node:18-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo package.json y costumer.js al contenedor
COPY package.json . 
COPY costumer.js . 

# Instalar las dependencias de Node.js
RUN npm install

# Ejecutar el script de inicio del package.json (npm start)
CMD ["npm", "start"]

# Bucle infinito para mantener el contenedor corriendo (opcional)
CMD ["sh", "-c", "npm start && tail -f /dev/null"]


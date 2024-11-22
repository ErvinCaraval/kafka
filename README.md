
# Proyecto Kafka con Microservicios

Este proyecto contiene múltiples microservicios y configuración para ejecutar una arquitectura basada en Kafka. 
Se proporcionan archivos para configurar contenedores Docker, implementaciones en Kubernetes y pruebas locales.

## Estructura del Proyecto

- **auth-service**: Servicio de autenticación.
  - Lenguaje: Node.js
  - Archivos importantes: `Dockerfile`, `server.js`, `package.json`

- **costumer**: Consumidor de mensajes en Python.
  - Lenguaje: Python
  - Archivos importantes: `Dockerfile`, `costumer.py`, `requirements.txt`

- **costumer-2**: Otro consumidor, esta vez en Node.js.
  - Lenguaje: Node.js
  - Archivos importantes: `Dockerfile`, `costumer.js`, `package.json`

- **producer**: Productor de mensajes en Python.
  - Lenguaje: Python
  - Archivos importantes: `Dockerfile`, `producer.py`, `requirements.txt`

- **producer-2**: Productor en Node.js.
  - Lenguaje: Node.js
  - Archivos importantes: `Dockerfile`, `producer.js`, `package.json`

- **Kubernetes**: Configuraciones de implementación para Kubernetes.
  - Archivos importantes:
    - `consumer-deployment.yml`
    - `consumer-2-deployment.yml`
    - `producer-deployment.yml`
    - `producer-2-deployment.yml`
    - `kafka-cluster.yml`

- **Otros archivos**:
  - `docker-compose.yaml`: Configuración para ejecutar los servicios localmente con Docker Compose.
  - `minikube.sh`: Script para configurar y ejecutar Minikube.
  - `create_deploy.sh`: Script para crear los despliegues en Kubernetes.
  - `build_upload.sh`: Script para crear imagenes docker y subirlas a dockerhub.

## Requisitos

1. **Docker** y **Docker Compose** instalados.
2. **Minikube** configurado para ejecutar un clúster local de Kubernetes.
3. **kubectl** para gestionar el clúster de Kubernetes.

## Ejecución Local con Docker Compose

1. Asegúrate de que Docker esté ejecutándose.
2. Ejecuta el siguiente comando para iniciar los servicios:

   ```bash
   docker-compose up
   ```

3. Los servicios estarán disponibles en los puertos configurados.

## Ejecución en Kubernetes con Minikube

1. Inicia Minikube:

   ```bash
   ./minikube.sh
   ```

2. Aplica las configuraciones de Kubernetes para crear el clúster de Kafka:

   ```bash
   ./create_deploy.sh
   ```



3. Verifica que todos los pods están en estado `Running`:

   ```bash
   kubectl get pods
   kubectl get all
   ```

## Recomendacion

Usa la configuracion del archivo de la tarea que esta en el campus virtual, y usa los comandos alojados en comandos.txt

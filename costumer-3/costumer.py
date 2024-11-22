from confluent_kafka import Consumer, KafkaException, KafkaError
import signal
import sys
import json  # Importar la librería para manejar el JSON

# Configuración del consumidor
consumer_config = {
    'bootstrap.servers': 'kafka-broker-1:9092',  # Dirección y puerto del broker Kafka
    'group.id': 'test',               # Grupo de consumidores
    'auto.offset.reset': 'earliest',        # Leer mensajes desde el inicio si no hay offset
}

# Crear una instancia del consumidor
consumer = Consumer(consumer_config)

def shutdown(signum, frame):
    """
    Cerrar el consumidor limpiamente al recibir señales de interrupción.
    """
    print("\nCerrando el consumidor...")
    consumer.close()
    sys.exit(0)

# Registrar señales para cierre limpio
signal.signal(signal.SIGINT, shutdown)  # Ctrl+C
signal.signal(signal.SIGTERM, shutdown)  # Terminación

def main():
    topic = 'univalle-ideas'  # Tema donde se escucharán los mensajes
    print(f"Consumidor iniciado. Leyendo mensajes del tema '{topic}'... Presiona Ctrl+C para salir.")

    # Suscribirse al tema
    consumer.subscribe([topic])

    try:
        while True:
            # Leer mensajes desde el tema (espera de 1 segundo)
            msg = consumer.poll(timeout=1.0)

            if msg is None:
                continue  # No hay mensajes, continuar esperando
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # Fin de la partición alcanzado
                    print(f"Fin de la partición {msg.partition()} en el tema {msg.topic()}")
                else:
                    raise KafkaException(msg.error())
            else:
                # Procesar el mensaje
                try:
                    # Convertir el mensaje en formato JSON
                    message = json.loads(msg.value().decode('utf-8'))

                    # Acceder al campo 'source' que contiene la información sobre el origen del mensaje
                    source = message.get('source', 'Costumer.py Estiven Andres Martinez Granados')
                    message_value = message.get('message', '')

                    print(f"Mensaje recibido desde {source}: {message_value}")

                except json.JSONDecodeError:
                    print("Error al decodificar el mensaje. El mensaje no es un JSON válido.")
                
    except Exception as e:
        print(f"Error al consumir mensajes: {e}")
    finally:
        print("Cerrando el consumidor...")

if __name__ == "__main__":
    main()


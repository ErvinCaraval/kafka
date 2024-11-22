from confluent_kafka import Producer
import json  # Importamos la librería para manejar el JSON

# Configuración del productor
producer_config = {
    'bootstrap.servers':'kafka-broker-1:9092',  # Dirección y puerto del broker Kafka
    'client.id': 'test',         # ID del cliente para identificarlo
}

# Crear una instancia del productor
producer = Producer(producer_config)

def delivery_report(err, msg):
    """
    Callback para reportar el estado de entrega del mensaje.
    """
    if err is not None:
        print(f"Error al enviar mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [partición {msg.partition()}]: {msg.value().decode('utf-8')}")

def main():
    topic = 'univalle-ideas'  # Tema donde se enviarán los mensajes
    print(f"Productor iniciado. Escribe mensajes para enviarlos al tema '{topic}'. Escribe 'exit' para salir.")

    try:
        while True:
            # Leer mensaje desde la consola
            message_value = input("Ingresa el mensaje: ")
            if message_value.lower() == 'exit':  # Salir si el mensaje es 'exit'
                break

            # Crear un diccionario con el mensaje y la fuente
            message = {
                'source': 'python-producer Ervin Caravali Ibarra ',  # Indicar que es de Python
                'message': message_value
            }

            # Enviar el mensaje como un JSON
            producer.produce(
                topic,
                value=json.dumps(message).encode('utf-8'),  # Convertir a JSON y codificar en bytes
                callback=delivery_report             # Asignar callback para la entrega
            )

            # Forzar la entrega de mensajes pendientes
            producer.flush()
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")
    finally:
        print("Cerrando productor...")

if __name__ == "__main__":
    main()

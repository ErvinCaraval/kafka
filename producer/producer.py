from confluent_kafka import Producer

# Configuración del productor
producer_config = {
    'bootstrap.servers': 'localhost:9092',  # Dirección y puerto del broker Kafka
    'client.id': 'python-producer',         # ID del cliente para identificarlo
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

            # Enviar mensaje
            producer.produce(
                topic,
                value=message_value.encode('utf-8'),  # Codificar el mensaje en bytes
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

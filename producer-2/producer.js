const { Kafka } = require('kafkajs');

// Configuración del productor
const kafka = new Kafka({
  clientId: 'test', // Identificador del cliente
  brokers: ['kafka-broker-1:9092'],  // Dirección y puerto del broker Kafka
});

// Crear el productor
const producer = kafka.producer();

async function runProducer() {
  await producer.connect(); // Conectar al broker

  console.log("Productor iniciado. Escribe 'exit' para salir.");

  process.stdin.on('data', async (message) => {
    const messageValue = message.toString().trim();

    if (messageValue === 'exit') {
      console.log("Cerrando productor...");
      await producer.disconnect(); // Desconectar productor
      process.exit(0);
    }

    try {
      // Crear el mensaje con los campos 'source' y 'message'
      const messageToSend = {
        source: 'nodejs-producer Ervin Caravali Ibarra', // Origen del mensaje
        message: messageValue,     // Contenido del mensaje
      };

      // Enviar el mensaje al tópico
      await producer.send({
        topic: 'univalle-ideas',
        messages: [
          { value: JSON.stringify(messageToSend) }, // Convertir el mensaje a JSON
        ],
      });
      console.log(`Mensaje enviado: ${messageValue}`);
    } catch (err) {
      console.error(`Error al enviar mensaje: ${err}`);
    }
  });
}

runProducer().catch(console.error);

const { Kafka } = require('kafkajs');

// Configuración del consumidor
const kafka = new Kafka({
  clientId: 'test', // Identificador del cliente
  brokers: ['kafka-broker-1:9092'],  // Dirección y puerto del broker Kafka
});

// Crear el consumidor
const consumer = kafka.consumer({ groupId: 'test-group' });

async function runConsumer() {
  await consumer.connect(); // Conectar al broker

  await consumer.subscribe({ topic: 'univalle-ideas', fromBeginning: true }); // Suscribirse al tema

  console.log("Consumidor iniciado. Leyendo mensajes del tema 'univalle-ideas'...");

  // Manejo de mensajes
  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      try {
        // Convertir el mensaje en formato string y luego a JSON
        const messageValue = message.value.toString();
        const parsedMessage = JSON.parse(messageValue);

        // Extraer y mostrar el campo 'source' y el contenido del mensaje
        const source = parsedMessage.source || 'Desconocido';
        const messageContent = parsedMessage.message || 'Sin contenido';

        console.log(`Mensaje recibido desde ${source} en ${topic} [partición ${partition}]: ${messageContent}`);
      } catch (error) {
        console.error('Error al procesar el mensaje:', error);
      }
    },
  });
}

runConsumer().catch(console.error);

// Manejo de cierre limpio
process.on('SIGINT', async () => {
  console.log("\nCerrando consumidor...");
  await consumer.disconnect(); // Desconectar consumidor
  process.exit(0);
});

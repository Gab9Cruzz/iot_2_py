from kafka import KafkaProducer
import json
import random
import time

# Configuración del Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'sensores'
print("✅ Productor iniciado. Enviando datos cada 5 segundos...")

# Simulación infinita de datos de sensores
while True:
    temperatura = round(random.uniform(20.0, 30.0), 2)
    humedad = round(random.uniform(40.0, 70.0), 2)
    timestamp = int(time.time())

    mensaje = {
        'sensor': 'ambiente',
        'temperatura': temperatura,
        'humedad': humedad,
        'timestamp': timestamp
    }

    producer.send(topic, mensaje)
    producer.flush()
    print("📤 Enviado a Kafka:", mensaje)
    time.sleep(5)


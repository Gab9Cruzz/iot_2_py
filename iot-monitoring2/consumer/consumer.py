from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import os

# Configuración de InfluxDB (usando variables de entorno)
INFLUX_URL = os.getenv("INFLUX_URL", "http://influxdb:8086")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN", "iot-super-secret-token-2024")
INFLUX_ORG = os.getenv("INFLUX_ORG", "IoT_Organization")
INFLUX_BUCKET = os.getenv("INFLUX_BUCKET", "sensor_data")

# Cliente de InfluxDB
client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Cliente de Kafka Consumer
consumer = KafkaConsumer(
    'sensores',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("✅ Consumidor iniciado. Escuchando datos desde Kafka...")

# Procesar cada mensaje del tópico
for mensaje in consumer:
    data = mensaje.value
    temperatura = data.get("temperatura")
    humedad = data.get("humedad")
    timestamp = data.get("timestamp")

    punto = (
        Point("ambiente")
        .tag("sensor", "ambiente")
        .field("temperatura", temperatura)
        .field("humedad", humedad)
        .time(timestamp, write_precision='s')
    )

    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=punto)
    print("💾 Guardado en InfluxDB:", data)


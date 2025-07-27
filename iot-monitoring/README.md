# Sistema de Monitoreo IoT en Tiempo Real

Sistema completo de monitoreo IoT usando Kafka, InfluxDB y Grafana.

## 🚀 Inicio Rápido

```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs en tiempo real
docker-compose logs -f

# Detener servicios
docker-compose down
```

## 🌐 Acceso a Servicios

- **Grafana**: http://localhost:3000 (admin / grafana_admin_2024)
- **InfluxDB**: http://localhost:8086 (iot_admin / iot_password_2024)
- **Kafka**: localhost:9092

## 📊 Servicios Incluidos

- **Zookeeper**: Coordinación de Kafka
- **Kafka**: Streaming de datos en tiempo real
- **InfluxDB**: Base de datos de series temporales
- **Grafana**: Visualización y dashboards
- **Productor IoT**: Simulador de sensores
- **Consumidor IoT**: Procesamiento y almacenamiento

## 🔧 Comandos Útiles

```bash
# Ver estado de servicios
docker-compose ps

# Reiniciar un servicio específico
docker-compose restart iot-producer

# Ver logs de un servicio específico
docker-compose logs -f iot-consumer

# Acceder al shell de un contenedor
docker-compose exec iot-producer bash
```

## 📈 Tipos de Sensores Simulados

- Temperatura (°C)
- Humedad (%)
- Presión atmosférica (hPa)
- Calidad del aire (PM2.5)
- Detector de movimiento
- Sensor de luminosidad (lux)

FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        g++ \
        netcat-traditional \
        curl \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN groupadd -r iotuser && \
    useradd -r -g iotuser -s /bin/bash iotuser

RUN mkdir -p /app/logs && \
    chown -R iotuser:iotuser /app

COPY --chown=iotuser:iotuser consumer.py .
COPY --chown=iotuser:iotuser health_check_consumer.py .

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV KAFKA_BOOTSTRAP_SERVERS=kafka:9092
ENV INFLUX_URL=http://influxdb:8086
ENV INFLUX_TOKEN=iot-super-secret-token-2024
ENV INFLUX_ORG=IoT_Organization
ENV INFLUX_BUCKET=sensor_data
ENV LOG_LEVEL=INFO

HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD python health_check_consumer.py || exit 1

USER iotuser
EXPOSE 8081
VOLUME ["/app/logs"]

CMD ["python", "consumer.py"]

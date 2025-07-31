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

COPY --chown=iotuser:iotuser producer.py .
COPY --chown=iotuser:iotuser health_check.py .

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV KAFKA_BOOTSTRAP_SERVERS=kafka:9092
ENV SENSOR_INTERVAL=5
ENV LOG_LEVEL=INFO

HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python health_check.py || exit 1

USER iotuser
EXPOSE 8080
VOLUME ["/app/logs"]

CMD ["python", "producer.py"]

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    curl \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /app/indexes
RUN mkdir -p /app/ai_models

# Variables de entorno
ENV HF_HOME=/app/ai_models
ENV TRANSFORMERS_CACHE=/app/ai_models
ENV SENTENCE_TRANSFORMERS_HOME=/app/ai_models

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
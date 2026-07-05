# Tourism Vector Search

Sistema de búsqueda semántica de destinos turísticos peruanos, basado en:

- **Frontend:** React (Vite)
- **Backend:** FastAPI (Python)
- **Base de datos:** MariaDB
- **Índice vectorial:** hnswlib (HNSW)
- **Embeddings:** SentenceTransformers (modelo multilingüe español/inglés)
- **Orquestación:** Docker Compose

Este documento explica cómo levantar el proyecto, descargar el modelo de IA y construir el índice vectorial.

---

## 1. Requisitos previos

- **Docker** y **Docker Compose** instalados.
- **Python 3.10+** en la máquina host (solo necesario para ejecutar algunos scripts de utilidad, opcional).
- Git (opcional, si vas a clonar el repositorio).

---

## 2. Variables de entorno

En la raíz del proyecto se usa un archivo `.env` (ya incluido o a crear) para configurar:

```env
# Ejemplo mínimo (ajustar según tu entorno)
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=tourism
MYSQL_USER=tourism
MYSQL_PASSWORD=tourism

# Parámetros de construcción del índice HNSW
HNSW_M=64
HNSW_EF_CONSTRUCTION=200
HNSW_MMAX0=40

# Ruta del índice dentro del contenedor backend
VECTOR_INDEX_PATH=/app/indexes/destinos.index
```

Asegúrate de que el `.env` exista antes de levantar los contenedores.

---

## 3. Levantar la base de datos y el backend con Docker

Desde la raíz del proyecto:

```bash
docker compose up -d
```

Esto levanta:

- `backend`: FastAPI + scripts + modelo/índice.
- `db`: MariaDB (con `init.sql` y `seed.sql`).
- `phpmyadmin`: interfaz web para la base de datos (opcional).
- `n8n`: servicio de automatización (opcional).

Para ver el estado de los contenedores:

```bash
docker compose ps
```

Para ver logs del backend:

```bash
docker compose logs -f backend
```

---

## 4. Descargar el modelo de embeddings (offline)

El backend usa un modelo de SentenceTransformers que se guarda en `backend/ai_models` (montado en `/app/ai_models` dentro del contenedor).

Hay dos formas de descargar el modelo:

### 4.1. Desde el contenedor backend (recomendado)

Ejecuta:

```bash
docker compose exec backend python scripts/download_model.py
```

Esto descargará el modelo al directorio `/app/ai_models` dentro del contenedor, que está mapeado a `backend/ai_models` en tu máquina.

### 4.2. Desde la máquina host (si lo prefieres)

También puedes ejecutar el script directamente (requiere Python y dependencias instaladas en tu host):

```bash
cd backend
python scripts/download_model.py
cd ..
```

---

## 5. Construir el índice vectorial HNSW

Una vez que:

- La base de datos está levantada y poblada (lo hace Docker con `init.sql` + `seed.sql`).
- El modelo de embeddings ya fue descargado.

Entonces puedes construir el índice vectorial:

### 5.1. Construir el índice desde el contenedor backend

Desde la raíz del proyecto:

```bash
# Opcional: borrar índice anterior
docker compose exec backend rm -f /app/indexes/destinos.index

# Construir índice
docker compose exec backend python scripts/build_index.py
```

Este comando:

1. Lee todos los atractivos desde MariaDB.
2. Genera un embedding por destino usando SentenceTransformers.
3. Construye el índice HNSW con los parámetros `HNSW_M`, `HNSW_EF_CONSTRUCTION` y `HNSW_MMAX0`.
4. Guarda el índice en la ruta configurada (por defecto `/app/indexes/destinos.index`).

Si quieres medir el tiempo de construcción:

```bash
time docker compose exec backend python scripts/build_index.py
```

---

## 6. Probar el endpoint de búsqueda

Con los contenedores en marcha, el backend suele estar expuesto en:

- `http://localhost:8000` (ajustar si cambiaste puertos en `docker-compose.yml`).

### 6.1. Probar salud

```bash
curl http://localhost:8000/health
```

Deberías recibir una respuesta simple indicando que el servicio está OK.

### 6.2. Probar búsqueda semántica

Ejemplos de consultas:

```bash
curl "http://localhost:8000/search?q=hombres%20tejedores"
curl "http://localhost:8000/search?q=ciudadela%20incaica"
curl "http://localhost:8000/search?q=ba%C3%B1os%20termales"
```

La respuesta será un JSON con una lista de destinos ordenados por relevancia.

---

## 7. Levantar el frontend

Si el frontend está configurado para hablar con `http://localhost:8000`:

```bash
cd frontend
npm install
npm run dev
```

Por defecto, Vite levanta el frontend en `http://localhost:5173` (o el puerto configurado).

Desde el navegador:

1. Abre `http://localhost:5173`.
2. Escribe una consulta en el buscador (por ejemplo: “hombres tejedores”, “lago andino”).
3. Deberías ver la lista de destinos relevantes.

---

## 8. Script de evaluación (opcional)

Hay un script de evaluación para medir Recall@5 y tiempo medio por consulta:

```bash
python backend/tests/eval_hnsw_recall.py
```

Este script:

- Envía un conjunto fijo de queries al endpoint `/search`.
- Calcula el Recall@5 por consulta y el promedio.
- Calcula el tiempo medio de respuesta.

Es útil para comparar configuraciones del índice (M, efConstruction, etc.).

---

## 9. Comandos rápidos de referencia

- **Levantar todo:**

  ```bash
  docker compose up -d
  ```

- **Detener todo:**

  ```bash
  docker compose down
  ```

- **Ver logs del backend:**

  ```bash
  docker compose logs -f backend
  ```

- **Descargar modelo (en backend):**

  ```bash
  docker compose exec backend python scripts/download_model.py
  ```

- **Construir índice (en backend):**

  ```bash
  docker compose exec backend python scripts/build_index.py
  ```

- **Ejecutar evaluación de recall (desde host):**

  ```bash
  python backend/tests/eval_hnsw_recall.py
  ```

Con estos pasos deberías poder levantar el proyecto completo, descargar el modelo de IA y construir el índice vectorial HNSW desde cero.

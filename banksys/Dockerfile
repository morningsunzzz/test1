FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .

RUN pip install --no-cache-dir ".[dev]"

COPY src/ ./src/
COPY tests/ ./tests/

EXPOSE 8502

CMD ["streamlit", "run", "src/backend/app.py", "--server.port=8502", "--server.address=0.0.0.0"]

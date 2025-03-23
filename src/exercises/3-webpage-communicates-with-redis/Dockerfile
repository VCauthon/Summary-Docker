FROM python:3.11-slim


WORKDIR /app

ENV REDIS_HOST=redis-db

COPY src/ src/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "-m", "flask", "--app=src", "run", "--host=0.0.0.0", "--port=5000"]

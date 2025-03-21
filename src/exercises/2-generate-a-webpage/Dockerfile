FROM python:3.11-slim


COPY src/ app/src/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


WORKDIR /app


CMD ["gunicorn", "-w", "2", "-b" "0.0.0.0:5000", "src:create_app", "--reload"]

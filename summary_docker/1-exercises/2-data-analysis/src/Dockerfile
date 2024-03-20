FROM python:3.12.1-alpine
EXPOSE 5000

COPY app.py /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN mkdir /app/files_input /app/files_output
CMD ["python", "app.py"]

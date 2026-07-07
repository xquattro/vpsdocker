FROM python:3.11-slim
# Sağlık kontrolü için curl kurulumu eklendi
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN pip install flask
COPY app.py .
CMD ["python", "app.py"]

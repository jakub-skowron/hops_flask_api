FROM python:3.10.6

WORKDIR /app

COPY . /app

EXPOSE 5000

RUN pip install -r requirements.txt



CMD ["python3", "app.py"]

FROM python:3.10.6

WORKDIR /app

COPY . /app

EXPOSE 5000

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5000 -w 3 app:app

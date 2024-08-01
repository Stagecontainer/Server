# Dockerfile
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=config.settings

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]

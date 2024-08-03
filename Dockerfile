FROM python:3.10-slim

WORKDIR /app

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    wget

# wait-for-it.sh 다운로드 및 실행 권한 설정
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x wait-for-it.sh

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY . /app

ENV DJANGO_SETTINGS_MODULE=config.settings

# wait-for-it.sh를 사용하여 Redis가 준비될 때까지 기다림
CMD ["bash", "-c", "/app/wait-for-it.sh redis:6379 -- daphne -b 0.0.0.0 -p 8000 config.asgi:application"]

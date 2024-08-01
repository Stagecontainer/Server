# Python 3.10 사용
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 업데이트 및 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 의존성 설치
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# 애플리케이션 소스 코드 복사
COPY . /app

# 환경 변수 설정
ENV DJANGO_SETTINGS_MODULE=config.settings

# 명령어
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "config.asgi:application"]

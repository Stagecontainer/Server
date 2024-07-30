# Dockerfile

# 베이스 이미지
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . /app/

# 정적 파일 모으기
RUN python manage.py collectstatic --noinput

# 포트 노출
EXPOSE 8000

# 기본 실행 명령
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

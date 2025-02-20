# 1. 베이스 이미지 설정
FROM python:3.8-slim

# 2. 필수 패키지 설치 (pillow 설치에 필요한 라이브러리 포함)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    python3-dev \
    python3-venv \
    python3-pip \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. 컨테이너 내부 작업 디렉토리 설정
WORKDIR /back_to_the_zero

# 4. pip 최신화
RUN pip install --upgrade pip setuptools

# 5. 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. 애플리케이션 코드 복사
COPY . .

# 7. 포트 노출
EXPOSE 8000

# 8. 애플리케이션 실행 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
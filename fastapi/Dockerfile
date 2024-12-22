FROM python:3.10

# 한국어 로케일을 설정하기 위해 필요한 패키지 설치
RUN apt-get update && apt-get install -y locales && \
    locale-gen ko_KR.UTF-8 && \
    apt-get install -y fonts-nanum

# 로케일 설정
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8

WORKDIR /app
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# requirements.txt 파일로 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

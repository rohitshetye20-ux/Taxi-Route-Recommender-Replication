FROM python:3.10-slim

LABEL maintainer="Rohit Shetye"
LABEL project="Taxi Route Recommender"
LABEL version="1.0.0"
LABEL license="MIT"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    graphviz \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p output logs models figures

EXPOSE 8888

CMD ["python", "scripts/run_pipeline.py"]

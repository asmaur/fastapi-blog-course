FROM python:3.11-alpine

RUN mkdir blog.db

WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apk update
RUN apk add --no-cache --virtual build-deps gcc musl-dev pkgconf mariadb-dev && \
    apk add --no-cache mariadb-connector-c-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-deps

COPY ./blog .
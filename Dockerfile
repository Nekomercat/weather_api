# Base image
FROM python:3.9

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY ./app /app

ADD schema.sql /var/lib/postgresql/data/new/

#COPY schema.sql /var/lib/postgresql/data/schema.sql

RUN chmod a+r /var/lib/postgresql/data/new/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copiar el archivo CSV al contenedor
COPY challenge_dataset.csv .

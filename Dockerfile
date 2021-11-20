# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN python3 -m pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

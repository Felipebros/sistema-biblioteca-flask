# syntax=docker/dockerfile:1
FROM python:3.8

ARG APP_ENV

ENV APP_ENV=${APP_ENV} \
    PYTHONUNBUFFERED=1
WORKDIR /code

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install pipenv

COPY . /code/
RUN pipenv install $(test "$APP_ENV" = PRD || echo "--dev") --deploy --system --ignore-pipfile

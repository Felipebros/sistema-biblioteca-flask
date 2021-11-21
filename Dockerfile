# syntax=docker/dockerfile:1
FROM python:3.8

ARG APP_ENV APP_DEBUG

ENV APP_ENV=${APP_ENV} \
    PYTHONUNBUFFERED=1 \
    FLASK_APP="src/app" \
    FLASK_ENV=${APP_ENV} \
    FLASK_DEBUG=${APP_DEBUG}
WORKDIR /code

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install pipenv

COPY . /code/
RUN pipenv install $(test "$APP_ENV" = production || echo "--dev") --deploy --system --ignore-pipfile

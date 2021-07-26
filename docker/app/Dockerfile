FROM python:3.8.3-slim-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./docker/app/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

COPY . /app/
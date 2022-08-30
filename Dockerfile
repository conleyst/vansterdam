FROM python:3.10.6-slim-buster AS base

LABEL maintainer="Sean Conley <conleyst@gmail.com>"

ENV FLASK_DEBUG=1
ENV FLASK_APP=application
ENV FLASK_RUN_HOST=0.0.0.0

RUN apt-get update && apt-get install -y

WORKDIR /vansterdam
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run"]

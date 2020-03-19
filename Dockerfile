FROM python:3.8-alpine
MAINTAINER Ahmed Emad.
ENV PYTHONUNBUFFERED 1
RUN mkdir /covid19
WORKDIR /covid19
COPY . /covid19
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN apk add --update --no-cache postgresql-client postgresql
RUN pip3 install -r /covid19/requirements.txt
RUN apk del .tmp-build-deps
RUN adduser -D covid19
USER covid19
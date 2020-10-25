FROM python:3-alpine

MAINTAINER Omri Grazutis

COPY . /apps/

WORKDIR /apps

ENV FLASK_APP=myapp.py

EXPOSE 7800

RUN pip install flask

CMD ["flask", "run", "--host=0.0.0.0"]

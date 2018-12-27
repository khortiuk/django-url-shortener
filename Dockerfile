FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_url_shortener

WORKDIR /django_url_shortener

ADD . /django_url_shortener

RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate


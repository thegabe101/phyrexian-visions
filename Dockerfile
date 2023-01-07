# FROM python:3.8-buster

FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive

# build-essential
RUN apt-get -qq -y update \
    && apt-get -qq -y install  \
    python3-pip python3-icu python3-psycopg2 \


# Install Python dependencies
RUN pip3 install --no-cache-dir -q -U pip setuptools six

# Install bard
COPY . /bard
WORKDIR /bard
ENV PYTHONPATH /bard
# RUN pip install -q -e /bard


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . .
RUN pip install .
#CMD flask run -h 0.0.0.0 -p 8080
# CMD gunicorn --workers 2 --timeout 90 --bind 0.0.0:5000 --access-logfile - wsgi:application



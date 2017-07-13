FROM ubuntu:latest
MAINTAINER Wellington Castro "wcesarc@gmail.com"

RUN apt-get update
RUN apt-get install -y python-pip
RUN apt-get install -y libmysqlclient-dev


RUN mkdir -p /opt/deploy/ads
RUN mkdir -p /var/log/ads/webserver/
RUN mkdir -p /var/log/ads/application/

COPY . /opt/deploy/ads
RUN pip install -r /opt/deploy/ads/requirements.txt

WORKDIR /opt/deploy/ads

EXPOSE 8000

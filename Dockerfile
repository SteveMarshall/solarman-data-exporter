FROM python:3-alpine

EXPOSE 18000

LABEL MAINTAINER="Steve Marshall"
LABEL NAME=solarman-data-exporter

COPY . /solarman-data-exporter

WORKDIR /solarman-data-exporter

RUN pip install --upgrade pip \
  && pip3 install -r requirements.txt

CMD [ "python", "./main.py" ]

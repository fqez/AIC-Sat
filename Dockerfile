FROM ubuntu:bionic

MAINTAINER Fraitor

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt install -y git nano wget
RUN apt install -y python3 python3-pip python3-dev python3-venv python3-tk
RUN apt install -y libsm6

RUN useradd -ms /bin/bash aiva
RUN usermod -a -G aiva aiva
WORKDIR /home/aiva
USER aiva

RUN git clone https://github.com/fqez/AIVA-segmentacion-satelite AIVA
RUN sed -i 's/127.0.0.1/0.0.0.0/g' AIVA/server.py

RUN python3 -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r AIVA/requirements.txt

#COPY aerial_model.h5 AIVA/model/aerial_model.h5
RUN wget -O AIVA/model/aerial_model.h5 https://jderobot.org/store/fperez/uploads/aerial_model.h5
COPY boot.sh ./

USER root
RUN chmod +x /home/aiva/boot.sh
RUN chown aiva:aiva AIVA/model/aerial_model.h5
USER aiva

ENTRYPOINT ["/bin/bash", "boot.sh"]

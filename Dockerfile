FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app .

ENTRYPOINT ["sh","runner.sh"]

VOLUME /python-docker/config

EXPOSE 9000
EXPOSE 8080
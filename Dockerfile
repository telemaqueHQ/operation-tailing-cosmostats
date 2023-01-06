FROM python:3.8-buster

# System deps:
ENV TZ Europe/Paris

RUN apt-get update && apt-get install -y --no-install-recommends autossh \
                telnet \
                net-tools \
                cron \
                rsyslog \
                vim \
                man \
            && apt-get autoremove -y

COPY ./crons/* /etc/cron.d/cronpy

# Copy only requirements to cache them in docker layer
WORKDIR /code
ADD ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt
ADD . /code

RUN chmod 777 ./start.sh

CMD ./start.sh
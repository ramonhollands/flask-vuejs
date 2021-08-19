FROM python:3.8-slim-buster

# Install python requirements
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN a=a pip install -r requirements.txt

# Install node/npm
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_11.x
RUN apt-get install -y nodejs
RUN apt-get install -y npm

ADD app app
WORKDIR /app

EXPOSE 8008

CMD sh start_app.sh

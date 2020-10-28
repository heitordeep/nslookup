FROM python:3.7.3-slim
RUN apt-get update -y && apt-get install python-pip -y
RUN apt-get install dnsutils -y
COPY . /app
WORKDIR /app
RUN make requirements
CMD gunicorn wsgi:application_whois --bind 0.0.0.0:$PORT --preload

FROM debian:8.2
MAINTAINER Venkata Gummadi
RUN apt-get update && apt-get install -y \
  python \
  python-dev \
  python-distribute \
  python-pip
WORKDIR /app/
ADD . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python server.py

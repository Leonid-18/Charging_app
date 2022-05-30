FROM python:3.9.5
EXPOSE 8000

WORKDIR /opt/shell-charge/api/
ADD . /opt/shell-charge/api/
RUN apt-get update && apt-get install -y wget \
  && mkdir -p /opt/shell-charge/logs \
  && pip install -U\
  --no-cache-dir \
  --trusted-host pypi.python.org \
  -r requirements.txt

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["./bin/start.sh"]
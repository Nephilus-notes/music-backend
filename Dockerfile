FROM python:3.16.0

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt; \
    sudo apt-get update; \
    sudo apt-get install nginx;

COPY ./musicbackend /musicbackend

WORKDIR /musicbackend

COPY ./entrypoint.sh .
ENTRYPOINT [ "sh", "." ]
FROM python:3.12.1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt; \
    apt-get update; \
    apt-get install nginx;

COPY ./musicbackend /musicbackend

WORKDIR /musicbackend

COPY ./entrypoint.sh .
ENTRYPOINT [ "sh", "." ]
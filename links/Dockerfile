FROM python:3.11

WORKDIR /home

COPY rq.txt .

RUN pip install --upgrade pip

RUN pip install -r rq.txt

COPY . /home
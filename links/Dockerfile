FROM python:3.12


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

WORKDIR /home

RUN mkdir /home/static

COPY --chown=root:root . .

RUN pip install -r rq.txt

CMD ["gunicorn", "-b", "0.0.0:8001", "links.wsgi:application"]



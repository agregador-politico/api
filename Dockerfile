FROM python:3.7.9-slim

WORKDIR /app

ARG APP_DIR=./app

RUN useradd -m app

USER app

ENV PATH="/home/app/.local/bin:${PATH}"

COPY ./requirements.txt /tmp

COPY ./app /app

RUN pip install --upgrade pip                                                  && \
    pip install -r /tmp/requirements.txt                                       && \
    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

CMD python server.py

FROM python:3.6-slim-buster

ARG image_name
ARG image_version
LABEL name="${image_name}" release="${image_version}"

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PYTHONFAULTHANDLER 1

ENV NUM_WORKERS 2
ENV THREADS_PER_WORKER 2
ENV WORKER_TIMEOUT_SEC 30
ENV LOG_LEVEL INFO

RUN useradd --create-home dev
WORKDIR  /home/dev/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-deps wheels/*.whl

RUN pip3 list

RUN chmod +x start_server.sh
ENTRYPOINT ./start_server.sh workers=${NUM_WORKERS} threads=${THREADS_PER_WORKER} timeout=${WORKER_TIMEOUT_SEC} log-level=${LOG_LEVEL}

USER dev
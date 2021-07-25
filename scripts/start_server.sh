#!/bin/bash
set -euo pipefail

for ARGUMENT in "$@"; do
  KEY=$(echo $ARGUMENT | cut -f1 -d=)
  VALUE=$(echo $ARGUMENT | cut -f2 -d=)
  case "$KEY" in
    workers)     NUM_WORKERS=${VALUE} ;;
    threads)     THREADS_PER_WORKER=${VALUE} ;;
    timeout)     WORKER_TIMEOUT_SEC=${VALUE} ;;
    log-level)   LOG_LEVEL=${VALUE} ;;
    *)
  esac
done

gunicorn --bind 0.0.0.0:8000 \
  --workers "${NUM_WORKERS:-2}" \
  --threads "${THREADS_PER_WORKER:-2}" \
  --timeout "${WORKER_TIMEOUT_SEC:-30}" \
  --log-level "${LOG_LEVEL:-INFO}" \
  --preload \
  app.service.server:app

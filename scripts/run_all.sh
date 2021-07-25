#!/bin/bash
set -eo pipefail

if [ -z "${DATA_DIR}" ]; then
  echo "\$DATA_DIR is NOT set"
  exit 1
fi

FORCE_RECREATE=${1:-"true"}

if [ "${FORCE_RECREATE}" == "true" ] || [ "${FORCE_RECREATE}" == "True" ]; then
  echo "Building new image..."
  sh scripts/build_docker_image.sh
fi

VERSION=$(cat VERSION)
export VERSION

mkdir -p "${DATA_DIR}/pgdata"
docker-compose up -d
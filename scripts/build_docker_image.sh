#!/bin/bash
set -euo pipefail

NAME="backend-api"
VERSION=$(cat VERSION)
IMAGE_TAG="${NAME}:${VERSION}"
BACKEND_API_WHEEL="dist/backend_api-${VERSION}-py36-none-any.whl"

DOCKERFILE="app/docker/Dockerfile"
WORKING_DIR="./working-dir"

python3 setup.py test

echo "Preparing files..."

python3 setup.py bdist_wheel --python-tag py36

rm -rf ${WORKING_DIR}
mkdir -p "${WORKING_DIR}/wheels/"

cp "${BACKEND_API_WHEEL}" "${WORKING_DIR}/wheels/"
cp "scripts/start_server.sh" "${WORKING_DIR}/"
cp "requirements.txt" "${WORKING_DIR}/"

echo "Building Docker image..."

docker build -t "${IMAGE_TAG}" --build-arg image_name="${NAME}" --build-arg image_version="${VERSION}" -f "${DOCKERFILE}" "${WORKING_DIR}"

rm -rf ${WORKING_DIR}

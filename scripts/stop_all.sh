#!/bin/bash
set -euo pipefail

VERSION=$(cat VERSION)
export VERSION

docker-compose down -v --remove-orphans
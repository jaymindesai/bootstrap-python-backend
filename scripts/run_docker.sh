#!/bin/bash

docker run -p 8000:8000 --name backend-api backend-api:$(cat VERSION)
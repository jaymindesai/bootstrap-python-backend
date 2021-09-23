# Bootstrap Python Backend

A template repository for backend Python REST API server with a database

Stack: Flask Server, Gunicorn WSGI, Postgres DB, Docker, Shell

## Prerequisites

- Python 3.6
- [Docker](https://docs.docker.com/get-docker/)

## Setup

[Setup and activate a virtual environment](https://docs.python.org/3/tutorial/venv.html) (optional but recommended)

```shell script
pip install -r requirements.txt
```

## Testing

```shell script
# Run unit tests with PyTest
python setup.py test
```

## Running

### Running Flask Server Locally
```shell script
# Install application
python setup.py install

# Start server locally
sh scripts/start_server.sh
```

To start server locally with custom settings:
  - Number of workers
  - Threads per worker
  - Worker timeout
  - Gunicorn log level

```shell script
sh scripts/start_server.sh workers=3 threads=2 timeout=30 log-level=DEBUG
```

### Running Flask Server inside Docker
```shell script
# Build docker image
python setup.py build_docker

# Start server
sh scripts/run_docker.sh
```

For custom settings, update [Dockerfile](app/docker/Dockerfile) before building image

### Running Flask Server with Postgres DB

Runs the entire setup using `docker-compose`:
  - Flask API server
  - Postgres database
  - Postgres admin

Make sure you have `DATA_DIR` environment variable set. This directory will be used as persistent volume mount 
for Postgres database.

```shell script
# Start all services (will always create new backend-api image)
sh scripts/run_all.sh

# Use existing backend-api image as per the VERSION file
sh scripts/run_all.sh false

# Stop all services
sh scripts/stop_all.sh
```

This will start three containers on the same virtual network. Database will run on port`5432`, admin 
console will be available on `http://localhost:5433` and API server will be available on `http://localhost:8000`

### Endpoints

```shell script
# Health check
curl localhost:8000/health

# Sample POST endpoint
curl -X POST http://localhost:8000/postendpoint -H 'Content-Type: application/json' -d '{"param": "value"}'
```

### Kubernetes

To run the app on a Kubernetes cluster:
- Install kubernetes-cli (`kubectl`)
- Build and push the docker image to a registry accessible on the cluster
- Replace the placeholders in the deployment files under [kubernetes](./kubernetes) directory and run the following commands
```shell
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

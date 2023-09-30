# URL Shortener Project

A professional URL Shortener project using Docker, FastAPI, Celery, Redis, PostgreSQL, Grafana, Prometheus, Nginx, and more.


## Table of Contents
1. [Project Structure](#project-structure)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Installation](#installation)
5. [Endpoints](#endpoints)
6. [Contributing](#contributing)
7. [License](#license)

## Project Structure

The project is a backend component. The `docker-compose.yml` file orchestrates the deployment.

## Features

- **Dockerized:** Utilizes Docker and Docker Compose for easy deployment and containerization of the project.
- **FastAPI:** Uses FastAPI as the web framework to build efficient and fast API endpoints.
- **Celery and Redis:** Implements background task processing using Celery and Redis for scalability.
- **PostgreSQL:** Utilizes PostgreSQL as the database for storing URL information.
- **Grafana and Prometheus:** Provides monitoring and visualization of metrics through Grafana and Prometheus.
- **Nginx:** Serves as the web server, handling direct access to API documentation.
- **Pytest:** Includes pytest for automated testing of API routes.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- A modern web browser for accessing Grafana, Prometheus, and other components.

## Installation

- Clone this repository
- Configure environment variables using the provided `env-example.txt` file and create your own `.env`

## Endpoints

### Accessing Components

- React App: http://127.0.0.1
- API Documentation: http://127.0.0.1/api/v1/docs
- Grafana: http://127.0.0.1:3000
- Prometheus: http://127.0.0.1:9090
- PostgreSQL Admin: http://127.0.0.1:5050


### Testing
- Pytest framework implemented for rigorous testing.
- When container is running run the following [export TESTING=1]
- Then run test [pystest ./app/tests/test_url.py -v]
- When you are done run [unset TESTING]


## Contributing

Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE)


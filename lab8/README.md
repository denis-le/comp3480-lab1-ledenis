# Lab 8

## Objective
The objective of this project is to use Docker Compose to implement three cloud services:
- **MinIO** for shared file system
- **Postfix** for an email server
- **Redis** for shared memory

Additionally, the Python command line driver must be updated to support the services mentioned.

## Description of the Project
The project sets up a local cloud environment using Docker Compose to run the services:
- **MinIO**: Provides an object storage service for file sharing
- **Postfix**: Acts as an email relay to simulate an email service
- **Redis**: Provides shared memory with key-value stores.

The Python driver interacts with the services programmatically:
- Uploading and listing files on MinIO
- Sending a test email through Postfix and `smtplib`
- Storing and retrieving data in Redis

## Design of the Project
Each service is run in its own Docker container:
- **MinIO**: Runs the MinIO server and exposes ports 9000 (API) and 9001 (Console)
- **Postfix**: Runs a Postfix SMTP server on port 1587 (mapped from 587)
- **Redis**: Runs Redis on port 6379

The Docker containers are also implemented with volumes for persistence.

## How to Run the Project
### Prerequisites
1. Ensure Docker is installed
2. Build the docker container for the FastAPI service by running this command from the project directory:
```bash
docker build -t lab8fastapi .
```

### Containers
To start the containers to ensure functionality, run this command from the project directory:

```bash
docker-compose up
```

This will start:
- The FastAPI service on port 8080
- The MySQL service on port 3306

Access the services:
- MinIO console: http://localhost:9001
    - Credentials:
        - Username: lab8user
        - Password: lab8password
- Redis: Available at localhost:6379.
- Postfix: SMTP available at localhost:1587.

#### Command Line Driver

To run the Python Command Line Driver, run this command from the project directory:
```bash
python driver.py
```
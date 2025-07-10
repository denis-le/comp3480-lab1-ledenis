# Lab 7

## Objective
The objective of this lab is to implement the queries done in Lab 5 and 6 in Python. The queries would then be added to the existing command line driver previously implemented for FastAPI, and unit tests would be augmented to cover the queries.

## Description of the Project
This project extends the functionality of the Lab 6 application by integrating SQL queries directly into the Python command line driver. The driver allows users to interact with the FastAPI endpoints as well as execute various MySQL queries on the `my_guitar_shop` database. This provides a unified interface for testing both API routes and database queries.

## Design of the Project
The command line driver and the queries are implemented in `driver.py`. The existing FastAPI service is stored in `main.py`, so no changes are made with it. Meanwhile, `DockerCompose.yaml` covers the containerization of both the FastAPI service and the MySQL database.

## How to Run the Project

### Prerequisites
1. Ensure Docker is installed
2. Build the docker container for the FastAPI service by running this command from the project directory:
```bash
docker build -t lab7fastapi .
```

### Running the Project

#### Containers
To start the containers to ensure functionality, run this command from the project directory:

```bash
docker compose -f DockerCompose.yaml up
```

This will start:
* The FastAPI service on port 8080
* The MySQL service on port 3306

#### Command Line Driver

To run the Python Command Line Driver, run this command from the project directory:
```bash
python driver.py
```

This will display a menu to either select the FastAPI service or MySQL service.

#### Unit Tests
To run the unit tests, use the built-in run button in PyCharm (or preferred code editor)
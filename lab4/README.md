# Lab 3

## Objective

The objective of this lab is to containerize a FastAPI application using Docker.

## Description of the Project

The project uses a `Dockerfile` to containerize the FastAPI service previously implemented in another lab. It is
configured to expose the application on port `8080` and run using Uvicorn.

## Design of the Project

The FastAPI service is stored in `main.py`, and `Dockerfile` is used to containerize it. The dependencies needed to run
the application are specified in requirements.txt, and `Dockerfile` uses that file to install any required dependencies.

`Dockerfile` follows these steps:
1. Uses official Python image as its parent image
2. Sets the working app directory in the container
3. Copies the current directory contents into the container at app
4. Installs any dependencies specified in `requirements.txt`
5. Exposes port 8080 to allow access to the service
6. Runs the application using Uvicorn

## How to Run the Project

### Prerequisites
* Have Docker installed
* Python (3.9+)

To build the container, run this command from the project's directory:
```bash
docker build -t lab4 .
```

Afterward, run the docker container using this command in a new terminal window:
```bash
docker run -p 8080:8080 lab4
```

This will start the service on http://localhost:8080/



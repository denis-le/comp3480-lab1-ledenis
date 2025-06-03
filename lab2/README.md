# Lab 2

## Introduction
The objective of this lab is to expand on Lab 1, which covered creating a FastAPI service.
This lab expands by having:
* A command line driver program which accesses all the routes
* An additional route that contains header parameters
* An additional route that contains cookie parameters
* Unit tests for all routes

## Description
The service contains several endpoints when opening the FastAPI service using Uvicorn.
Adding on to the previous lab, this service contains:
* Unit tests that prints response of the route
* A header route that takes in an email, role (admin, guest, etc.), and the device
type (desktop, phone, tablet)
* A cookie route that will store the theme (light, dark) for future reference to visuals

## Design
The routes are organized in `main.py`, while tests are written in a different file, `tests.py`.
The driver used to run the routes are stored in another file `driver.py`.

Uvicorn is used to start the FastAPI service, while the tests and drivers can be run using the built in code runner.

## How to run the Project
### Prerequisites
* Python (requests)
* FastAPI
* Uvicorn

To install the packages using pip, run these commands:
```
pip install fastapi
pip install uvicorn
pip install requests
```

### Running the Project
#### Service
To start the service, run this command from the project's directory:
```
uvicorn main:app --port 8080 --reload
```

This will start the service on http://localhost:8080/

#### Unit Tests
To run the unit tests, use the built-in run button in PyCharm (or preferred code editor)

#### Command Line Driver
To run the command line driver, use the built-in run button or run this command from the project's directory:
```
python driver.py
```


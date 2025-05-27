# Lab 1

## Objective
The objective of this lab is to create a FastAPI Service with the following features:
* Minimum of 10 routes total
* At least one simple route
* At least one query string route
* At least one path route
* The routes should return information related to the route description

## Description of the Project
The service provides several endpoints when opening the FastAPI service using Uvicorn
* Static routes such as `/` and `/about`
* Query routes and path routes for calculating age given the year born and current year
* A post route to take user data and get the age
* Routes to get the current year, time, and day using `datetime`
* Query routes and path routes to greet users by name

## Design of the Project
The lab is done using FastAPI and is organized in a single file (`main.py`). The endpoints are designed to be simple 
while fulfilling the requirements of the lab. The service also uses Python's `datetime` to get the current date and time
for display purposes.

Finally, the lab is run using Uvicorn to get a visual display that the endpoints are working as intended.

## How to run the Project
### Prerequisites
* Python
* FastAPI
* Uvicorn

To install the packages using pip, run these commands:
```
pip install fastapi
pip install uvicorn
```

### Running the Service
To start the service, run this command from the project's directory:
```
uvicorn main:app --port 8080 --reload
```

This will start the service, which can then be accessed on [http://localhost:8080/](http://localhost:8080/)

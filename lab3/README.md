# Lab 3

## Objective
The objective of this lab is to create a Node.js service using Express with the following features:
* 12 Routes
    * 5 routes should return HTML content
    * 5 routes should have query parameters
    * 1 route should have header parameters
    * 1 route should have body inputs

## Description of the Project
The project implements the following endpoints:
* `/`: Returns a basic "Hello World" Message
* `/about`: Describes the app
* `/year`: Returns current year
* `/time`: Returns current time
* `/day`: Returns the day of the week
* `/greet`: Returns a greeting based on a query parameter name
* `/age`: Returns age given a query parameter birth year
* `/add`: Calculates and returns sum of two numbers passed by query parameters `x` and `y`
* `/multiply`: Calculates and returns product of two numbers passed by query parameters `x` and `y`
* `/convert`: Converts inches to centimeters given query parameter `inch`
* `/headers`: Returns user info sent via headers
* `/person`: Accepts a POST request with a JSON body and responds with a message using the body input


## Design of the Project
The lab is done using Express and is organized in a single file (`app.js`). The endpoints are designed to be simple 
while fulfilling the requirements of the lab. The service also uses JavaScript's `Date` object to get the current date and time.

## How to run the Project

### Prerequisites
* Node.js
* npm (comes with Node.js)
* Express (used for routing)

### Initialize npm
```bash
cd lab3/
npm init -y
```

#### Install Dependencies
```bash
npm install express
```

### Running the Service
To start the service, run this command from the project's directory:

```bash
node app.js
```

This will start the service, which can then be accessed on [http://localhost:8080/](http://localhost:8080/)

The routes can then be accessed and tested on an API testing app such as Postman
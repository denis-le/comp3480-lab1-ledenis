# Lab 6

## Objective
The objective of this lab is to containerize an implementaion of MySQL, and repeat lab 5 using it. 

## Description of the Project
The database models a fictional guitar shop business, and includes tables for:
* products - Items available for sale
* categories - Product categories
* customers - customer details
* addresses - billing and shipping information
* orders - customer orders
* order_items - items within each order
* administrators - login information for the admin accounts

The queries include:
1. Showing all product information
2. Showing product name and category
3. Showing customer name and shipping address
4. Showing customer name and billing address
5. Showing customer name and product ordered
6. Showing product name and discount if over 30%
7. Showing number of products in each category
8. Showing how many products have discount and how much of a discount
9. Showing number of customers per state
10. Showing average price per category
11. Showing number of orders from each customer

## Design of the Project
The MySQL database is containerized using Docker Compose. It features volume for persistency, and is exposed to the default port for MySQL (3306).

## How to Run the Project

### Start the Container
To start the container, run this command from the project directory:

```bash
docker compose -f DockerCompose.yaml up
```

### Connect to MySQL
To connect to MySQL through DBeaver, create a connection:
* Host: localhost
* Port: 3306
* Username: root
* Password: lab6password

### Running the Project
1. Run `createguitar.sql` to create the `my_guitar_shop` database
2. Open `Queries.sql` and connect to the `my_guitar_shop` database
3. Run queries individually or run script to run all queries at once

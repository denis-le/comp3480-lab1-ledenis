# Lab 5

## Objective
The objective of this lab is to develop at least 10 queries using the included Guitar Database `.sql` file. The queries include simple table queries, inner join queries, and group by queries.

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
The database is generated from the provided script and called `my_guitar_shop`. The queries are then stored in `Queries.sql`

## How to Run the Project

1. Install DBeaver and MySQL if not already installed
2. Start MySQL server and connect to DBeaver
3. Run `createguitar.sql` to create the `my_guitar_shop` database
4. Open `Queries.sql` and connect to the `my_guitar_shop` database
5. Run queries individually or run script to run all queries at once

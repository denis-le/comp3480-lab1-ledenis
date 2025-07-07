import mysql.connector
import requests
from datetime import datetime

def print_routes():
    print("\nRoutes")
    routes = [
        "0. Exit Driver",
        "1. Root",
        "2. About",
        "3. Year",
        "4. Time",
        "5. Day of the Week",
        "6. Age (query)",
        "7. Age (path)",
        "8. Age (post)",
        "9. Greet (query)",
        "10. Greet (path)",
        "11. Headers",
        "12. Theme (cookies)"
    ]
    for route in routes:
        print(route)

# Show query options
def print_queries():
    print("\nQueries")
    routes = [
        "0. Exit Driver",
        "1. Show all products",
        "2. Show product name and category",
        "3. Show customer name and shipping address",
        "4. Show customer name and billing address",
        "5. Show customer and product ordered",
        "6. Show product and discount if over 30",
        "7. Show number of products in each category",
        "8. Show how many products had certain discount",
        "9. Show customers per state",
        "10. Show average price per category",
        "11. Show number of orders per customer",
    ]
    for route in routes:
        print(route)

def call_root():
    url = "http://localhost:8080/"
    response = requests.get(url)
    print(response.json())

def call_about():
    url = "http://localhost:8080/about"
    response = requests.get(url)
    print(response.json())

def call_year():
    url = "http://localhost:8080/year"
    response = requests.get(url)
    print(response.json())

def call_time():
    url = "http://localhost:8080/time"
    response = requests.get(url)
    print(response.json())

def call_day():
    url = "http://localhost:8080/day"
    response = requests.get(url)
    print(response.json())

def call_age_query():
    birth_year = input("Enter birth year: ")
    current_year = datetime.today().year
    url = f"http://localhost:8080/age?birth_year={birth_year}&current_year={current_year}"
    response = requests.get(url)
    print(response.json())

def call_age_path():
    birth_year = input("Enter birth year: ")
    current_year = datetime.today().year
    url = f"http://localhost:8080/age/{birth_year}/{current_year}"
    response = requests.get(url)
    print(response.json())

def call_age_post():
    data = {
        "name" : input("Enter name: "),
        "birth_year": input("Enter birth year: "),
        "current_year": datetime.today().year
    }
    url = f"http://localhost:8080/person"
    response = requests.post(url, json=data)
    print(response.json())

def call_name_query():
    name = input("Enter name: ")
    url = f"http://localhost:8080/name?names={name}"
    response = requests.get(url)
    print(response.json())

def call_name_path():
    name = input("Enter name: ")
    url = f"http://localhost:8080/name/{name}"
    response = requests.get(url)
    print(response.json())

def call_headers():
    email = input("Enter email: ")
    role = input("Enter role: ")
    device = input("Enter device type: ")
    headers = {
        "Content-Type": "application/json",
        "X-Custom-Header": "CustomValue",
        "user-email": email,
        "user-role": role,
        "device-type": device
    }
    url = "http://localhost:8080/headers"
    response = requests.get(url=url, headers=headers)
    print(response.json())

def call_theme():
    theme = input("Enter theme (light or dark): ")
    url = "http://localhost:8080/theme"
    cookies = {
        "theme": f"{theme}"
    }
    response = requests.get(url=url, cookies=cookies)
    print(response.json())

# Connects to MySQL
def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lab6password",
            database="my_guitar_shop"
        )
        print("Successfully connected to MySQL database!")
        return mydb

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

# Helper function to execute queries
def execute_query(sql_query, mydb = None):
    try:
        # Establish a connection to the MySQL database
        if mydb is None:
            mydb = connect_to_db()

        # Create a cursor object to execute SQL queries
        my_cursor = mydb.cursor()

        # Execute the query
        my_cursor.execute(sql_query)

        # Fetch all the results
        # Use fetchone() to retrieve a single row, or fetchmany(size) for a specific number of rows
        results = my_cursor.fetchall()

        return results

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and the database connection
        if mydb.is_connected():
            mydb.close()
        print("MySQL connection closed.")

def main():
    while True:
        options = [
            "0. Exit Driver",
            "1. FastAPI",
            "2. SQL Queries"
        ]
        for option in options:
            print(option)
        service = input("\nFastAPI or Queries: ")
        match service:
            case "0":
                exit()
            case "1":
                while True:
                    print_routes()
                    choice = input("\nChoose a Route: ")
                    match choice:
                        case "0":
                            break
                        case "1":
                            call_root()
                        case "2":
                            call_about()
                        case "3":
                            call_year()
                        case "4":
                            call_time()
                        case "5":
                            call_day()
                        case "6":
                            call_age_query()
                        case "7":
                            call_age_path()
                        case "8":
                            call_age_post()
                        case "9":
                            call_name_query()
                        case "10":
                            call_name_path()
                        case "11":
                            call_headers()
                        case "12":
                            call_theme()
            case "2":
                while True:
                    print_queries()
                    choice = input("\nEnter your choice: ")
                    match choice:
                        case "0":
                            break
                        case "1":
                            result = execute_query("SELECT * FROM products;")
                            for row in result:
                                print(row)
                        case "2":
                            result = execute_query("SELECT product_name, category_name "
                                                "FROM products INNER JOIN categories "
                                                "ON products.category_id = categories.category_id;")
                            for row in result:
                                print(row)
                        case "3":
                            result = execute_query("SELECT first_name, last_name, line1 "
                                                "FROM customers "
                                                "INNER JOIN addresses "
                                                "ON customers.shipping_address_id = addresses.address_id;")
                            for row in result:
                                print(row)
                        case "4":
                            result = execute_query("SELECT first_name, last_name, line1 "
                                                "FROM customers "
                                                "INNER JOIN addresses "
                                                "ON customers.billing_address_id = addresses.address_id;")
                            for row in result:
                                print(row)
                        case "5":
                            result = execute_query("SELECT c.first_name, c.last_name, p.product_name "
                                                "FROM customers c "
                                                "INNER JOIN orders o "
                                                "ON c.customer_id = o.customer_id "
                                                "INNER JOIN order_items oi "
                                                "ON o.order_id = oi.order_id "
                                                "INNER JOIN products p "
                                                "ON oi.product_id = p.product_id;")
                            for row in result:
                                print(row)
                        case "6":
                            result = execute_query("SELECT p.product_name, oi.discount_amount "
                                                "FROM products p "
                                                "INNER JOIN order_items oi ON oi.product_id = p.product_id "
                                                "WHERE p.discount_percent > 30;")
                            for row in result:
                                print(row)
                        case "7":
                            result = execute_query("SELECT p.category_id, COUNT(p.product_name) AS number_of_products "
                                                "FROM products p "
                                                "GROUP BY p.category_id;")
                            for row in result:
                                print(row)
                        case "8":
                            result = execute_query("SELECT p.discount_percent, COUNT(p.product_id) "
                                                "FROM products p "
                                                "GROUP BY p.discount_percent "
                                                "ORDER BY p.discount_percent DESC;")
                            for row in result:
                                print(row)
                        case "9":
                            result = execute_query("SELECT state, COUNT(c.customer_id) AS number_of_customers "
                                                "FROM addresses a "
                                                "INNER JOIN customers c ON a.address_id = c.shipping_address_id "
                                                "GROUP BY a.state ORDER BY COUNT(c.customer_id) DESC;")
                            for row in result:
                                print(row)
                        case "10":
                            result = execute_query("SELECT c.category_name, AVG(p.list_price) AS average_price "
                                                "FROM categories c  "
                                                "INNER JOIN products p ON c.category_id = p.category_id "
                                                "GROUP BY c.category_name;")
                            for row in result:
                                print(row)
                        case "11":
                            result = execute_query("SELECT c.first_name, c.last_name, COUNT(o.order_id) AS total_orders "
                                        "FROM orders o "
                                        "INNER JOIN customers c ON c.customer_id = o.customer_id  "
                                        "GROUP BY c.customer_id;")
                            for row in result:
                                print(row)

main()

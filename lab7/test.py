import unittest
import mysql.connector
import requests
from datetime import datetime

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lab6password",
            database="my_guitar_shop"
        )
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

class TestCases(unittest.TestCase):
    def test_getRoot(self):
        url = "http://localhost:8080/"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Hello Lab 1!",
        })

    def test_getAbout(self):
        url = "http://localhost:8080/about/"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "This is my FastAPI service!",
        })

    def test_getYear(self):
        url = "http://localhost:8080/year/"
        response = requests.get(url)

        expected_year = datetime.now().year

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": f"The year is now {expected_year}!",
        })

    def test_getTime(self):
        url = "http://localhost:8080/time/"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)


    def test_getDay(self):
        url = "http://localhost:8080/day/"
        response = requests.get(url)

        expected_day = datetime.now().strftime("%A")

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": f"The day is now {expected_day}!",
        })

    def test_getAge(self):
        url = "http://localhost:8080/age?birth_year=2003&current_year=2025"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "You are 22 years old!",
        })

    def test_getAgePath(self):
        url = "http://localhost:8080/age/2003/2025"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "You are 22 years old!",
        })

    def test_getPerson(self):
        url = "http://localhost:8080/person"
        data = {
            "name": "Denis",
            "birth_year": 2003,
            "current_year": 2025,
        }
        response = requests.post(url, json=data)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Denis, You are 22 years old!",
        })

    def test_getName(self):
        url = "http://localhost:8080/name?names=Denis"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Hello Denis!",
        })

    def test_getNamePath(self):
        url = "http://localhost:8080/name/Denis"
        response = requests.get(url)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "message": "Hello Denis!",
        })

    def test_getHeaders(self):
        url = "http://localhost:8080/headers/"
        headers = {
            "Content-Type": "application/json",
            "X-Custom-Header": "CustomValue",
            "user-email": "demo@example.com",
            "user-role": "admin",
            "device-type": "desktop"
        }
        response = requests.get(url=url, headers=headers)

        print("Status code:", response.status_code)
        print("Response Body:", response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {
            "user-email": "demo@example.com",
            "user-role": "admin",
            "device-type": "desktop"
        })

    def test_getTheme(self):
        url = "http://localhost:8080/theme/"
        cookies = {
            "theme": "dark"
        }
        response = requests.get(url=url, cookies=cookies)

        print("Status code: ", response.status_code)
        print("Response Body: ", response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), {"theme": "dark"})

    def test_showAllProducts(self):
        result = execute_query("SELECT * FROM products;")
        
        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 3, "Each product row should have 3 columns")

    def test_showProductCategory(self):
        result = execute_query("SELECT product_name, category_name "
                    "FROM products INNER JOIN categories "
                    "ON products.category_id = categories.category_id;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 2, "Each product row should have 2 columns")

    def test_showShippingAddresses(self):
        result = execute_query("SELECT first_name, last_name, line1 "
                                "FROM customers "
                                "INNER JOIN addresses "
                                "ON customers.shipping_address_id = addresses.address_id;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 3, "Each product row should have 3 columns")

    def test_showBillingAddresses(self):
        result = execute_query("SELECT first_name, last_name, line1 "
                                "FROM customers "
                                "INNER JOIN addresses "
                                "ON customers.billing_address_id = addresses.address_id;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 3, "Each product row should have 3 columns")

    def test_showCustomerProductOrdered(self):
        result = execute_query("SELECT c.first_name, c.last_name, p.product_name "
                            "FROM customers c "
                            "INNER JOIN orders o "
                            "ON c.customer_id = o.customer_id "
                            "INNER JOIN order_items oi "
                            "ON o.order_id = oi.order_id "
                            "INNER JOIN products p "
                            "ON oi.product_id = p.product_id;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 3, "Each product row should have 3 columns")

    def test_showDiscount(self):
        result = execute_query("SELECT p.product_name, oi.discount_amount "
                                "FROM products p "
                                "INNER JOIN order_items oi ON oi.product_id = p.product_id "
                                "WHERE p.discount_percent > 30;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 2, "Each product row should have 2 columns")

    def test_showNumProductsCategory(self):
        result = execute_query("SELECT p.category_id, COUNT(p.product_name) AS number_of_products "
                            "FROM products p "
                            "GROUP BY p.category_id;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 2, "Each product row should have 2 columns")

    def test_showCustomersPerState(self):
        result = execute_query("SELECT state, COUNT(c.customer_id) AS number_of_customers "
                            "FROM addresses a "
                            "INNER JOIN customers c ON a.address_id = c.shipping_address_id "
                            "GROUP BY a.state ORDER BY COUNT(c.customer_id) DESC;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 2, "Each product row should have 2 columns")

    def test_showAveragePriceCategory(self):
        result = execute_query("SELECT c.category_name, AVG(p.list_price) AS average_price "
                            "FROM categories c  "
                            "INNER JOIN products p ON c.category_id = p.category_id "
                            "GROUP BY c.category_name;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 2, "Each product row should have 2 columns")

    def test_showOrdersPerCustomer(self):
        result = execute_query("SELECT c.first_name, c.last_name, COUNT(o.order_id) AS total_orders "
                    "FROM orders o "
                    "INNER JOIN customers c ON c.customer_id = o.customer_id  "
                    "GROUP BY c.customer_id;")

        # Assert that we get results back
        self.assertIsNotNone(result, "Query should return results")
        
        # Print results for debugging
        print(f"Number of products found: {len(result)}")
            
        # Validate structure - each row should have the expected number of columns
        # Based on typical products table structure
        if len(result) > 0:
            first_row = result[0]
            self.assertIsInstance(first_row, tuple, "Each row should be a tuple")
            self.assertEqual(len(first_row), 3, "Each product row should have 3 columns")
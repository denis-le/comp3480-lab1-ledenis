import mysql.connector

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_guitar_shop"
        )
        print("Successfully connected to MySQL database!")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

    return mydb

def query_addresses(mydb):
    try:
        # Establish a connection to the MySQL database
        if mydb == None:
            print("reconnection to db required")
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="my_guitar_shop"
            )

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Define the SQL SELECT query
        sql_query = "select address_id, line1 from addresses a"

        # Execute the query
        mycursor.execute(sql_query)

        # Fetch all the results
        # Use fetchone() to retrieve a single row, or fetchmany(size) for a specific number of rows
        results = mycursor.fetchall()

        # Iterate through the fetched results and print them
        for row in results:
            print(f"address_id: {row[0]}, address_line1: {row[1]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and the database connection
        if mydb.is_connected():
            mydb.close()
        print("MySQL connection closed.")


def main():
    mydb = connect_to_db()
    query_addresses(mydb)

main()

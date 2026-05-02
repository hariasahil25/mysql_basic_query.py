# Program to perform a basic SQL query on a MySQL database

import mysql.connector
from mysql.connector import Error


def run_basic_query():
    connection = None
    cursor = None

    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="student_db"
        )

        if connection.is_connected():
            print("Connected to MySQL database")

            # Create cursor
            cursor = connection.cursor()

            # Basic SQL query
            query = "SELECT id, name, age FROM students"

            # Execute query
            cursor.execute(query)

            # Fetch all rows
            records = cursor.fetchall()

            print("\nStudent Records:\n")

            if records:
                for record in records:
                    print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}")
            else:
                print("No records found.")

    except Error as e:
        print("Database error:", e)

    finally:
        # Close resources
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()
            print("\nMySQL connection closed")


# Run the program
run_basic_query()

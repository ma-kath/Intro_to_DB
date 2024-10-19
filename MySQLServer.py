import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',          # Replace with your host, e.g., 'localhost'
            user='your_username',      # Replace with your MySQL username
            password='your_password'   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Attempt to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
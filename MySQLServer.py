import mysql.connector

def create_database(host, user, password, database_name):
  """
  Attempts to create a database with the given name.

  Args:
      host (str): The hostname of the MySQL server.
      user (str): The username to connect to the server.
      password (str): The password for the user.
      database_name (str): The name of the database to create.

  Returns:
      None
  """

  try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = connection.cursor()

    # Create database (ignore errors if it already exists)
    try:
      cursor.execute(f"CREATE DATABASE {database_name}")
      print(f"Database '{database_name}' created successfully!")
    except mysql.connector.Error as err:
      # Likely a "Database exists" error, so we can ignore it
      pass

  except mysql.connector.Error as err:
    print(f"Error connecting to MySQL server: {err}")
  finally:
    if connection:
      connection.close()
      cursor.close()  # Close cursor even if creation failed

# Replace with your actual MySQL server credentials
host = "localhost"  # Replace with your MySQL server hostname
user = "your_username"  # Replace with your MySQL username
password = "your_password"  # Replace with your MySQL password
database_name = "alx_book_store"

create_database(host, user, password, database_name)

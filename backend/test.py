import mysql.connector as connector

try:
    print("Attempting connection...")
    connection = connector.connect(
        host="127.0.0.1",     
        database='main',
        user='root',
        password = '8411',
        port=3306
    )
    print("Connection successful!")

    cursor = connection.cursor()
    print("Cursor created:", cursor)
except connector.Error as err:
    print(f"Error: {err}")




















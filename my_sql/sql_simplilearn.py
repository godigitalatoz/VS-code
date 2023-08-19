import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_server_connection (host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password)
        print ("MySQL connection sucessful")
    except Error as err:
        print(f"Error: '{err}")
    return connection        
# put MYSQL terminal password
pw = "paindabad&786" 

# Database name
db = "mysql_python"
connection = create_server_connection("localhost", "root", pw)

# create mysql_python
def create_database(connection, querry):
    cursor = connection.cursor()
    try:
        cursor.execute(querry)
        print("Database created")
    except Error as err:
        print(f"Error: '{err}'")
create_database_querry = "CREATE DATABASE mysql_python"
create_database(connection, create_database_querry)
#

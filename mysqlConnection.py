from mysql.connector import connect
# dotenv lets me hide important details in a .env file
from dotenv import load_dotenv
# os module allows code to access the os so we can read our hidden variables
import os

load_dotenv

# attempts to make a connection to the mysql server
def get_mysql_connection():
    return connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
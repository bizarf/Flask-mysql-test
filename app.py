from flask import Flask
from mysqlConnection import get_mysql_connection
from mysql.connector import Error


app = Flask(__name__)
# the connection doesn't get created straight away, so we need to try first or else it won't exist
try:
    connection = get_mysql_connection()
    print("Database connection established successfully.")
except Error as e:
    print("Error connecting to database:", e)

# index route
@app.route("/")
def index():
    return "<p>Index</p>"


# create a table
@app.route("/create-car-table")
def createCarTable():
    create_car_table_query = """
    CREATE TABLE IF NOT EXISTS cars(
        id INT AUTO_INCREMENT PRIMARY KEY,
        carBrand VARCHAR(50),
        carModel VARCHAR(50),
        carType VARCHAR(50)
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_car_table_query)
        connection.commit()
    return "Car table created"

# show all tables in the database. don't use commit, because we're not committing anything to the database
@app.route("/show-tables")
def showTables():
    show_table_query = "SHOW TABLES;"
    with connection.cursor() as cursor:
        cursor.execute(show_table_query)
        # loop through the tables in the print statement
        for db in cursor:
            print(db)
    return "Showing tables. Check terminal"


# @app.route("/show-all-records")
# def show():
#     return 
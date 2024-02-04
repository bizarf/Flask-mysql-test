from flask import Flask
from flask import render_template
from mysqlConnection import get_mysql_connection
from mysql.connector import Error


app = Flask(__name__)
# the connection doesn't get created straight away, so we need to try first or else it won't exist
try:
    connection = get_mysql_connection()
    cursor = connection.cursor()
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
    try:
        tableList = []
        show_tableList_query = "SHOW TABLES;"
        cursor.execute(show_tableList_query)
        for db in cursor:
            tableList.append(db)
        return render_template("tableList.html", tableList=tableList)
    except Error as e:
        print(f"An error occurred: {e}")

# dynamically load a table and render it's contents
@app.route("/show-tables/table/<tableName>")
def showTableData(tableName):
    try:
        table = []
        tableDef = []
        show_table_query = f"SELECT * FROM {tableName};"
        describe_table_query = f"DESCRIBE {tableName};"
        cursor.execute(show_table_query)
        rows = cursor.fetchall()
        for row in rows:
            table.append(row)
        
        cursor.execute(describe_table_query)
        for db in cursor:
            tableDef.append(db)
                   
        return render_template("table.html", table=table, tableName=tableName, tableDef=tableDef)
    except Error as e:
        print(f"An error occurred: {e}")
    return "beep beep"

# @app.route("/show-all-records")
# def show():
#     return 
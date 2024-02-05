from flask import Flask, request, redirect, url_for
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


# fetch all rows in a table
def fetchTableRows(tableName):
    show_table_query = f"SELECT * FROM {tableName};"
    cursor.execute(show_table_query)
    tableRows = cursor.fetchall()
    return tableRows


# fetch all columns in a table
def fetchTableColumns(tableName):
    describe_table_query = f"DESCRIBE {tableName};"
    cursor.execute(describe_table_query)
    tableColumns = cursor.fetchall()
    return tableColumns


# index route
@app.route("/")
def index():
    return render_template("index.html")


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
        show_tableList_query = "SHOW TABLES;"
        cursor.execute(show_tableList_query)
        tableList = cursor.fetchall()
        
        return render_template("tableList.html", tableList=tableList)
    except Error as e:
        print(f"An error occurred: {e}")


# dynamically load a table and render it's contents
@app.route("/show-tables/table/<tableName>")
def showTableData(tableName):
    try:
        tableRows = fetchTableRows(tableName)
        tableColumns = fetchTableColumns(tableName)

        return render_template("table.html", tableRows=tableRows, tableName=tableName, tableColumns=tableColumns)
    except Error as e:
        print(f"An error occurred: {e}")


@app.route("/show-tables/table/<tableName>/add", methods=["GET", "POST"])
def addData(tableName):
    if request.method == "POST":
        try:
            columns = ", ".join(request.form.keys())
            row = ", ".join(request.form.values())
            insert_row_query = f"INSERT INTO {tableName}({columns}) VALUES ({row})"
            cursor.execute(insert_row_query)
            connection.commit()
            return redirect(url_for("showTableData", tableName=tableName))
        except Error as e:
            print(f"An error occurred: {e}")
    else:
        try:
            tableColumns = fetchTableColumns(tableName)
            return render_template("insertDataForm.html", tableName=tableName, tableColumns=tableColumns)
        except Error as e:
            print(f"An error occurred: {e}")
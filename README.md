# Flask-mysql-test

This is just a personal project where I'm playing around with Flask with the MySQL connector.

#### Install:

To run this project on your locally, first clone the repo and enter the folder in your terminal. Now setup a VENV with the command:

```
python -m venv venv
```

After that has been created activate the virtual environment by typing in your terminal:

```
venv\Scripts\activate
```

Now to install the project dependencies type:

```
pip install -r requirements.txt
```

Now create a file called ".env" and inside it add:

```
MYSQL_HOST="(your MySQL hostname)"
MYSQL_USER="(your MySQL username)"
MYSQL_PASSWORD="(your MySQL password)"
MYSQL_DATABASE="(the MySQL database that you want to use)"
```

When everything has been done, we can start the server with:

```
flask --app app run
```

<hr>
#### Features

-   []

<hr>

##### Tools and technologies used:

-   Python
-   Flask
-   MySQL connector

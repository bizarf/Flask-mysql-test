from flask import Flask
from flask import render_template
import mysqlConnection

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Index</p>"


@app.route("/hello")
# def hello_world():
#     return "<p>Hello World</p>"
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)
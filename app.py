from flask import Flask, render_template
from mysql import connector

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html")

@app.route("/crow")
def crow():
    mydb = connector.connect(
        host="db",
        user="root",
        password="daswid",
        database="crowbase"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM crow")

    res = mycursor.fetchall()
    return render_template("crow.html", crow=res)
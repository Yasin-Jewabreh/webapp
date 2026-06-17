import database
from flask import Flask, render_template, redirect, url_for, request
from flsk_sqlalchemy import SQLAlchemy
from sqlalchemy import orm
import os 
import database

app = Flask(__name__)

os.makedirs(app.instance_path, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pflegehilfe.db"

db = SQLAlchemy()
db.init_app(app)

database.init_app(app)

@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/db-test")
def db_test():
    db_con = database.get_db_con()
    result =db_con.execute("Select 1").fetchone() #ohne fetchone würde es nur drauf zeigen: <sqlite3.Cursor object at 0x...>

    return f"Datenbank funktioniert: {result[0]}"

@app.route("Kalender")
def kalender():
    return render_template("calendar.html")

if __name__ == "__main__":
    app.run(debug=True)
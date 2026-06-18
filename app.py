from db import db
from flask import Flask, render_template, redirect, url_for, request
import models

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/termine")
def kalender():
    return render_template("termine.html")

if __name__ == "__main__":
    app.run(debug=True)
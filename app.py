from db import db
from flask import Flask, render_template, redirect, url_for, request
import models
from models import Nutzer, Auftrag
from flask_login import LoginManager, login_user, login_required, current_user

from datetime import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return Nutzer.query.get(int(user_id))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        neuer_nutzer = Nutzer(
            vorname = request.form["vorname"],
            nachname = request.form["nachname"],
            geschlecht = request.form["geschlecht"],
            geburtsdatum = datetime.strptime(
    request.form["geburtsdatum"],
    "%Y-%m-%d"
).date(),
            adresse = request.form["adresse"],
            plz = request.form["plz"],
            ort = request.form["ort"],
            email = request.form["email"],
            telefonnummer = request.form["telefonnummer"],
            passwort = request.form["passwort"],
            rolle = request.form["rolle"]
        )

        db.session.add(neuer_nutzer)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        passwort = request.form["passwort"]

        nutzer = Nutzer.query.filter_by(email=email).first()

        if nutzer and nutzer.passwort == passwort:
            login_user(nutzer)
            return redirect(url_for("auftraege_start"))

    return render_template("login.html")

@app.route("/auftraege")
@login_required
def auftraege_start():
    if current_user.rolle == "PP":
        return redirect (url_for("auftrag_erstellen"))

    if current_user.rolle == "Helfer":
        return redirect (url_for("helfer_auftraege"))

    return "Unbekante Benutzerrolle", 403

@app.route("/auftrag/erstellen", methods =["GET", "POST"])
@login_required
def auftrag_erstellen():
    if request.method == "POST":
        neuer_auftrag = Auftrag(
            wohnsituation = request.form["wohnsituation"],
            beschreibung = request.form["beschreibung"],
            status = "offen",
            nutzer_id = current_user.id
        )

        db.session.add(neuer_auftrag)
        db.session.commit()

        return redirect(url_for("auftraege_start"))
    
    return render_template(
        "auftrag_erstellen.html",
        nutzer = current_user
    )


@app.route("/termine")
def kalender():
    return render_template("termine.html")

if __name__ == "__main__":
    app.run(debug=True)
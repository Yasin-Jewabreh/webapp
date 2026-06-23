import os 
from datetime import date, datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from models import Nutzer, Auftrag, Termin, Nachricht
from forms import AuftragFormular
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask import session 
from db import db
from forms import AuftragFormular


app = Flask(__name__)
app.secret_key = "helpyourneighbour"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Nutzer, int(user_id))

db.init_app(app)
bootstrap = Bootstrap5(app)
with app.app_context():
    db.create_all()

@app.route("/")
def startseite():
    return render_template("startseite.html")

@app.route("/rolle-auswaehlen")
def rolle_auswaehlen():
    return render_template("rolle_auswaehlen.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        neuer_nutzer = Nutzer(
            vorname = request.form["vorname"],
            nachname = request.form["nachname"],
            geschlecht = request.form["geschlecht"],
            geburtsdatum = datetime.strptime(request.form["geburtsdatum"], "%Y-%m-%d").date(),
            adresse = request.form["adresse"],
            plz = request.form["plz"],
            ort = request.form["ort"],
            email = request.form["email"],
            telefon = request.form["telefonnummer"],
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

            if nutzer.rolle == "hilfe_anbietend":
                return redirect(url_for("helfer_auftraege"))
            else:
                return redirect(url_for("auftrag_erstellen"))

    return render_template("login.html")



@app.route("/logout")
@login_required
def logout():
    logout_user()  
    session.clear() 
    return redirect(url_for("login")) 

@app.route("/auftrag/erstellen", methods=["GET", "POST"])
@login_required
def auftrag_erstellen():

    form = AuftragFormular()
    
    if form.validate_on_submit():
        neuer_auftrag = Auftrag(
            wohnsituation=form.wohnsituation.data,
            beschreibung=form.beschreibung.data,
            nutzer_id=current_user.id
        )
        db.session.add(neuer_auftrag)
        db.session.commit()
        flash("Dein Auftrag wurde erfolgreich erstellt!", "success")
        return redirect(url_for("startseite"))
    return render_template("auftrag_erstellen.html", nutzer=current_user, form=form)

@app.route("/termine")
def kalender():
    return render_template("termine.html")

@app.route("/helfer/auftraege")
@login_required
def helfer_auftraege():
    
    if current_user.rolle != "hilfe_anbietend":
        return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403

    offene_auftraege = Auftrag.query.filter_by(angenommen="offen").all()
    heute = date.today()
    return render_template("helfer_auftraege.html", auftraege=offene_auftraege, heute=heute)


@app.route("/helfer/auftrag/<int:auftrag_id>")
@login_required
def auftrag_annehmen(auftrag_id):
    
    
    if current_user.rolle != "hilfe_anbietend":
        return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403
  
    auftrag = db.session.get(Auftrag, auftrag_id)
    if not auftrag:
        return "Auftrag nicht gefunden", 404
    
    auftrag.angenommen = "angenommen"
    
    nutzer_id = current_user.id
    
    db.session.commit()
    return render_template("auftrag_angenommen.html", auftrag=auftrag)

@app.route("/helfer/meine-auftraege")
@login_required
def meine_auftraege():

    if current_user.rolle != "hilfe_anbietend":
        return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403
    
    meine_auftraege = Auftrag.query.filter_by(nutzer_id=current_user.id, angenommen="angenommen").all()


    return render_template("meine_auftraege.html", auftraege=meine_auftraege)



@app.route("/chat/<int:empfaenger_id>", methods=["GET", "POST"])
def chat(empfaenger_id):
    if request.method == "POST":
        neue_nachricht = Nachricht(
            inhalt=request.form["inhalt"],
            sender_id=1,
            empfaenger_id=empfaenger_id
        )
        db.session.add(neue_nachricht)
        db.session.commit()
    nachrichten = Nachricht.query.filter(
        (Nachricht.sender_id == 1) |
        (Nachricht.empfaenger_id == 1)
    ).all()
    return render_template("chat.html", nachrichten=nachrichten)

if __name__ == "__main__":
   with app.app_context():
        #db.drop_all()    
        db.create_all()  
    
app.run(debug=True, port=8080)
import os 
from datetime import date, datetime
from flask import Flask, render_template, redirect, url_for, request, session
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Nutzer, Auftrag, Termin, Nachricht, berlin_time
from forms import AuftragFormular

app = Flask(__name__)
app.secret_key = "helpyourneighbour"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

db.init_app(app)
bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Nutzer, int(user_id))

with app.app_context():
    db.create_all()

@app.route("/")
def startseite():
    return render_template("startseite.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        neuer_nutzer = Nutzer(
            vorname=request.form["vorname"],
            nachname=request.form["nachname"],
            geschlecht=request.form["geschlecht"],
            geburtsdatum=datetime.strptime(request.form["geburtsdatum"], "%Y-%m-%d").date(),
            adresse=request.form["adresse"],
            plz=request.form["plz"],
            ort=request.form["ort"],
            email=request.form["email"],
            telefon=request.form["telefonnummer"],
            passwort=request.form["passwort"],
            rolle=request.form["rolle"]
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
            if nutzer.rolle == "helfer":
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

@app.route("/auftraege")
@login_required
def auftraege_start():
    if current_user.rolle == "helfer":
        return redirect(url_for("helfer_auftraege"))
    else:
        return redirect(url_for("auftrag_erstellen"))

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
        return redirect(url_for("auftraege_start"))
    return render_template("auftrag_erstellen.html", nutzer=current_user, form=form)

@app.route("/termine")
def kalender():
    return render_template("termine.html")

@app.route("/helfer/auftraege")
@login_required
def helfer_auftraege():
    if current_user.rolle != "helfer":
        return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403
    offene_auftraege = Auftrag.query.filter_by(angenommen="offen").all()
    heute = date.today()
    return render_template("helfer_auftraege.html", auftraege=offene_auftraege, heute=heute)

@app.route("/helfer/auftrag/<int:auftrag_id>")
@login_required
def auftrag_annehmen(auftrag_id):
    if current_user.rolle != "helfer":
        return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403
    auftrag = db.session.get(Auftrag, auftrag_id)
    if not auftrag:
        return "Auftrag nicht gefunden", 404
    auftrag.angenommen = "angenommen"
    db.session.commit()
    return redirect(url_for("chat", empfaenger_id=auftrag.nutzer_id))

@app.route("/chat", methods=["GET"])
@app.route("/chat/<int:empfaenger_id>", methods=["GET", "POST"])
@login_required
def chat(empfaenger_id=None):
    # 1. Alle Chatpartner ermitteln
    gesendete_nachrichten = Nachricht.query.filter_by(sender_id=current_user.id).all()
    empfangene_nachrichten = Nachricht.query.filter_by(empfaenger_id=current_user.id).all()
    
    partner_ids = set()
    for n in gesendete_nachrichten:
        partner_ids.add(n.empfaenger_id)
    for n in empfangene_nachrichten:
        partner_ids.add(n.sender_id)
    
    partner_ids.discard(current_user.id)
    
    chat_partner = Nutzer.query.filter(Nutzer.id.in_(partner_ids)).all() if partner_ids else []

    aktiver_partner = None
    nachrichten = []
    
    if empfaenger_id:
        aktiver_partner = db.session.get(Nutzer, empfaenger_id)
        
        if aktiver_partner and aktiver_partner not in chat_partner:
            chat_partner.append(aktiver_partner)

        if request.method == "POST" and request.form.get("inhalt"):
            neue_nachricht = Nachricht(
                inhalt=request.form["inhalt"],
                sender_id=current_user.id,
                empfaenger_id=empfaenger_id,
                zeitstempel=berlin_time()
            )
            db.session.add(neue_nachricht)
            db.session.commit()
            return redirect(url_for("chat", empfaenger_id=empfaenger_id))

        nachrichten = Nachricht.query.filter(
            ((Nachricht.sender_id == current_user.id) & (Nachricht.empfaenger_id == empfaenger_id)) |
            ((Nachricht.sender_id == empfaenger_id) & (Nachricht.empfaenger_id == current_user.id))
        ).order_by(Nachricht.zeitstempel.asc()).all()

    return render_template(
        "chat.html",
        chat_partner=chat_partner,
        aktiver_partner=aktiver_partner,
        nachrichten=nachrichten
    )

if __name__ == "__main__":
    app.run(debug=True)
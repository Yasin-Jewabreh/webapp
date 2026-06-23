import os 
from datetime import date, datetime
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from db import db
from models import Nutzer, Auftrag, Termin, Nachricht
from forms import RollenWahlForm, RegisterForm, LoginForm, AuftragFormular, ProfilFormular 

app = Flask(__name__)
app.secret_key = "helpyourneighbour"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"
os.makedirs(app.instance_path, exist_ok=True)


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
@app.route("/startseite")
def startseite():
    return render_template("startseite.html")


@app.route('/rolle_auswaehlen', methods=['GET', 'POST'])
def rolle_waehlen():
    form = RollenWahlForm()
    
    if form.validate_on_submit():

        if form.helfer_btn.data:
            gewaehlte_rolle = "Helfer"
        elif form.suchender_btn.data:
            gewaehlte_rolle = "PP"
        else:
            gewaehlte_rolle = "PP"

       
        session["rollenwahl"] = gewaehlte_rolle
        return redirect(url_for('register'))

    return render_template('rolle_auswaehlen.html', form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        
        gewaehlte_rolle = session.get("rollenwahl", "PP")
        
        neuer_nutzer = Nutzer(
            vorname=form.vorname.data,
            nachname=form.nachname.data,
            geschlecht=form.geschlecht.data,
            geburtsdatum=form.geburtsdatum.data,
            adresse=form.adresse.data,
            plz=form.plz.data,
            ort=form.ort.data,
            email=form.email.data,
            telefon=form.telefonnummer.data,
            passwort=form.passwort.data,
            rolle=gewaehlte_rolle
        )

        db.session.add(neuer_nutzer)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    fehler = None 

    if form.validate_on_submit():
        email = form.email.data
        passwort = form.passwort.data
        
        
        nutzer = db.session.execute(db.select(Nutzer).where(Nutzer.email == email)).scalars().first()
        
        if not nutzer:
            fehler = "Benutzer nicht vorhanden. Bitte prüfe deine Eingabe oder registriere dich neu!"
            flash(fehler)
        else:
            if nutzer.passwort == passwort:
                
                login_user(nutzer)
                
                
                if nutzer.rolle == "Helfer":
                    return redirect(url_for("dashboard"))
                else:
                    return redirect(url_for("dashboard"))
            else:
                fehler = "Passwort oder Emailadresse falsch!"
                flash(fehler)

    return render_template("login.html", form=form, fehler=fehler)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route("/profil", methods=["GET", "POST"])
@login_required
def profil():
    form = ProfilFormular()

    if form.validate_on_submit():
        
        current_user.vorname = form.vorname.data
        current_user.nachname = form.nachname.data
        current_user.email = form.email.data
        current_user.telefon = form.telefon.data
        current_user.adresse = form.adresse.data
        current_user.plz = form.plz.data
        current_user.ort = form.ort.data
        
        db.session.commit()
        flash("Profil erfolgreich aktualisiert!", "success")
        return redirect(url_for("dashboard"))

    
    elif request.method == "GET":
        form.vorname.data = current_user.vorname
        form.nachname.data = current_user.nachname
        form.email.data = current_user.email
        form.telefon.data = current_user.telefon 
        form.adresse.data = current_user.adresse
        form.plz.data = current_user.plz
        form.ort.data = current_user.ort

    return render_template("profil.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()  
    session.clear() 
    return redirect(url_for("startseite")) 


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
        return redirect(url_for("dashboard"))
        
    return render_template("auftrag_erstellen.html", nutzer=current_user, form=form)


@app.route("/termine")
def kalender():
    return render_template("termine.html")


@app.route("/helfer/auftraege")
@login_required
def helfer_auftraege():
    if current_user.rolle != "Helfer":
        return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403

    offene_auftraege = Auftrag.query.filter_by(angenommen="offen").all()
    heute = date.today()
    return render_template("helfer_auftraege.html", auftraege=offene_auftraege, heute=heute)


@app.route("/helfer/auftrag/<int:auftrag_id>")
@login_required
def auftrag_annehmen(auftrag_id):
    if current_user.rolle != "Helfer":
        return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403
  
    auftrag = db.session.get(Auftrag, auftrag_id)
    if not auftrag:
        return "Auftrag nicht gefunden", 404
    
    auftrag.angenommen = "angenommen"
    db.session.commit()
    return render_template("auftrag_angenommen.html", auftrag=auftrag)


@app.route("/chat/<int:empfaenger_id>", methods=["GET", "POST"])
@login_required  # Wichtig, damit current_user existiert!
def chat(empfaenger_id):
    if request.method == "POST":
        neue_nachricht = Nachricht(
            inhalt=request.form["inhalt"],
            sender_id=current_user.id,  # Dynamisch!
            empfaenger_id=empfaenger_id
        )
        db.session.add(neue_nachricht)
        db.session.commit()
    
    # Filtert Nachrichten zwischen dem aktuellen User und dem Empfänger
    nachrichten = Nachricht.query.filter(
        ((Nachricht.sender_id == current_user.id) & (Nachricht.empfaenger_id == empfaenger_id)) |
        ((Nachricht.sender_id == empfaenger_id) & (Nachricht.empfaenger_id == current_user.id))
    ).all()
    
    return render_template("chat.html", nachrichten=nachrichten)

if __name__ == "__main__":
    app.run(debug=True)
import os 
from datetime import date, datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Nutzer, Auftrag, Termin, Nachricht
from forms import AuftragFormular

app = Flask(__name__)
app.secret_key = "helpyourneighbour"

from db import db
from models import Termin, Nutzer, Auftrag, Nachricht

app.config["SECRET_KEY"] = "secret_key_just_for_dev_environment"
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

app = Flask(__name__)

app.secret_key = "your_secret_key"
os.makedirs(app.instance_path, exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pflegehilfe.db"
app.config["SECRET_KEY"]= "ein_geheimes_passwort"


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Nutzer, int(user_id))

db.init_app(app)
bootstrap = Bootstrap5(app)


@app.route("/")
def startseite():
    return render_template("startseite.html")

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

@app.route("/termine/historie/", methods = ["GET"])
def historie():
    aktueller_nutzer = db.session.execute(db.select(Nutzer).where(Nutzer.rolle == "Helfer")).scalars().first()

    if aktueller_nutzer.rolle == "Helfer":
        erledigte_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif aktueller_nutzer.rolle == "PP":
        erledigte_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    if request.method == "GET":
        return render_template("historie.html", erledigte = erledigte_termine , nutzer= aktueller_nutzer)


@app.route("/termine/", methods = ["GET", "POST"])
def termine():
    form = forms.TerminErstellenForm()

    aktueller_nutzer = db.session.execute(db.select(Nutzer).where(Nutzer.rolle == "Helfer")).scalars().first()
    if not aktueller_nutzer:
        return ("Es gibt keinen Nutzer")
  
    bestaetigte_termine = []
    offene_termine = []
    warten_auf_antwort_termine = []

    if aktueller_nutzer.rolle == "Helfer":
        verfuegbare_auftraege = aktueller_nutzer.angenommene_auftraege
        if not verfuegbare_auftraege:
            return("Du hast noch keinen Auftrag angenommen. Bitte Vereinbare zunächst einen Termin!")
        form.teilnehmer.choices = [(a.id, f"{a.pp.vorname} {a.pp.nachname} - {a.pp.adresse}") for a in verfuegbare_auftraege]
        form.teilnehmer.choices.insert(0,(0, "---Bitte wählen---"))
        bestaetigte_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        offene_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id != aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        warten_auf_antwort_termine = db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id == aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif aktueller_nutzer.rolle == "PP":
        verfuegbare_auftraege = aktueller_nutzer.erstellte_auftraege
        form.teilnehmer.choices = [(a.id, f"{a.helfer.vorname} {a.helfer.nachname}") for a in verfuegbare_auftraege]
        form.teilnehmer.choices.insert(0,(0, "---Bitte wählen---"))
        bestaetigte_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        offene_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id != aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        warten_auf_antwort_termine = db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id == aktueller_nutzer.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    
    if request.method == "GET":
        if request.args.get('json') is not None:
            json_ausgabe = {}
            for schluessel, liste in [("bestaetigte", bestaetigte_termine), 
                                      
                                      ("offene", offene_termine),

                                      ("wartende", warten_auf_antwort_termine)]:
                json_ausgabe[schluessel]= [{
                    "id": t.id,
                    "helfer_id": t.helfer_id,
                    "pp_id": t.pp_id,
                    "auftrag_id": t.auftrag_id,
                    "notizen": t.notizen,
                    "datum": str(t.datum),
                    "uhrzeit_beginn": str(t.uhrzeit_beginn),
                    "uhrzeit_ende": str(t.uhrzeit_ende),
                    "complete": t.complete,
                    "bestaetigt": t.bestaetigt
                }for t in liste]
            return json_ausgabe
        else:
            return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= aktueller_nutzer)
    else:
        if "erledigen_id" in request.form:
            termin_id = int(request.form.get("erledigen_id"))
            termin = db.session.get(Termin,termin_id)
            if termin:
                termin.complete = True
                db.session.commit()
                flash("Termin als erledigt markiert!", "success")
            return redirect(url_for("termine"))
        
        if "bestaetigen_id" in request.form:
            termin_id = int(request.form.get("bestaetigen_id"))
            termin = db.session.get(Termin,termin_id)
            if termin:
                termin.bestaetigt = True
                db.session.commit()
                flash("Termin erfolgreich bestätigt!", "success")
            return redirect(url_for("termine"))
       
        if "ablehnen_id" in request.form:
            termin_id = int(request.form.get("ablehnen_id"))
            termin = db.session.get(Termin,termin_id)
            if termin:
                db.session.delete(termin)  
                db.session.commit()
                flash("Termin abgelehnt!", "warning")
            return redirect(url_for("termine"))

        if form.validate():

            gewaehlter_auftrag_id = int(form.teilnehmer.data)
            auftrag = db.session.get(Auftrag, gewaehlter_auftrag_id)

            ueberschneidung = db.session.execute(db.select(Termin).where(
                Termin.datum == form.datum.data,
                Termin.complete == False,
                (Termin.helfer_id == auftrag.helfer_id)| (Termin.pp_id == auftrag.pp_id),
                Termin.uhrzeit_beginn < form.uhrzeit_ende.data,
                Termin.uhrzeit_ende > form.uhrzeit_beginn.data)).scalars().first()

            if ueberschneidung:
                    flash("Fehler: Zu dieser Uhrzeit gibt es eine Terminüberschneidung!", "danger")
                    return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= aktueller_nutzer)
            termin = Termin(helfer_id = auftrag.helfer.id,
                            auftrag_id = auftrag.id,
                            pp_id = auftrag.pp_id,
                            notizen = form.notizen.data, 
                            datum=form.datum.data, 
                            uhrzeit_beginn = form.uhrzeit_beginn.data, 
                            uhrzeit_ende = form.uhrzeit_ende.data,
                            ersteller_id = aktueller_nutzer.id                                                       
                            )
            db.session.add(termin)
            db.session.commit()
            flash("Termin wurde eingetragen.", "success")
            return redirect(url_for("termine"))
        else:
            flash("Der Termin konnte leider nicht eingetragen werden", "warning")
        return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= aktueller_nutzer)



@app.route('/termine/<int:id>', methods=['GET', 'POST'])
def termin(id):
    termin = db.session.get(Termin, id) 
    form = forms.TerminBearbeiternForm(obj=termin)
    
    aktueller_nutzer = db.session.execute(db.select(Nutzer).where(Nutzer.rolle == "Helfer")).scalars().first()

    if aktueller_nutzer.rolle == "Helfer":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.helfer_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.pp.vorname} {a.pp.nachname} - {a.pp.adresse}") for a in verfuegbare_auftraege]

    elif aktueller_nutzer.rolle == "PP":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.pp_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.helfer.vorname} {a.helfer.nachname}") for a in verfuegbare_auftraege]

    if request.method == 'GET':
        if termin:
            return render_template('termin-bearbeiten.html', form=form)
        else:
            abort(404)
    else:
        if form.speichern.data == True:
            if form.validate():
                form.populate_obj(termin)
                
                gewaehlter_auftrag_id = int(form.teilnehmer.data)
                auftrag = db.session.get(Auftrag, gewaehlter_auftrag_id)

                ueberschneidung = db.session.execute(db.select(Termin).where(
                    Termin.id != id,
                    Termin.datum == form.datum.data,
                    Termin.complete == False,
                    (Termin.helfer_id == auftrag.helfer_id)| (Termin.pp_id == auftrag.pp_id),
                    Termin.uhrzeit_beginn < form.uhrzeit_ende.data,
                    Termin.uhrzeit_ende > form.uhrzeit_beginn.data)).scalars().first()

                if ueberschneidung:
                    flash("Fehler: Zu dieser Uhrzeit gibt es eine Terminüberschneidung!", "danger")
                    return redirect(url_for('termin', id=id))
                termin.auftrag_id= gewaehlter_auftrag_id
                termin.pp_id = auftrag.pp.id
                termin.helfer_id = auftrag.helfer.id
                termin.bestaetigt = False
                termin.ersteller_id = aktueller_nutzer.id
                db.session.add(termin)
                db.session.commit()
                flash("Deine Änderungen wurden erfolgreich gespeichert", "success")
                return redirect(url_for('termine'))
            else:
                flash("Deine Änderungen konnten leider nicht gespeichert werden!", "warning")
            return render_template('termin-bearbeiten.html', form=form)
        elif form.entfernen.data == True:
            db.session.delete(termin)  
            db.session.commit()
            flash("Der Termin wurde erfolgreich gelöscht!", "success")
            return redirect(url_for('termine'), 303)
        elif form.zurueck.data == True:
            return redirect(url_for('termine'))
        else:
            flash("Nichts passiert", "info")
            return redirect(url_for('termin', id=id))
        

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
    return render_template("auftrag_angenommen.html", auftrag=auftrag)

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
    app.run(debug=True)
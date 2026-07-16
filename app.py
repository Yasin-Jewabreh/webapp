from datetime import date, datetime
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms import TerminBearbeiternForm, TerminErstellenForm, RollenWahlForm, RegistrierungFormular, LoginFormular, AuftragFormular, ProfilFormular
from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
from flask_bootstrap import Bootstrap5
from db import db
from models import Nutzer, Auftrag, Termin, Nachricht, berlin_time

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret_key_just_for_dev_environment"
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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
    form = RegistrierungFormular()
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
            telefon=form.telefon.data,
            passwort=form.passwort.data,
            rolle=gewaehlte_rolle
        )
        db.session.add(neuer_nutzer)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginFormular()
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
    # Prüfen ob Formular abgeschickt wurde und ob alle Pflichtfelder gefüllt sind
    if form.validate_on_submit():
        # Es wird ein neuer Auftrag mit den Daten angelegt
        neuer_auftrag = Auftrag(
            wohnsituation=form.wohnsituation.data,
            beschreibung=form.beschreibung.data,
            pp_id=current_user.id 
        )
        # Hinzufügen in die DB
        db.session.add(neuer_auftrag)
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("auftrag_erstellen.html", nutzer=current_user, form=form)

@app.route("/termine/historie/", methods = ["GET"])
@login_required
def historie():

    if current_user.rolle == "Helfer":
        erledigte_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif current_user.rolle == "PP":
        erledigte_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == current_user.id,Termin.complete == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    if request.method == "GET":
        return render_template("historie.html", erledigte = erledigte_termine , nutzer= current_user)


@app.route("/termine/", methods = ["GET", "POST"])
@login_required
def termine():
    form = TerminErstellenForm()
    form.teilnehmer.choices = [(0, "---Bitte wählen---")]

    verfuegbare_auftraege = []
    bestaetigte_termine = []
    offene_termine = []
    warten_auf_antwort_termine = []

    if current_user.rolle == "Helfer":
        verfuegbare_auftraege = current_user.angenommene_auftraege
        if verfuegbare_auftraege:
            form.teilnehmer.choices += [(a.id, f"{a.pp.vorname} {a.pp.nachname} - {a.pp.adresse}") for a in verfuegbare_auftraege]

        else:
            flash("Um Termine zu vereinbaren, nimm bitte erstmal einen Auftrag an!", "info")
        bestaetigte_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == False,Termin.bestaetigt == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        offene_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id != current_user.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        warten_auf_antwort_termine = db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id == current_user.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif current_user.rolle == "PP":
        verfuegbare_auftraege = current_user.erstellte_auftraege
        if verfuegbare_auftraege:
            form.teilnehmer.choices += [(a.id, f"{a.helfer.vorname} {a.helfer.nachname}") for a in verfuegbare_auftraege]
        else:
            flash("Um Termine zu erstellen, leg bitte einen Auftrag an und warte, bis dieser angeommen wird!", "info")
        bestaetigte_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == current_user.id,Termin.complete == False,Termin.bestaetigt == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        offene_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == current_user.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id != current_user.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        warten_auf_antwort_termine = db.session.execute(db.select(Termin).where(Termin.pp_id == current_user.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id == current_user.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    
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
            return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= current_user)
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
                    return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= current_user)
            termin = Termin(helfer_id = auftrag.helfer.id,
                            auftrag_id = auftrag.id,
                            pp_id = auftrag.pp_id,
                            notizen = form.notizen.data, 
                            datum=form.datum.data, 
                            uhrzeit_beginn = form.uhrzeit_beginn.data, 
                            uhrzeit_ende = form.uhrzeit_ende.data,
                            ersteller_id = current_user.id                                                       
                            )
            db.session.add(termin)
            db.session.commit()
            flash("Termin wurde eingetragen.", "success")
            return redirect(url_for("termine"))
        else:
            flash("Der Termin konnte leider nicht eingetragen werden", "warning")
        return render_template("termine.html", bestaetigte = bestaetigte_termine, offene = offene_termine, wartende = warten_auf_antwort_termine, form = form, nutzer= current_user)



@app.route('/termine/<int:id>', methods=['GET', 'POST'])
@login_required
def termin(id):
    termin = db.session.get(Termin, id) 
    form = TerminBearbeiternForm(obj=termin)
    
    if current_user.rolle == "Helfer":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.helfer_id == current_user.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.pp.vorname} {a.pp.nachname} - {a.pp.adresse}") for a in verfuegbare_auftraege]

    elif current_user.rolle == "PP":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.pp_id == current_user.id)).scalars().all()
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
                termin.ersteller_id = current_user.id
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
    # Sicherheitscheck 
    if current_user.rolle != "Helfer":
          return "Zugriff verweigert. Nur Helfer können diese Seite sehen.", 403
    
    statement = db.select(Auftrag).filter_by(angenommen=False)
    
    # Füge die ergebnisse aus Statement in die Variable offene Auftrage ein
    offene_auftraege = db.session.scalars(statement).all()
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
    auftrag.angenommen = True
    # Die Id des Nutzers wird mit dem Helfer ID gleichgesetzt 
    auftrag.helfer_id = current_user.id
    db.session.commit()
    return render_template("auftrag_angenommen.html", auftrag=auftrag)


@app.route("/meine_auftraege")
@login_required
def meine_auftraege():
    # Filtert die Aufträge die angenommen wurden und die Helfer ID mit dem Nutzer ID übereinstimmt 
    statement = db.select(Auftrag).filter_by(angenommen=True, helfer_id =current_user.id)
    
    meine = db.session.scalars(statement).all()
    return render_template("meine_auftraege.html", auftraege=meine) 


@app.route("/chat_uebersicht")
@login_required
def chat_uebersicht():
    return redirect(url_for("chat"))

@app.route("/chat")
@app.route("/chat/<int:empfaenger_id>", methods=["GET", "POST"])
@login_required
def chat(empfaenger_id=None):
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

    return render_template("chat.html", chat_partner=chat_partner, aktiver_partner=aktiver_partner, nachrichten=nachrichten)

@app.route("/chat/loeschen/<int:partner_id>", methods=["POST"])
@login_required
def chat_loeschen(partner_id):
    nachrichten = Nachricht.query.filter(
        ((Nachricht.sender_id == current_user.id) & (Nachricht.empfaenger_id == partner_id)) |
        ((Nachricht.sender_id == partner_id) & (Nachricht.empfaenger_id == current_user.id))
    ).all()
    for n in nachrichten:
        if n.sender_id == current_user.id:
            n.geloescht_fuer_sender = True
        else:
            n.geloescht_fuer_empfaenger = True
    db.session.commit()
    return redirect(url_for("chat", empfaenger_id=partner_id))

if __name__ == "__main__":
    app.run(debug=True)
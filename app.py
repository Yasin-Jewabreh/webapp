from datetime import date, datetime
import os
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms import TerminBearbeitenForm, TerminErstellenForm, RollenWahlForm, RegistrierungPP, LoginFormular, AuftragFormular, ProfilFormular, RegistrierungHelfer
from flask import Flask, render_template, redirect, url_for, request, session, flash, abort, send_from_directory
from flask_bootstrap import Bootstrap5
from db import db
from models import Nutzer, Auftrag, Termin, Nachricht, berlin_time, Bewerbung
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret_key_just_for_dev_environment"
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

ROLLE_HELFER = "Helfer"
ROLLE_PP = "PP"
ROLLE_ADMIN = "Admin"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Nutzer, int(user_id))

db.init_app(app)
bootstrap = Bootstrap5(app)

with app.app_context():
            db.create_all()
            admin = db.session.execute(db.select(Nutzer).where(Nutzer.email == "admin@email.com")).scalar()
            if not admin:
                admin = Nutzer(
                    vorname=ROLLE_ADMIN,
                    nachname=ROLLE_ADMIN,
                    geschlecht="Männlich",
                    geburtsdatum=date(1995, 5, 20),
                    adresse="Hauptstraße 42",
                    plz="10115",
                    ort="Berlin",
                    email="admin@email.com",
                    freigegeben=True,
                    passwort=generate_password_hash("12345678"), 
                    telefon="015112345678",
                    rolle=ROLLE_ADMIN
                )
                db.session.add(admin)

            helfer1 = db.session.execute(db.select(Nutzer).where(Nutzer.email == "helfer1@email.com")).scalar()
            
            if not helfer1:
                helfer1 = Nutzer(
                    vorname="Max",
                    nachname=ROLLE_HELFER,
                    geschlecht="Männlich",
                    geburtsdatum=date(2001, 3, 12),
                    adresse="Müllerstraße 20",
                    plz="13353",
                    ort="Berlin",
                    email="helfer1@email.com",
                    freigegeben=True,
                    passwort=generate_password_hash("12345678"),
                    telefon="015100000001",
                    rolle=ROLLE_HELFER,
                    vorstellungstext="Hallo, ich bin Max. Ich bin zuverlässig, geduldig und helfe gerne im Alltag. Besonders gerne unterstütze ich beim Einkaufen, bei Spaziergängen oder bei kleineren Erledigungen. Ein respektvoller und freundlicher Umgang ist mir besonders wichtig.")
                db.session.add(helfer1)


            helfer2 = db.session.execute(db.select(Nutzer).where(Nutzer.email == "helfer2@email.com")).scalar()
            if not helfer2:
                helfer2 = Nutzer(
                    vorname="Lena",
                    nachname="Hilfsbereit",
                    geschlecht="Weiblich",
                    geburtsdatum=date(2000, 8, 25),
                    adresse="Turmstraße 15",
                    plz="10559",
                    ort="Berlin",
                    email="helfer2@email.com",
                    freigegeben=True,
                    passwort=generate_password_hash("12345678"),
                    telefon="015100000002",
                    rolle=ROLLE_HELFER,
                    vorstellungstext="Hallo, ich bin Lena. Ich bin eine offene und verantwortungsbewusste Person und unterstütze gerne bei Arztbesuchen, Einkäufen, Spaziergängen oder im Haushalt. Dabei sind mir Zuverlässigkeit, Geduld und Vertrauen besonders wichtig."
                )
                db.session.add(helfer2)


            pp1 = db.session.execute(db.select(Nutzer).where(Nutzer.email == "pp1@email.com")).scalar()

            if not pp1:
                pp1 = Nutzer(
                    vorname="Maria",
                    nachname="Mustermann",
                    geschlecht="Weiblich",
                    geburtsdatum=date(1948, 6, 10),
                    adresse="Alt-Moabit 80",
                    plz="10555",
                    ort="Berlin",
                    email="pp1@email.com",
                    freigegeben=True,
                    passwort=generate_password_hash("12345678"),
                    telefon="015100000003",
                    rolle = ROLLE_PP
                )
                db.session.add(pp1)


            pp2 = db.session.execute(db.select(Nutzer).where(Nutzer.email == "pp2@email.com")).scalar()
            if not pp2:
                pp2 = Nutzer(
                    vorname="Peter",
                    nachname="Beispiel",
                    geschlecht="Männlich",
                    geburtsdatum=date(1952, 11, 4),
                    adresse="Invalidenstraße 30",
                    plz="10115",
                    ort="Berlin",
                    email="pp2@email.com",
                    freigegeben=True,
                    passwort=generate_password_hash("12345678"),
                    telefon="015100000004",
                    rolle = ROLLE_PP
                )
                db.session.add(pp2)
            db.session.commit()

@app.route("/")
@app.route("/startseite")
def startseite():  
    return render_template("startseite.html")


@app.route('/rolle_auswaehlen', methods=['GET', 'POST'])
def rolle_waehlen():
       
    form = RollenWahlForm()
    if form.validate_on_submit():
        if form.helfer_btn.data:
            gewaehlte_rolle = ROLLE_HELFER
        elif form.suchender_btn.data:
            gewaehlte_rolle = ROLLE_PP
        else:
            return render_template('rolle_auswaehlen.html', form=form)
        session["rollenwahl"] = gewaehlte_rolle
        return redirect(url_for('register'))
    return render_template('rolle_auswaehlen.html', form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    gewaehlte_rolle = session.get("rollenwahl")
    if gewaehlte_rolle not in [ROLLE_HELFER, ROLLE_PP]:
        return redirect(url_for("rolle_waehlen"))
    
    helfer_form = RegistrierungHelfer()
    pp_form = RegistrierungPP()

    if gewaehlte_rolle == ROLLE_HELFER:
        if helfer_form.validate_on_submit():
            neuer_nutzer = Nutzer(
                vorname=helfer_form.vorname.data,
                nachname=helfer_form.nachname.data,
                geschlecht=helfer_form.geschlecht.data,
                geburtsdatum=helfer_form.geburtsdatum.data,
                adresse=helfer_form.adresse.data,
                plz=helfer_form.plz.data,
                ort=helfer_form.ort.data,
                email=helfer_form.email.data,
                telefon=helfer_form.telefon.data,
                passwort= generate_password_hash(helfer_form.passwort.data),
                rolle=gewaehlte_rolle,
                vorstellungstext = helfer_form.vorstellungstext.data
            )
            db.session.add(neuer_nutzer)
            db.session.flush()

            f = helfer_form.fuehrungszeugnis.data
            filename = f"{neuer_nutzer.id}_{secure_filename(f.filename)}"
            upload_ordner = os.path.join(app.static_folder,"fuehrungszeugnisse")
            os.makedirs(upload_ordner, exist_ok=True)
            f.save(os.path.join(upload_ordner, filename))
            neuer_nutzer.fuehrungszeugnis_dateiname = filename
            db.session.commit()
            session.pop("rollenwahl", None)
            return redirect(url_for("login"))

    elif gewaehlte_rolle == ROLLE_PP:
        if pp_form.validate_on_submit():
            neuer_nutzer = Nutzer(
                vorname=pp_form.vorname.data,
                nachname=pp_form.nachname.data,
                geschlecht=pp_form.geschlecht.data,
                geburtsdatum=pp_form.geburtsdatum.data,
                adresse=pp_form.adresse.data,
                plz=pp_form.plz.data,
                ort=pp_form.ort.data,
                email=pp_form.email.data,
                telefon=pp_form.telefon.data,
                passwort=generate_password_hash(pp_form.passwort.data),
                rolle=gewaehlte_rolle
            )
            db.session.add(neuer_nutzer)
            db.session.commit()
            session.pop("rollenwahl", None)
            return redirect(url_for("login"))

       
    return render_template("register.html", helfer_form =helfer_form, pp_form = pp_form, rolle = gewaehlte_rolle)

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
            if check_password_hash(nutzer.passwort, passwort):
                login_user(nutzer)
                if nutzer.rolle == ROLLE_ADMIN:
                    return redirect(url_for("nutzeruebersicht"))
                return redirect(url_for("dashboard"))
            else:
                fehler = "Passwort oder Email-Adresse falsch!"
                flash(fehler)
    return render_template("login.html", form=form, fehler=fehler)

@app.route("/dashboard")
@login_required
def dashboard():
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    return render_template("dashboard.html")

@app.route("/profil", methods=["GET", "POST"])
@login_required
def profil():
    if not current_user.freigegeben:
        return render_template("warten_auf_bestaetigung.html")

    form = ProfilFormular(obj=current_user)

    if form.validate_on_submit():
        form.populate_obj(current_user)
        db.session.commit()
        flash("Profil erfolgreich aktualisiert!", "success")
        return redirect(url_for("dashboard"))
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
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    # Verhinderung von falschen Nutzer zugriffen
    if current_user.rolle != ROLLE_PP:
        abort(403, description = "Zugriff verweigert. Nur Pflegebedürftige können diese Seite sehen.")
    
    form = AuftragFormular()
    
    vorhandener_auftrag = db.session.scalar(db.select(Auftrag).filter_by(pp_id = current_user.id))
    
    if vorhandener_auftrag:
        return redirect (url_for("auftrag_bearbeiten", auftrag_id = vorhandener_auftrag.id))
    
    # Prüfen ob ein Post ausgeführt wurde und ob alle Pflichtfelder gefüllt sind
    if form.validate_on_submit():
        # Es wird ein neuer Auftrag mit den eingegebenen Daten angelegt
        neuer_auftrag = Auftrag(
            wohnsituation=form.wohnsituation.data,
            beschreibung=form.beschreibung.data,
            pp_id=current_user.id)
        
        # Hinzufügen in die DB
        db.session.add(neuer_auftrag)
        db.session.commit()
        flash("Auftrag erfolgreich veröffentlicht!", "success")
        return redirect(url_for("dashboard"))
    return render_template("auftrag_erstellen.html", nutzer=current_user, form=form)


@app.route("/auftrag/bearbeiten/<int:auftrag_id>", methods = ["GET", "POST"])
@login_required
def auftrag_bearbeiten(auftrag_id):
    
    auftrag = db.get_or_404(Auftrag, auftrag_id)

    if auftrag.pp_id != current_user.id:
        flash("Zufriff verweigert", "danger")
        return redirect (url_for("dashboard"))
    
    form = AuftragFormular()

    if request.method == "POST" and "loeschen" in request.form:                
        db.session.delete(auftrag)
        db.session.commit()
        flash("Auftrag erfolgreich gelöscht!", "success")
        return redirect(url_for("dashboard"))
    
    # Ob ein Post gemacht wurde oder alle Felder gefüllt sind
    if form.validate_on_submit():
        auftrag.wohnsituation=form.wohnsituation.data
        auftrag.beschreibung=form.beschreibung.data
        db.session.commit()

        flash("Auftrag erfolgreich aktualisiert!", "success")
        return redirect(url_for("dashboard"))

    # Falls nichts bearbeitet wurde werden die alten daten aufgegriffen
    elif request.method == "GET":
        form.wohnsituation.data = auftrag.wohnsituation
        form.beschreibung.data = auftrag.beschreibung
        form.bestaetigung.data = True
    
    return render_template("auftrag_bearbeiten.html", form=form, nutzer=current_user, auftrag=auftrag)

@app.route("/auftrag/bewerben/<int:auftrag_id>", methods=["POST"])
@login_required
def auftrag_bewerben(auftrag_id):
    stmt = db.select(Auftrag).where(Auftrag.id == auftrag_id)
    auftrag = db.session.scalar(stmt)

    if current_user.rolle != ROLLE_HELFER:
        abort(403, description="Nur Helfer können sich bewerben.")
        
    if not auftrag:
        abort(404, description="Auftrag nicht gefunden.")
    
    if auftrag.angenommen:
        flash("Dieser Auftrag ist leider nicht mehr offen.", "danger")
        return redirect(url_for("dashboard"))
    
    stmt_check = db.select(Bewerbung).where(
        Bewerbung.auftrag_id == auftrag_id,
        Bewerbung.helfer_id == current_user.id)
    
    bereits_beworben = db.session.scalar(stmt_check)

    if bereits_beworben:
        flash("Du hast dich auf diesen Auftrag bereits beworben!", "info")
    else:
        neue_bewerbung = Bewerbung(auftrag_id=auftrag.id, helfer_id=current_user.id)
        db.session.add(neue_bewerbung)
        db.session.commit()
        flash("Deine Bewerbung wurde erfolgreich verschickt!", "success")

    return redirect(url_for("dashboard"))

@app.route("/pp/anfragen", methods=["GET", "POST"])
@login_required
def pp_anfragen():
    if current_user.rolle != ROLLE_PP:
        abort(403, description="Nur Pflegebedürftige können diese Seite sehen")
    
    if request.method == "POST":
        auftrag_id = int(request.form.get("auftrag_id"))
        aktion = request.form.get("aktion")
        
        helfer_id = request.form.get("helfer_id")   
        auftrag = db.session.get(Auftrag, auftrag_id)

        if auftrag and auftrag.pp_id == current_user.id:
            if aktion == "Annehmen" and helfer_id:
                auftrag.helfer_id = int(helfer_id)
                auftrag.angenommen = True 
                db.session.commit()
                flash("Bewerbung angenommen!", "success")
            elif aktion == "Ablehnen":
                flash("Bewerbung abgelehnt.", "info")
                
        return redirect(url_for("pp_anfragen"))
    
    anfragen = db.session.execute(
        db.select(Auftrag).where(Auftrag.pp_id == current_user.id)).scalars().all()
        
    return render_template("pp_anfragen.html", anfragen=anfragen)

@app.route("/termine/historie/")
@login_required
def historie():
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    erledigte_termine = []
    if current_user.rolle == ROLLE_HELFER:
        erledigte_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif current_user.rolle == ROLLE_PP:
        erledigte_termine =  db.session.execute(db.select(Termin).where(Termin.pp_id == current_user.id,Termin.complete == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    return render_template("historie.html", erledigte = erledigte_termine , nutzer= current_user)


@app.route("/termine/", methods = ["GET", "POST"])
@login_required
def termine():
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    
    form = TerminErstellenForm()

    verfuegbare_auftraege = []
    bestaetigte_termine = []
    offene_termine = []
    warten_auf_antwort_termine = []

    if current_user.rolle == ROLLE_HELFER:
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.helfer_id == current_user.id)).scalars().all()
        if verfuegbare_auftraege:
            form.teilnehmer.choices += [(a.id, f"{a.pp.vorname} {a.pp.nachname} - {a.pp.adresse}") for a in verfuegbare_auftraege]

        else:
            flash("Um Termine zu vereinbaren, nimm bitte erstmal einen Auftrag an!", "info")
        bestaetigte_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == False,Termin.bestaetigt == True).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        offene_termine =  db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id != current_user.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        warten_auf_antwort_termine = db.session.execute(db.select(Termin).where(Termin.helfer_id == current_user.id,Termin.complete == False,Termin.bestaetigt == False, Termin.ersteller_id == current_user.id).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif current_user.rolle == ROLLE_PP:
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.pp_id == current_user.id, Auftrag.angenommen == True)).scalars().all()
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
            if (termin.helfer_id!= current_user.id and termin.pp_id != current_user.id):
                abort(404, description = "Termin nicht gefunden")
            if termin:
                termin.complete = True
                db.session.commit()
                flash("Termin als erledigt markiert!", "success")
            return redirect(url_for("termine"))
        
        if "bestaetigen_id" in request.form:
            termin_id = int(request.form.get("bestaetigen_id"))
            termin = db.session.get(Termin,termin_id)
            if (termin.helfer_id!= current_user.id and termin.pp_id != current_user.id):
                abort(404, description = "Termin nicht gefunden")
            if termin:
                termin.bestaetigt = True
                db.session.commit()
                flash("Termin erfolgreich bestätigt!", "success")
            return redirect(url_for("termine"))
       
        if "ablehnen_id" in request.form:
            termin_id = int(request.form.get("ablehnen_id"))
            termin = db.session.get(Termin,termin_id)
            if (termin.helfer_id!= current_user.id and termin.pp_id != current_user.id):
                abort(404, description = "Termin nicht gefunden")
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
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    
    termin = db.session.get(Termin, id) 
    
    if not termin or termin.complete:
         abort(404, description = "Termin nicht gefunden")
    
    if (termin.helfer_id!= current_user.id and termin.pp_id != current_user.id):
         abort(404, description = "Termin nicht gefunden")
    
    if termin.auftrag_id is None:
        flash("Der zugehörige Auftrag wurde gelöscht. Der Termin kann nicht mehr bearbeitet werden.","warning")
        return redirect(url_for("termine"))
    
    form = TerminBearbeitenForm(obj=termin)

    if current_user.rolle == ROLLE_HELFER:
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.helfer_id == current_user.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.pp.vorname} {a.pp.nachname} - {a.pp.adresse}") for a in verfuegbare_auftraege]

    elif current_user.rolle == ROLLE_PP:
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.pp_id == current_user.id, Auftrag.angenommen == True)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.helfer.vorname} {a.helfer.nachname}") for a in verfuegbare_auftraege]

    if request.method == 'GET':
        form.teilnehmer.data = termin.auftrag_id
        return render_template('termin-bearbeiten.html', form=form)
    else:
        if form.speichern.data:
            if form.validate():
                ueberschneidung = db.session.execute(db.select(Termin).where(
                    Termin.id != id,
                    Termin.datum == form.datum.data,
                    Termin.complete == False,
                    (Termin.helfer_id == termin.helfer_id)| (Termin.pp_id == termin.pp_id),
                    Termin.uhrzeit_beginn < form.uhrzeit_ende.data,
                    Termin.uhrzeit_ende > form.uhrzeit_beginn.data)).scalars().first()

                if ueberschneidung:
                    flash("Fehler: Zu dieser Uhrzeit gibt es eine Terminüberschneidung!", "danger")
                    return redirect(url_for('termin', id=id))
                
                form.populate_obj(termin)
                termin_ende = datetime.combine(termin.datum,termin.uhrzeit_ende)
                
                if termin.bestaetigt and termin_ende< datetime.now():    
                    termin.bestaetigt= True
                else:
                    termin.bestaetigt = False
                termin.ersteller_id = current_user.id
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
        
@app.route("/meine_auftraege")
@login_required
def meine_auftraege():
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    
    # Filtert die Aufträge die angenommen wurden und die Helfer ID mit dem Nutzer ID übereinstimmt 
    statement = db.select(Auftrag).filter_by(angenommen=True, helfer_id =current_user.id)
    
    meine = db.session.scalars(statement).all()
    return render_template("meine_auftraege.html", auftraege=meine) 

@app.route("/helfer/auftraege")
@login_required
def helfer_auftraege():
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    
    # Sicherheitscheck 
    if current_user.rolle != ROLLE_HELFER:
        abort(403, description = "Nur Helfer können diese Seite sehen")

    
    statement = db.select(Auftrag).filter_by(angenommen=False)
    
    # Füge die ergebnisse aus Statement in die Variable offene Auftrage ein
    offene_auftraege = db.session.scalars(statement).all()
    heute = date.today()
    return render_template("helfer_auftraege.html", auftraege=offene_auftraege, heute=heute)

@app.route("/helfer/auftrag/<int:auftrag_id>", methods= ["POST"])
@login_required
def auftrag_annehmen(auftrag_id):
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    
    if current_user.rolle != ROLLE_HELFER:
        abort(403, description = "Nur Helfer können diese Seite sehen")
    auftrag = db.session.get(Auftrag, auftrag_id)
    if not auftrag:
        abort(404, description = "Auftrag nicht gefunden")
    if auftrag.angenommen:
        flash("Dieser Auftrag wurde bereits von einem anderen Helfer angenommen.","warning")
        return redirect(url_for("helfer_auftraege"))
    auftrag.angenommen = True
    # Die Id des Nutzers wird mit dem Helfer ID gleichgesetzt 
    auftrag.helfer_id = current_user.id
    db.session.commit()
    return render_template("auftrag_angenommen.html", auftrag=auftrag)

@app.route("/chat")
@app.route("/chat/<int:empfaenger_id>", methods=["GET", "POST"])
@login_required
def chat(empfaenger_id=None):
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    # Lade nur Nachrichten in die Kontaktliste, die für MICH NICHT gelöscht sind
    gesendete_nachrichten = db.session.execute(
        db.select(Nachricht).where(
            (Nachricht.sender_id == current_user.id) &
            (Nachricht.geloescht_fuer_sender.is_(False))
        )
    ).scalars().all()

    empfangene_nachrichten = db.session.execute(
        db.select(Nachricht).where(
            (Nachricht.empfaenger_id == current_user.id) &
            (Nachricht.geloescht_fuer_empfaenger.is_(False))
        )
    ).scalars().all()

    partner_ids = set()
    for n in gesendete_nachrichten:
        partner_ids.add(n.empfaenger_id)
    for n in empfangene_nachrichten:
        partner_ids.add(n.sender_id)

    partner_ids.discard(current_user.id)

    if partner_ids:
        chat_partner = db.session.execute(
            db.select(Nutzer).where(Nutzer.id.in_(partner_ids))
        ).scalars().all()
    else:
        chat_partner = []

    aktiver_partner = None
    nachrichten = []

    if empfaenger_id:
        aktiver_partner = db.session.get(Nutzer, empfaenger_id)

        # SICHERHEITSPRÜFUNG: Nur chatten wenn ein gemeinsamer Auftrag existiert
        gemeinsamer_auftrag = db.session.execute(
            db.select(Auftrag).where(
                (
                    (Auftrag.helfer_id == current_user.id) & (Auftrag.pp_id == empfaenger_id)
                ) | (
                    (Auftrag.pp_id == current_user.id) & (Auftrag.helfer_id == empfaenger_id)
                )
            )
        ).scalars().first()
        
        vorhandene_nachricht = db.session.scalar(
            db.select(Nachricht).where(
                (
                    (Nachricht.sender_id == current_user.id)
                    & (Nachricht.empfaenger_id == empfaenger_id)
                )
                |
                (
                    (Nachricht.sender_id == empfaenger_id)
                    & (Nachricht.empfaenger_id == current_user.id)
                )
            )
        )

        if not gemeinsamer_auftrag and not vorhandene_nachricht:
            abort(404, description="Chat nicht gefunden")

        if aktiver_partner and aktiver_partner not in chat_partner:
            chat_partner.append(aktiver_partner)

        if request.method == "POST" and request.form.get("inhalt"):
            if not gemeinsamer_auftrag:
                flash("Der Auftrag wurde gelöscht. Es können keine neuen Nachrichten mehr gesendet werden.","warning")
                return redirect(url_for("chat", empfaenger_id=empfaenger_id))
            
            neue_nachricht = Nachricht(
                inhalt=request.form["inhalt"],
                sender_id=current_user.id,
                empfaenger_id=empfaenger_id,
                zeitstempel=berlin_time()
            )
            db.session.add(neue_nachricht)
            db.session.commit()
            return redirect(url_for("chat", empfaenger_id=empfaenger_id))

        # Lade in den Chatverlauf nur Nachrichten, die ICH noch nicht gelöscht habe
        nachrichten = db.session.execute(
            db.select(Nachricht).where(
                (
                    (Nachricht.sender_id == current_user.id) &
                    (Nachricht.empfaenger_id == empfaenger_id) &
                    (Nachricht.geloescht_fuer_sender.is_(False))
                ) | (
                    (Nachricht.sender_id == empfaenger_id) &
                    (Nachricht.empfaenger_id == current_user.id) &
                    (Nachricht.geloescht_fuer_empfaenger.is_(False))
                )
            ).order_by(Nachricht.zeitstempel.asc())
        ).scalars().all()

    return render_template("chat.html", chat_partner=chat_partner, aktiver_partner=aktiver_partner, nachrichten=nachrichten)

@app.route("/chat/loeschen/<int:partner_id>", methods=["POST"])
@login_required
def chat_loeschen(partner_id):
    if current_user.freigegeben == False:
        return render_template("warten_auf_bestaetigung.html")
    nachrichten = db.session.execute(
        db.select(Nachricht).where(
            ((Nachricht.sender_id == current_user.id) & (Nachricht.empfaenger_id == partner_id)) |
            ((Nachricht.sender_id == partner_id) & (Nachricht.empfaenger_id == current_user.id))
        )
    ).scalars().all()

    for n in nachrichten:
        if n.sender_id == current_user.id:
            n.geloescht_fuer_sender = True
        else:
            n.geloescht_fuer_empfaenger = True
    db.session.commit()
    return redirect(url_for("chat"))

@app.route("/nutzeruebersicht", methods=["GET", "POST"])
@login_required
def nutzeruebersicht():
    if current_user.rolle != ROLLE_ADMIN:
        abort(404)

    nicht_freigegebene_liste = []
    nicht_freigegebene_liste = db.session.execute(db.select(Nutzer).where(Nutzer.rolle != ROLLE_ADMIN, Nutzer.freigegeben == False)).scalars().all()
    freigegebene_liste = []
    freigegebene_liste = db.session.execute(db.select(Nutzer).where(Nutzer.rolle != ROLLE_ADMIN, Nutzer.freigegeben == True)).scalars().all()
   
    if request.method == "GET":
        return(render_template("nutzer_bestaetigen.html", nicht_freigegebene = nicht_freigegebene_liste, freigegebene = freigegebene_liste))
    else:
        if "freigeben_id" in request.form:
            nutzer_id = int(request.form.get("freigeben_id"))
            nutzer = db.session.get(Nutzer,nutzer_id)
            if nutzer:
                nutzer.freigegeben = True
                db.session.commit()
                flash("Nutzer erfolgreich freigegeben!", "success")
            
        if "deaktivieren_id" in request.form:
            nutzer_id = int(request.form.get("deaktivieren_id"))
            nutzer = db.session.get(Nutzer,nutzer_id)
            if nutzer:
                nutzer.freigegeben = False
                db.session.commit()
                flash("Nutzer erfolgreich deaktiviert!", "success")
        return redirect(url_for("nutzeruebersicht"))


@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html', message = e.description), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(403)
def http_access_denied(e):
    return render_template('403.html', message = e.description), 403            

if __name__ == "__main__":
    app.run(debug=True)
from datetime import date, time, datetime
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
import forms

app = Flask(__name__)

from db import db
from models import Termin, Nutzer, Auftrag, Nachricht

app.config["SECRET_KEY"] = "secret_key_just_for_dev_environment"
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bootstrap = Bootstrap5(app)

@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/termine/", methods = ["GET", "POST"])
def termine():
    form = forms.TerminErstellenForm()
    
    aktueller_nutzer = db.session.execute(db.select(Nutzer).where(Nutzer.rolle == "Helfer")).scalars().first()

    if aktueller_nutzer.rolle == "Helfer":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.helfer_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.pp.vorname} {a.pp.nachname}") for a in verfuegbare_auftraege]

    elif aktueller_nutzer.rolle == "PP":
        verfuegbare_auftraege = db.session.execute(db.select(Auftrag).where(Auftrag.pp_id == aktueller_nutzer.id)).scalars().all()
        form.teilnehmer.choices = [(a.id, f"{a.helfer.vorname} {a.helfer.nachname}") for a in verfuegbare_auftraege]

    if aktueller_nutzer.rolle == "Helfer":
        termin_liste =  db.session.execute(db.select(Termin).where(Termin.helfer_id == aktueller_nutzer.id,Termin.complete == False).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    elif aktueller_nutzer.rolle == "PP":
         termin_liste =  db.session.execute(db.select(Termin).where(Termin.pp_id == aktueller_nutzer.id,Termin.complete == False).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()


    if request.method == "GET":
        return render_template("termine.html", termine = termin_liste, form = form, nutzer= aktueller_nutzer)
    else:
        if form.validate():

            gewaehlter_auftrag_id = int(form.teilnehmer.data)
            auftrag = db.session.get(Auftrag, gewaehlter_auftrag_id)

            ueberschneidung = db.session.execute(db.select(Termin).where(
                Termin.datum == form.datum.data,
                Termin.complete == False,
                (Termin.helfer_id == auftrag.helfer_id)| (Termin.pp_id == auftrag.pp_id),
                Termin.uhrzeit_beginn < form.uhrzeit_ende.data,
                Termin.uhrzeit_ende > form.uhrzeit_beginn.data

            )).scalars().first()

            if ueberschneidung:
                    flash("Fehler: Zu dieser Uhrzeit gibt es eine Terminüberschneidung!", "danger")
                    return render_template("termine.html", termine=termin_liste, form=form, nutzer=aktueller_nutzer)
            termin = Termin(helfer_id = auftrag.helfer.id,
                            auftrag_id = auftrag.id,
                            pp_id = auftrag.pp_id,
                            notizen = form.notizen.data, 
                            datum=form.datum.data, 
                            uhrzeit_beginn = form.uhrzeit_beginn.data, 
                            uhrzeit_ende = form.uhrzeit_ende.data                                                          
                            )
            db.session.add(termin)
            db.session.commit()
            flash("Termin wurde eingetragen.", "success")
        else:
            flash("Ups, hat nicht geklappt", "warning")
        return render_template("termine.html", termine=termin_liste, form=form, nutzer=aktueller_nutzer)



if __name__ == "__main__":
    app.run(debug=True)
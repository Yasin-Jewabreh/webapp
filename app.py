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

with app.app_context():
    db.session.execute(db.delete(Nutzer))
    db.session.execute(db.delete(Auftrag))
    db.session.execute(db.delete(Nachricht))
    db.session.execute(db.delete(Termin))

    helfer1= Nutzer(vorname = "Yasin", nachname = "Jason", 
                    geschlecht = "M", geburtsdatum = datetime.strptime("27.12.2008", "%d.%m.%Y").date(),
                     adresse = "Bischofshasener Straße 102", plz ="235453",
                      ort = "Berlin", email ="y.yasin@web.de",
                       passwort = "12345", rolle = "Helfer")
    
    helfer2= Nutzer(vorname = "Ahmad", nachname = "Patron", 
                    geschlecht = "M", geburtsdatum = datetime.strptime("25.08.2004", "%d.%m.%Y").date(),
                     adresse = "Badensche Straße 8", plz ="10557",
                      ort = "Berlin", email ="a.patron@gmail.com",
                       passwort = "11111", rolle = "Helfer")
    
    pp1= Nutzer(vorname = "Alexander", nachname = "Eck", 
                    geschlecht = "M", geburtsdatum = datetime.strptime("15.03.1986", "%d.%m.%Y").date(),
                     adresse = "Heidestraße 5", plz ="12395",
                      ort = "Berlin", email ="a.eck@gmail.com",
                       passwort = "22222", rolle = "PP")
    
    pp2= Nutzer(vorname = "Mohamed", nachname = "Aoun", 
                    geschlecht = "M", geburtsdatum = datetime.strptime("30.03.1999", "%d.%m.%Y").date(),
                     adresse = "Irgendwo in Libanon", plz ="19999",
                      ort = "Berlin", email ="m.aoun@gmail.com",
                       passwort = "33333", rolle = "PP")
    
    db.session.add_all([helfer1, helfer2, pp1, pp2])
    db.session.commit()
    
    auftrag1 = Auftrag(wohnsituation = "Alleinstehend", 
                       beschreibung = "Spende bittööö",
                       angenommen = True, helfer_id = helfer1.id, pp_id = pp1.id)
    
    db.session.add_all([auftrag1])
    db.session.commit()
    
    termin1 = Termin(helfer_id = helfer1.id, auftrag_id = auftrag1.id, 
                     pp_id = pp1.id, notizen = "Bring bitte Geld mit", 
                     datum = datetime.strptime("23.06.2026", "%d.%m.%Y").date(),   
                     uhrzeit_beginn = datetime.strptime("12:30", "%H:%M").time(),         
                     uhrzeit_ende = datetime.strptime("14:30", "%H:%M").time(), complete = False)
    
    db.session.add_all( [termin1])
    db.session.commit()



@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/termine/", methods = ["GET", "POST"])
def termine():
    form = forms.TerminErstellenForm()
    if request.method == "GET":
        termin_liste=  db.session.execute(db.select(Termin).where(Termin.complete == False).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
        return render_template("termine.html", termine = termin_liste, form = form)
    else:
        if form.validate():
            termin = Termin(helfer_id = helfer1.id,
                            auftrag_id = auftrag1.id,
                            pp_id = pp1.id, 
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
        return redirect (url_for("termine"))



if __name__ == "__main__":
    app.run(debug=True)
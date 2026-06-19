from db import db
from datetime import date, time
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from models import Termin, Nutzer, Auftrag, Nachricht
import forms

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret_key_just_for_dev_environment"
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "pulse"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()
    if not Nutzer.query.first():
        # 1. Einen Test-Nutzer (Helfer/Hilfesuchender) anlegen
        test_nutzer = Nutzer(
            vorname="Max", nachname="Mustermann", geschlecht="Männlich",
            geburtsdatum=date(1990, 1, 1), adresse="Musterstraße 1",
            plz="12345", ort="Musterstadt", email="max@example.com",
            passwort="geheimspasswort", rolle="Helfer"
        )
        db.session.add(test_nutzer)
        db.session.commit() # Speichern, um die ID für die ForeignKeys zu generieren
        
        # 2. Einen Test-Auftrag anlegen
        test_auftrag = Auftrag(
            wohnsituation="Einfamilienhaus",
            beschreibung="Rasen mähen im Vorgarten",
            angenommen = False,
            nutzer_id=test_nutzer.id
        )
        db.session.add(test_auftrag)
        db.session.commit()
        
        # 3. Zwei Test-Termine anlegen (einen offenen, einen erledigten)
        termin1 = Termin(
            helfer_id=test_nutzer.id, pp_id=test_nutzer.id, auftrag_id=test_auftrag.id, notizen="Rasenmäher steht im Schuppen",
            datum=date(2026, 7, 20), uhrzeit_beginn=time(14, 0), uhrzeit_ende=time(16, 0),
            complete=False
        )
        termin2 = Termin(
            helfer_id=test_nutzer.id, pp_id=test_nutzer.id, auftrag_id=test_auftrag.id,
            notizen="Einkaufszettel liegt auf dem Küchentisch",
            datum=date(2026, 6, 15), uhrzeit_beginn=time(10, 0), uhrzeit_ende=time(11, 30),
            complete=False
        )
        termin3 = Termin(
            helfer_id=test_nutzer.id, pp_id=test_nutzer.id, auftrag_id=test_auftrag.id, notizen="Einkaufszettel liegt auf dem Küchentisch",
            datum=date(2026, 6, 15), uhrzeit_beginn=time(12, 0), uhrzeit_ende=time(13, 30),
            complete=False
        )

        db.session.add_all([termin1, termin2, termin3])
        db.session.commit()
        print("🎉 Testdaten erfolgreich angelegt!")

@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/termine/", methods = ["GET", "POST"])
def termine():
    termin_liste=  db.session.execute(db.select(Termin).where(Termin.complete == False).order_by(Termin.datum, Termin.uhrzeit_beginn)).scalars().all()
    
    form = forms.TerminErstellenForm()

    if form.validate_on_submit():
        neuer_termin = Termin(
            datum = form.datum.data,
            uhrzeit_beginn = form.uhrzeit_beginn.data,
            uhrzeit_ende = form.uhrzeit_ende.data,
            notizen = form.notizen.data,
            complete = False,
            auftrag_id = 1,
            pp_id = 1,
            helfer_id = 1
        )
        db.session.add(neuer_termin)
        db.session.commit()
        return redirect (url_for("termine"))
    return render_template("termine.html",termine = termin_liste, form = form)



if __name__ == "__main__":
    app.run(debug=True)
import os 
from datetime import date, datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from models import db, Nutzer, Auftrag, Termin  # Termin mitimportiert

app = Flask(__name__)
bootstrap = Bootstrap5(app)

os.makedirs(app.instance_path, exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pflegehilfe.db"
db.init_app(app)


@app.route("/")
def startseite():
    return "Die Startseite funktioniert"


@app.route("/auftrag/erstellen", methods=["GET", "POST"])
def auftrag_erstellen():
    
    aktueller_nutzer = Nutzer.query.get(3)

    print("Gefundener Nutzer:", aktueller_nutzer)
    if aktueller_nutzer:
        print("Vorname:", aktueller_nutzer.vorname)
        print("Adresse:", aktueller_nutzer.adresse)

    if request.method == "POST":
        neuer_auftrag = Auftrag(
            wohnsituation=request.form["wohnsituation"],
            beschreibung=request.form["beschreibung"],
            nutzer_id=aktueller_nutzer.id if aktueller_nutzer else 3
        )

        db.session.add(neuer_auftrag)
        db.session.commit()
        return redirect(url_for("startseite")) 
    
    return render_template("auftrag_erstellen.html", nutzer=aktueller_nutzer)



if __name__ == "__main__":
    with app.app_context():
        
        db.create_all()
        
        
        if Nutzer.query.first() is None:
            
            helfer1 = Nutzer(vorname="Yasin", nachname="Jason", geschlecht="M", 
                             geburtsdatum=datetime.strptime("27.12.2008", "%d.%m.%Y").date(),
                             adresse="Bischofshasener Straße 102", plz="235453", ort="Berlin", 
                             email="y.yasin@web.de", telefon="0151111111", passwort="12345", rolle="Helfer")
        
            helfer2 = Nutzer(vorname="Ahmad", nachname="Patron", geschlecht="M", 
                             geburtsdatum=datetime.strptime("25.08.2004", "%d.%m.%Y").date(),
                             adresse="Badensche Straße 8", plz="10557", ort="Berlin", 
                             email="a.patron@gmail.com", telefon="0151222222", passwort="11111", rolle="Helfer")
                
            pp1 = Nutzer(vorname="Alexander", nachname="Eck", geschlecht="M", 
                         geburtsdatum=datetime.strptime("15.03.1986", "%d.%m.%Y").date(),
                         adresse="Heidestraße 5", plz="12395", ort="Berlin", 
                         email="a.eck@gmail.com", telefon="0151333333", passwort="22222", rolle="PP")
                
            pp2 = Nutzer(vorname="Mohamed", nachname="Aoun", geschlecht="M", 
                         geburtsdatum=datetime.strptime("30.03.1999", "%d.%m.%Y").date(),
                         adresse="Irgendwo in Libanon", plz="19999", ort="Berlin", 
                         email="m.aoun@gmail.com", telefon="0151444444", passwort="33333", rolle="PP")
            
            db.session.add_all([helfer1, helfer2, pp1, pp2])
            db.session.commit()
                
           
            auftrag1 = Auftrag(wohnsituation="Alleinstehend", beschreibung="Spende bittööö",
                               angenommen="offen", nutzer_id=pp1.id)
                
            db.session.add(auftrag1)
            db.session.commit()
                
        
            print("Testdaten erfolgreich hinzugefügt!")
        else:
            print("Datenbank enthält bereits Daten. Testdaten-Generierung übersprungen.")


    app.run(debug=True)
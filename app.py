import os 
from datetime import date, datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from models import db, Nutzer, Auftrag, Termin  # Termin mitimportiert
from forms import AuftragFormular
from flask_login import LoginManager, login_user, logout_user, login_required, current_user



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
    return Nutzer.query.get(int(user_id))

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
            return redirect(url_for("auftrag_erstellen"))

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("startseite"))

@app.route("/auftrag/erstellen", methods=["GET", "POST"])
def auftrag_erstellen():
    
    aktueller_nutzer = Nutzer.query.get(3)

    form = AuftragFormular()

    
    if form.validate_on_submit():
        neuer_auftrag = Auftrag(
            wohnsituation=form.wohnsituation.data,  
            beschreibung=form.beschreibung.data,
            nutzer_id=aktueller_nutzer.id if aktueller_nutzer else 3
        )

        db.session.add(neuer_auftrag)
        db.session.commit()


        return redirect(url_for("startseite")) 
    


    return render_template("auftrag_erstellen.html", nutzer=aktueller_nutzer, form =form)

@app.route("/helfer/auftraege")
def helfer_auftraege():
    
    offene_auftraege = Auftrag.query.filter_by(angenommen="offen").all()

    heute = date.today()

    return render_template(
        "helfer_auftraege.html",
        auftraege=offene_auftraege,
        heute=heute
    )

@app.route("/helfer/auftrag/<int:auftrag_id>")
def auftrag_annehmen(auftrag_id):
    
    auftrag = Auftrag.query.get_or_404(auftrag_id)
    
  
    auftrag.angenommen = "angenommen"
    db.session.commit()
    
    return render_template("auftrag_angenommen.html", auftrag=auftrag)


if __name__ == "__main__":
    with app.app_context():
        
        db.create_all()
        
        
        if Nutzer.query.get(3) is None:
            
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
                
           
           # auftrag1 = Auftrag(wohnsituation="Alleinstehend", beschreibung="Spende bittööö",
            #                   angenommen="offen", nutzer_id=pp1.id)
                
            #db.session.add(auftrag1)
            #db.session.commit()
                
        
            print("Testdaten erfolgreich hinzugefügt!")
        else:
            print("Datenbank enthält bereits Daten. Testdaten-Generierung übersprungen.")


    app.run(debug=True)
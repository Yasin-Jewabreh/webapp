from db import db
from models import Pflegebeduerftiger
from flask import Flask, render_template, redirect, url_for, request
import os 
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)

os.makedirs(app.instance_path, exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pflegehilfe.db"

db.init_app(app)

#@app.route("/helfer/auftraege")


@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/pflegeprofil/erstellen", methods=["GET", "POST"])
def pflegeprofil_erstellen():
    if request.method == "POST":
        neues_profil = Pflegebeduerftiger(
            name=request.form["name"],
            alter=int(request.form["alter"]),
            geschlecht=request.form["geschlecht"],
            wohnsituation=request.form["wohnsituation"],
            beschreibung=request.form["beschreibung"]
        )

        db.session.add(neues_profil)
        db.session.commit()

        return redirect(
            url_for(
                "pflegeprofil_anzeigen",
                profil_id=neues_profil.id
            )
        )

    return render_template("auftrag_erstellen.html")


@app.route("/pflegeprofil/<int:profil_id>")
def pflegeprofil_anzeigen(profil_id):
    profil = db.get_or_404(Pflegebeduerftiger, profil_id)

    return render_template(
        "pflegeprofil_anzeigen.html",
        profil=profil
    )




''''
@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/db-test")
def db_test():
    db_con = database.get_db_con()
    result =db_con.execute("Select 1").fetchone() #ohne fetchone würde es nur drauf zeigen: <sqlite3.Cursor object at 0x...>

    return f"Datenbank funktioniert: {result[0]}"

@app.route("Kalender")
def kalender():
    return render_template("calendar.html")
'''
if __name__ == "__main__":
   with app.app_context():
       db.create_all()

       app.run(debug =True)
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

@app.route("/auftraege")
@login_required
def auftraege_start():
   
   
   
   
   
   ''''
    if current_user.rolle == "PP":
        return redirect (url_for("auftrag_erstellen"))

    if current_user.rolle == "Helfer":
        return redirect (url_for("helfer_auftraege"))

    return "Unbekante Benutzerrolle", 403

    '''
@app.route("/auftrag/erstellen", methods =["GET", "POST"])
@login_required
def auftrag_erstellen():
    if request.method == "POST":
        neuer_auftrag = auftrag(
            wohnsituation = request.form["wohnsituation"],
            beschreibung = request.form["beschreibung"],
            status = "offen",
            nutzer_id = current_user.id
        )

        db.session.add(neuer_auftrag)
        db.session.commit()

        return redirect(url_for("auftraege_start"))
    
    return render_template(
        "auftrag_erstellen.html",
        nutzer = current_user
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
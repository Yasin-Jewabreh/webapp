from db import db
from flask import Flask, render_template, redirect, url_for, request
import models

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpyourneighbour.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
@login_required
def auftraege_start():
    if current_user.rolle == "PP":
        return redirect (url_for("auftrag_erstellen"))

    if current_user.rolle == "Helfer":
        return redirect (url_for("helfer_auftraege"))

    return "Unbekante Benutzerrolle", 403

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


@app.route("/termine")
def kalender():
    return render_template("termine.html")

if __name__ == "__main__":
    app.run(debug=True)
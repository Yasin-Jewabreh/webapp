import db
from flask import Flask, render_template, redirect, url_for, request
import os 

app = Flask(__name__)

os.makedirs(app.instance_path, exist_ok=True)

app.config.from_mapping(
    DATABASE = os.path.join(app.instance_path, "Pflegehilfe.db")
    )

app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)

@app.route("/")
def startseite():
    return "Die Startseite funktioniert"

@app.route("/auftraege")
def auftraege():
    return "Auftragsübersicht funktioniert"

@app.route("/db-test")
def db_test():
    db_con = db.get_db_con()
    result =db_con.execute("Select 1").fetchone() #ohne fetchone würde es nur drauf zeigen: <sqlite3.Cursor object at 0x...>

    return f"Datenbank funktioniert: {result[0]}"

@app.route("/kalender")
def kalender():
    return render_template("calendar.html")

if __name__ == "__main__":
    app.run(debug=True)
from db import db

class Auftrag(db.Model):
    __tablename__ = "auftraege"

    id = db.Column(db.Integer, primary_key = true)
    name = db.Column(db.String(100), nullable = false)
    alter = db.Column(db.Integer, nullable = false)
    geschlecht = db.Column(db.String(50), nullable = false)
    wohnsituation = db.Column(db.String(100), nullable = false)
    beschreibung = db.Column(db.String(200), nullable = false)
    #Datum? Hilfeart?

    
    
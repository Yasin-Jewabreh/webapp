from db import db

class Pflegebeduerftiger(db.Model):
    __tablename__ = "pflegebeduerftige"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    alter = db.Column(db.Integer, nullable = False)
    geschlecht = db.Column(db.String(50), nullable = False)
    wohnsituation = db.Column(db.String(100), nullable = False)
    beschreibung = db.Column(db.String(200), nullable = False)


    status = db.Column(db.String(50), default = "offen", nullable = "False")
    #Datum? Hilfeart?
    
    


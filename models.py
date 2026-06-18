from db import db

class nutzer(db.Model):
    _tablename_ = "nutzer"
    id = db.Column(db.Integer, primary_key = True, index = True)
    vorname = db.Column(db.String(50), nullable = False)
    nachname = db.Column(db.String(50), nullable = False)
    geschlecht = db.Column(db.String(50), nullable = False)
    geburtsdatum = db.Column(db.Date(), nullable = False)
    adresse = db.Column(db.String(100), nullable = False)
    plz = db.Column(db.String(10), nullable = False)
    ort = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(), nullable = False, unique = True)
    passwort = db.Column(db.String(), nullable = False)
    rolle = db.Column(db.String(), nullable = False, index = True)
    



class auftrag(db.Model):
    __tablename__ = "auftrag"
    id = db.Column(db.Integer, primary_key = True, index = True)
    wohnsituation = db.Column(db.String(100), nullable = False)
    beschreibung = db.Column(db.String(200), nullable = False)
    status = db.Column(db.String(50), default = "offen", nullable = "False")
    db.Column('nutzer_id', db.ForeignKey('nutzer.id'), primary_key=True)
    


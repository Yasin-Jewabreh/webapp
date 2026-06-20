from db import db

class Nutzer(db.Model):
    __tablename__ = "nutzer"

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

class Auftrag(db.Model):
    __tablename__ = "auftrag"

    id = db.Column(db.Integer, primary_key = True, index = True)
    wohnsituation = db.Column(db.String(100), nullable = False)
    beschreibung = db.Column(db.String(500), nullable = False)
    angenommen = db.Column(db.Boolean, default = False, nullable = False)
    helfer_id = db.Column("helfer_id", db.ForeignKey("nutzer.id"), nullable = True)
    pp_id = db.Column("pp_id", db.ForeignKey("nutzer.id"), nullable = False)

    pp = db.relationship("Nutzer", foreign_keys=[pp_id], backref="erstellte_auftraege")
    helfer = db.relationship("Nutzer", foreign_keys=[helfer_id], backref="angenommene_auftraege")
    
class Nachricht (db.Model):
    __tablename__ = "nachricht"

    id = db.Column(db.Integer, primary_key = True)
    inhalt = db.Column(db.String(500), nullable=False)
    zeitstempel = db.Column(db.DateTime, default=db.func.now())
    sender_id=db.Column("sender_id", db.ForeignKey("nutzer.id"), nullable = False)
    empfaenger_id= db.Column('empfaenger_id', db.ForeignKey("nutzer.id"), nullable = False)
 
class Termin (db.Model):
    __tablename__ = "termin"

    id = db.Column(db.Integer, primary_key = True, index = True)
    helfer_id = db.Column("helfer_id", db.ForeignKey("nutzer.id"), nullable = False)
    auftrag_id = db.Column("auftrag_id", db.ForeignKey("auftrag.id"), nullable = False)
    pp_id = db.Column("pp_id", db.ForeignKey("nutzer.id"), nullable = False)
    notizen = db.Column(db.String(200), nullable = True)
    datum = db.Column(db.Date, nullable = False)
    uhrzeit_beginn = db.Column(db.Time, nullable = False)
    uhrzeit_ende = db.Column(db.Time, nullable = False)
    complete = db.Column(db.Boolean, default = False, nullable = False)
    bestaetigt = db.Column(db.Boolean, default = False, nullable = False)
    ersteller_id = db.Column(db.Integer, nullable = False, index = True)
    helfer = db.relationship("Nutzer", foreign_keys=[helfer_id], backref="helfer_termine")
    pp = db.relationship("Nutzer", foreign_keys=[pp_id], backref="pp_termine")
    auftrag = db.relationship("Auftrag", backref="termine")

    




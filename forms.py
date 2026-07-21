from datetime import date
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField, BooleanField, DateField, TimeField, HiddenField, TextAreaField, EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, InputRequired, Optional, Regexp, ValidationError, Email, EqualTo
from datetime import date, datetime
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_login import current_user

from db import db
from models import Nutzer

class RollenWahlForm(FlaskForm):
    helfer_btn = SubmitField('Hilfe anbieten')
    suchender_btn = SubmitField('Hilfe suchen')

def validate_email(self, field):
        field.data = field.data.strip().lower()
        if current_user.id:
            vorhandener_nutzer = db.session.scalar(db.select(Nutzer).where(Nutzer.email == field.data,Nutzer.id != current_user.id))
        else:
            vorhandener_nutzer = db.session.scalar(db.select(Nutzer).where(Nutzer.email == field.data))
        if vorhandener_nutzer:
            raise ValidationError("Diese E-Mail-Adresse wird bereits verwendet.")

def validate_telefon(self, field):
        field.data = field.data.strip().lower()
        if current_user.id:
            vorhandener_nutzer = db.session.scalar(db.select(Nutzer).where(Nutzer.telefon == field.data,Nutzer.id != current_user.id))
        else:
            vorhandener_nutzer = db.session.scalar(db.select(Nutzer).where(Nutzer.telefon == field.data))
        if vorhandener_nutzer:
            raise ValidationError("Diese Telefonnummer ist bereits vergeben.")
       
def check_geburtsdatum(self, field):
    if field.data: 
        if ((date.today() - field.data).days / 365.25) < 18:
            raise ValidationError("Du musst mindestens 18 Jahre alt sein.")
        
def strip_text(value):
    if value:
        return value.strip()
    return value
        
class RegistrierungFormular(FlaskForm):
    vorname = StringField("Vorname:", validators=[InputRequired()], filters=[strip_text])
    nachname = StringField("Nachname:", validators=[InputRequired()], filters=[strip_text])
    geschlecht = SelectField("Geschlecht:", validators=[DataRequired()],choices = [("","--Bitte wählen--"), ("M", "Männlich"), ("W","Weiblich"), ("D", "Divers")])
    geburtsdatum = DateField("Geburtsdatum",validators=[InputRequired(), check_geburtsdatum], format='%Y-%m-%d')
    adresse = StringField("Adresse:", validators=[InputRequired()], filters=[strip_text])
    plz = StringField("Postleitzahl:", validators=[InputRequired(), Regexp(r"^\d{5}$",message="Die PLZ muss aus genau 5 Ziffern bestehen.")],filters=[strip_text])
    ort = SelectField("Ort:", validators=[InputRequired()], choices = [("","--Bitte wählen--"), ("Berlin", "Berlin")])
    email = EmailField("Email:", validators=[InputRequired(), validate_email, Email(message="Bitte gib eine gültige E-Mail-Adresse ein.")], filters=[strip_text])
    passwort = PasswordField("Passwort:", validators=[InputRequired(), Length(min=8, message = "Das Passwort muss mindestens 8 Zeichen lang sein!")])
    passwort_wiederholen = PasswordField("Passwort wiederholen:", validators=[InputRequired(), EqualTo("passwort", message = "Die Passwörter müssen übereinstimmen!")])
    telefon = StringField('Telefonnummer', validators=[validate_telefon,Regexp(r"^\d+$", message="Die Telefonnummer darf nur aus Ziffern bestehen."),Length(min=7,max=15,message="Die Telefonnummer muss zwischen 7 und 15 Ziffern lang sein."), DataRequired(message="Bitte Telefonnummer eingeben.")], filters=[strip_text])
    
class RegistrierungPP(RegistrierungFormular):
    registrieren = SubmitField("Registrieren")

class RegistrierungHelfer(RegistrierungFormular):  
    fuehrungszeugnis = FileField("Führungszeugnis", validators=[FileRequired(), FileAllowed(['pdf'], "Bitte lade eine PDF Datei hoch!")])
    vorstellungstext = TextAreaField("Über mich", validators=[DataRequired(message="Bitte erzähle etwas über dich. Dieser Text wird angezeigt, wenn du dich für einen Auftrag bewirbst."),
                                                              Length(max=500, message="Die Beschreibung darf maximal 500 Zeichen lang sein.")])
    registrieren = SubmitField("Registrieren")




class LoginFormular(FlaskForm):
    email = EmailField("Email:", validators=[InputRequired()], filters=[strip_text])
    passwort = PasswordField("Passwort:", validators=[InputRequired()])
    login = SubmitField("Login")

class AuftragFormular(FlaskForm):
    wohnsituation = SelectField(
        "Wohnsituation",
        choices=[
            ("","Bitte auswählen"),
            ("allein", "Ich lebe allein"),
            ("partner/in", "Ich lebe mit meinem Partner oder meiner Partnerin"),
            ("familie", "Ich lebe mit meiner Familie"),
            ("wohngemeinschaft", "Ich lebe in einer Wohngemeinschaft"),
            ("pflegeeinrichtung", "Ich lebe in einer Pflegeeinrichtung"),
            ("andere Wohnsituation", "Andere Wohnsituation")
        ],validators=[DataRequired(message="Bitte wähle deine Wohnsituation aus.")])

    beschreibung = TextAreaField(
        "Über mich",
        validators=[
            DataRequired(message="Bitte erzähle etwas über dich."),
            Length(max=500, message="Die Beschreibung darf maximal 500 Zeichen lang sein.")])
    
    bestaetigung = BooleanField(
        "Ich bestätige, dass die angegebenen Informationen gespeichert und sichtbar sein dürfen.",
        validators=[DataRequired(message="Du musst der Bestätigung zustimmen.")])
    
    submit = SubmitField("Auftrag veröffentlichen")

def check_datum(self, field):
    if field.data:
        if field.data < date.today():
            raise ValidationError(f"Der Termin darf nicht in der Vergangenheit liegen!")

def check_endzeit(self, field):
    if self.uhrzeit_beginn.data and field.data:
        if field.data <= self.uhrzeit_beginn.data:
            raise ValidationError("Die End-Uhrzeit muss nach der Start-Uhrzeit liegen!")
        
def check_startzeit(self, field):
    if self.datum.data and field.data:
        if self.datum.data == date.today() and field.data < datetime.now().time():
            raise ValidationError("Der Termin darf nicht in der Vergangenheit liegen!")

def check_person(self,field):
    if field.data == 0:
        raise ValidationError("Bitte eine Person auswählen!")
          
class TerminErstellenForm(FlaskForm):
    teilnehmer = SelectField("Der Termin ist mit:", coerce=int, choices=[(0, "---Bitte wählen---")],validators=[InputRequired(),check_person])
    datum = DateField("Am",validators=[InputRequired(), check_datum], format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von",validators=[InputRequired(), check_startzeit],format='%H:%M')
    uhrzeit_ende = TimeField("Bis",validators=[InputRequired(), check_endzeit], format='%H:%M')
    notizen = TextAreaField("Trage hier deine Notizen ein",validators=[Optional(),Length(max=200, message= "Die Notiz darf nicht länger als 200 Zeichen sein")],render_kw={"placeholder": "(optional)"})
    eintragen = SubmitField("Termin eintragen")

class TerminBearbeitenForm(FlaskForm):
    teilnehmer = SelectField("Der Termin ist mit:", coerce=int,validate_choice=False, render_kw={"disabled": True})
    datum = DateField("Am",validators=[InputRequired(), check_datum], format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von",validators=[InputRequired()],format='%H:%M')
    uhrzeit_ende = TimeField("Bis",validators=[InputRequired(), check_endzeit], format='%H:%M')
    notizen = TextAreaField("Trage hier deine Notizen ein",validators=[Optional(),Length(max=200, message= "Die Notiz darf nicht länger als 200 Zeichen sein")])
    speichern = SubmitField("Änderungen Speichern")
    entfernen = SubmitField("Termin löschen", render_kw = {"class": "btn btn-outline-danger"})
    zurueck = SubmitField("Zurück", render_kw={"class": "btn btn-info"})

def validate_vorstellungstext(self, field):
        if current_user.rolle == "Helfer" and not field.data.strip():
            raise ValidationError("Dieses Feld darf nicht leer bleiben")
        
class ProfilFormular(FlaskForm):
    vorname = StringField('Vorname', validators=[DataRequired(message="Bitte Vornamen eingeben.")], filters=[strip_text])
    nachname = StringField('Nachname', validators=[DataRequired(message="Bitte Nachnamen eingeben.")], filters=[strip_text])
    email = EmailField("Email:", validators=[InputRequired(),validate_email, Email(message="Bitte gib eine gültige E-Mail-Adresse ein.")],filters=[strip_text])
    telefon = StringField('Telefonnummer', validators=[validate_telefon,Regexp(r"^\d+$", message="Die Telefonnummer darf nur aus Ziffern bestehen."),Length(min=7,max=15,message="Die Telefonnummer muss zwischen 7 und 15 Ziffern lang sein."), DataRequired(message="Bitte Telefonnummer eingeben.")], filters=[strip_text])
    adresse = StringField('Adresse', validators=[DataRequired(message="Bitte Adresse eingeben.")], filters=[strip_text])
    plz = StringField("Postleitzahl:", validators=[InputRequired(), Regexp(r"^\d{5}$",message="Die PLZ muss aus genau 5 Ziffern bestehen.")],filters=[strip_text])
    vorstellungstext = TextAreaField("Über mich", validators=[validate_vorstellungstext, Length(max=500, message="Die Beschreibung darf maximal 500 Zeichen lang sein.")])
    submit = SubmitField('Änderungen speichern')

from datetime import date
from flask_wtf import FlaskForm
from wtforms import SelectField, TextAreaField, SubmitField, BooleanField, DateField, TimeField, HiddenField, TextAreaField, EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length, InputRequired, Optional, ValidationError, Email, EqualTo
from datetime import date


class RollenWahlForm(FlaskForm):
    helfer_btn = SubmitField('Hilfe anbieten')
    suchender_btn = SubmitField('Hilfe suchen')

def check_geburtsdatum(self, field):
    if field.data: 
        if ((date.today() - field.data).days / 365.25) < 18:
            raise ValidationError("Du musst mindestens 18 Jahre alt sein.")
        
class RegistrierungFormular(FlaskForm):
    vorname = StringField("Vorname:", validators=[InputRequired()])
    nachname = StringField("Nachname:", validators=[InputRequired()])
    geschlecht = SelectField("Geschlecht:", validators=[DataRequired()],choices = [("","--Bitte wählen--"), ("M", "Männlich"), ("W","Weiblich"), ("D", "Divers")])
    geburtsdatum = DateField("Geburtsdatum",validators=[InputRequired(), check_geburtsdatum], format='%Y-%m-%d')
    adresse = StringField("Adresse:", validators=[InputRequired()])
    plz = StringField("Postleitzahl:", validators=[InputRequired()])
    ort = SelectField("Ort:", validators=[InputRequired()], choices = [("","--Bitte wählen--"), ("B", "Berlin")])
    email = EmailField("Email:", validators=[InputRequired()])
    passwort = PasswordField("Passwort:", validators=[InputRequired(), Length(min=8, message = "Das Passwort muss mindestens 8 Zeichen lang sein!")])
    passwort_wiederholen = PasswordField("Passwort wiederholen:", validators=[InputRequired(), EqualTo("passwort", message = "Die Passwörter müssen übereinstimmen!")])
    telefon = StringField("Telefon:", validators=[InputRequired()])
    registrieren = SubmitField("Registrieren")

class LoginFormular(FlaskForm):
    email = EmailField("Email:", validators=[InputRequired()])
    passwort = PasswordField("Passwort:", validators=[InputRequired()])
    login = SubmitField("Login")

class AuftragFormular(FlaskForm):
    wohnsituation = SelectField(
        "Wohnsituation",
        choices=[
            ("", "Bitte auswählen"),
            ("Ich lebe allein", "Ich lebe allein"),
            ("Ich lebe mit meinem Partner oder meiner Partnerin", "Ich lebe mit meinem Partner oder meiner Partnerin"),
            ("Ich lebe mit meiner Familie", "Ich lebe mit meiner Familie"),
            ("Ich lebe in einer Wohngemeinschaft", "Ich lebe in einer Wohngemeinschaft"),
            ("Ich lebe in einer Pflegeeinrichtung", "Ich lebe in einer Pflegeeinrichtung"),
            ("Andere Wohnsituation", "Andere Wohnsituation")
        ],
        validators=[DataRequired(message="Bitte wähle deine Wohnsituation aus.")]
    )

    beschreibung = TextAreaField(
        "Über mich",
        validators=[
            DataRequired(message="Bitte erzähle etwas über dich."),
            Length(max=500, message="Die Beschreibung darf maximal 500 Zeichen lang sein.")
        ]
    )
    
    bestaetigung = BooleanField(
        "Ich bestätige, dass die angegebenen Informationen sichtbar sein dürfen.",
        validators=[DataRequired(message="Du musst der Bestätigung zustimmen.")]
    )
    
    submit = SubmitField("Auftrag veröffentlichen")

def check_datum(self, field):
    if field.data:
        if field.data.year < date.today().year or  field.data.year > date.today().year +1 :
            raise ValidationError(f"Das Datum muss im Jahr {date.today().year} oder {date.today().year +1} liegen!")

def check_uhrzeit(self, field):
    if self.uhrzeit_beginn.data and field.data:
        if field.data <= self.uhrzeit_beginn.data:
            raise ValidationError("Die End-Uhrzeit muss nach der Start-Uhrzeit liegen!")

def check_person(self,field):
    if self.teilnehmer.data == 0:
        raise ValidationError("Bitte eine Person auswählen!")
          
class TerminErstellenForm(FlaskForm):
    teilnehmer = SelectField("Der Termin ist mit:", coerce=int, validators=[InputRequired(),check_person])
    datum = DateField("Am",validators=[InputRequired(), check_datum], format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von",validators=[InputRequired()],format='%H:%M')
    uhrzeit_ende = TimeField("Bis",validators=[InputRequired(), check_uhrzeit], format='%H:%M')
    notizen = TextAreaField("Trage hier deine Notizen ein",render_kw={"placeholder": "(optional)"})
    eintragen = SubmitField("Termin eintragen")

class TerminBearbeiternForm(FlaskForm):
    id = HiddenField()
    teilnehmer = SelectField("Der Termin ist mit:", coerce=int, validators=[InputRequired()])
    datum = DateField("Am",validators=[InputRequired(), check_datum], format='%Y-%m-%d')
    uhrzeit_beginn = TimeField("Von",validators=[InputRequired()],format='%H:%M')
    uhrzeit_ende = TimeField("Bis",validators=[InputRequired(), check_uhrzeit], format='%H:%M')
    notizen = TextAreaField("Trage hier deine Notizen ein",validators=[Optional()])
    speichern = SubmitField("Änderungen Speichern")
    entfernen = SubmitField("Termin löschen", render_kw = {"class": "btn btn-outline-danger"})
    zurueck = SubmitField("Zurück", render_kw={"class": "btn btn-info"})

class ProfilFormular(FlaskForm):
    vorname = StringField('Vorname', validators=[DataRequired(message="Bitte Vornamen eingeben.")])
    nachname = StringField('Nachname', validators=[DataRequired(message="Bitte Nachnamen eingeben.")])
    email = StringField('E-Mail', validators=[DataRequired(message="Bitte E-Mail eingeben."), Email(message="Ungültige E-Mail.")])
    telefon = StringField('Telefonnummer', validators=[DataRequired(message="Bitte Telefonnummer eingeben.")])
    adresse = StringField('Adresse', validators=[DataRequired(message="Bitte Adresse eingeben.")])
    plz = StringField('PLZ', validators=[DataRequired(message="Bitte PLZ eingeben.")])
    ort = StringField('Ort', validators=[DataRequired(message="Bitte Ort eingeben.")])
    submit = SubmitField('Änderungen speichern')

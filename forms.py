from datetime import date
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, DateField, HiddenField, SubmitField, SelectField, TextAreaField, BooleanField, EmailField)
from wtforms.validators import (DataRequired, Email, EqualTo, Length, InputRequired, ValidationError)

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

def check_geburtsdatum(form, field):
    if field.data:
        if ((date.today() - field.data).days / 365.25) < 18:
            raise ValidationError(
                "Du musst mindestens 18 Jahre alt sein."
            )
class RegistrierungFormular(FlaskForm):    
    vorname = StringField("Vorname", validators=[InputRequired()])
    nachname = StringField("Nachname", validators=[InputRequired()])
    geschlecht = SelectField(
        "Geschlecht",
        choices=[("", "--Bitte wählen--"), ("M", "Männlich"), ("W", "Weiblich"), ("D", "Divers")],
        validators=[DataRequired()]
    )
    geburtsdatum = DateField("Geburtsdatum", validators=[InputRequired(), check_geburtsdatum])
    adresse = StringField("Adresse", validators=[InputRequired()])
    plz = StringField("PLZ", validators=[InputRequired()])
    ort = SelectField("Ort",
        choices=[("", "--Bitte wählen--"), ("Berlin", "Berlin")],
        validators=[InputRequired()])
    email = EmailField("E-Mail", validators=[InputRequired()])
    telefon = StringField("Telefon", validators=[InputRequired()])
    passwort = PasswordField("Passwort", validators=[InputRequired(), Length(min=8)])
    passwort_wiederholen = PasswordField("Passwort wiederholen", validators=[InputRequired(), EqualTo("passwort")])
    registrieren = SubmitField("Registrieren")

class ProfilFormular(FlaskForm):
    vorname = StringField('Vorname', validators=[DataRequired(message="Bitte Vornamen eingeben.")])
    nachname = StringField('Nachname', validators=[DataRequired(message="Bitte Nachnamen eingeben.")])
    email = StringField('E-Mail', validators=[DataRequired(message="Bitte E-Mail eingeben."), Email(message="Ungültige E-Mail.")])
    telefon = StringField('Telefonnummer', validators=[DataRequired(message="Bitte Telefonnummer eingeben.")])
    adresse = StringField('Adresse', validators=[DataRequired(message="Bitte Adresse eingeben.")])
    plz = StringField('PLZ', validators=[DataRequired(message="Bitte PLZ eingeben.")])
    ort = StringField('Ort', validators=[DataRequired(message="Bitte Ort eingeben.")])
    submit = SubmitField('Änderungen speichern')